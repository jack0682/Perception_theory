#!/usr/bin/env python3
"""
Automated quality checker for SCC textbook figures.
Checks: file format, size, aspect ratio, DPI, and generates a summary report.

Usage:
    python3 docs/04-04/textbook_build/figures/check_quality.py
"""

import os
import sys
import csv
import json
from pathlib import Path
from datetime import datetime

# Try importing optional deps
try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

try:
    import fitz  # PyMuPDF for PDF inspection
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False


FIGURES_DIR = Path(__file__).parent
PARTS = ["P1_foundations", "P2_formal", "P3_experiments", "P4_applications"]

# Quality thresholds
MAX_FILE_SIZE_KB = 500
MIN_DPI = 200
TARGET_DPI = 300
MAX_ASPECT_RATIO = 1.8  # width/height
MAX_WIDTH_MM = 170  # A4 text column width
VALID_FORMATS = {".pdf", ".png", ".svg"}


def get_file_info(filepath: Path) -> dict:
    """Gather basic file info."""
    stat = filepath.stat()
    return {
        "filename": filepath.name,
        "part": filepath.parent.name,
        "path": str(filepath),
        "format": filepath.suffix.lower(),
        "size_kb": round(stat.st_size / 1024, 1),
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
    }


def check_png(filepath: Path, info: dict) -> list:
    """Check PNG-specific quality."""
    issues = []
    if not HAS_PIL:
        issues.append("WARN: PIL not installed, cannot check PNG details")
        return issues

    img = Image.open(filepath)
    w, h = img.size
    info["width_px"] = w
    info["height_px"] = h

    # DPI
    dpi_info = img.info.get("dpi", (72, 72))
    dpi = max(dpi_info) if isinstance(dpi_info, (tuple, list)) else dpi_info
    info["dpi"] = round(dpi)
    if dpi < MIN_DPI:
        issues.append(f"LOW_DPI: {dpi:.0f} dpi (need >= {MIN_DPI})")

    # Aspect ratio
    aspect = w / h if h > 0 else 999
    info["aspect_ratio"] = round(aspect, 2)
    if aspect > MAX_ASPECT_RATIO:
        issues.append(f"WIDE: aspect {aspect:.2f} > {MAX_ASPECT_RATIO}")

    # Estimated print width at DPI
    if dpi > 0:
        width_mm = (w / dpi) * 25.4
        info["est_width_mm"] = round(width_mm, 1)
        if width_mm > MAX_WIDTH_MM * 1.1:  # 10% tolerance
            issues.append(f"TOO_WIDE: {width_mm:.0f}mm > {MAX_WIDTH_MM}mm at {dpi:.0f}dpi")

    return issues


def check_pdf(filepath: Path, info: dict) -> list:
    """Check PDF-specific quality."""
    issues = []
    if not HAS_FITZ:
        # Fallback: just check file size
        info["note"] = "PyMuPDF not installed, limited PDF checks"
        return issues

    doc = fitz.open(filepath)
    if doc.page_count == 0:
        issues.append("EMPTY: PDF has 0 pages")
        return issues

    page = doc[0]
    rect = page.rect
    w_pt, h_pt = rect.width, rect.height
    # Convert points to mm (1 pt = 0.3528 mm)
    w_mm = w_pt * 0.3528
    h_mm = h_pt * 0.3528
    info["width_mm"] = round(w_mm, 1)
    info["height_mm"] = round(h_mm, 1)

    aspect = w_mm / h_mm if h_mm > 0 else 999
    info["aspect_ratio"] = round(aspect, 2)
    if aspect > MAX_ASPECT_RATIO:
        issues.append(f"WIDE: aspect {aspect:.2f} > {MAX_ASPECT_RATIO}")
    if w_mm > MAX_WIDTH_MM * 1.1:
        issues.append(f"TOO_WIDE: {w_mm:.0f}mm > {MAX_WIDTH_MM}mm")

    doc.close()
    return issues


def check_figure(filepath: Path) -> dict:
    """Run all checks on a single figure file."""
    info = get_file_info(filepath)
    issues = []

    # Format check
    if info["format"] not in VALID_FORMATS:
        issues.append(f"BAD_FORMAT: {info['format']} not in {VALID_FORMATS}")

    # Size check
    if info["size_kb"] > MAX_FILE_SIZE_KB:
        issues.append(f"TOO_LARGE: {info['size_kb']}KB > {MAX_FILE_SIZE_KB}KB")

    # Format-specific checks
    if info["format"] == ".png":
        issues.extend(check_png(filepath, info))
    elif info["format"] == ".pdf":
        issues.extend(check_pdf(filepath, info))

    info["issues"] = issues
    info["status"] = "PASS" if not issues else "FAIL"
    return info


def scan_all_figures() -> list:
    """Scan all figure directories and check each file."""
    results = []
    for part in PARTS:
        part_dir = FIGURES_DIR / part
        if not part_dir.exists():
            continue
        for f in sorted(part_dir.iterdir()):
            if f.suffix.lower() in VALID_FORMATS:
                results.append(check_figure(f))
    return results


def write_report(results: list):
    """Write QUALITY_REPORT.md."""
    report_path = FIGURES_DIR / "QUALITY_REPORT.md"
    total = len(results)
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = total - passed

    lines = [
        "# Figure Quality Report",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M KST')}",
        f"**Total figures:** {total}",
        f"**Passed:** {passed}  |  **Failed:** {failed}",
        "",
        "---",
        "",
    ]

    if failed > 0:
        lines.append("## Issues Found\n")
        for r in results:
            if r["status"] == "FAIL":
                lines.append(f"### `{r['part']}/{r['filename']}`")
                for issue in r["issues"]:
                    lines.append(f"- {issue}")
                lines.append("")

    lines.append("## Full Results\n")
    lines.append("| Part | Filename | Format | Size (KB) | Aspect | Status | Issues |")
    lines.append("|------|----------|--------|-----------|--------|--------|--------|")
    for r in results:
        issues_str = "; ".join(r["issues"]) if r["issues"] else "-"
        aspect = r.get("aspect_ratio", "-")
        lines.append(
            f"| {r['part']} | {r['filename']} | {r['format']} | {r['size_kb']} | {aspect} | {r['status']} | {issues_str} |"
        )

    lines.append("")
    lines.append("---")
    lines.append(f"\n*Report generated by check_quality.py*")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written to {report_path}")


def write_manifest(results: list):
    """Write MANIFEST.csv."""
    manifest_path = FIGURES_DIR / "MANIFEST.csv"
    with open(manifest_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Filename", "Part", "Chapter", "Caption", "Page_Ref", "Status"])
        for r in results:
            # Map part dir to chapter range
            ch_map = {
                "P1_foundations": "Ch1-3",
                "P2_formal": "Ch4-8",
                "P3_experiments": "Ch9-13",
                "P4_applications": "Ch14-15",
            }
            chapter = ch_map.get(r["part"], "?")
            writer.writerow([
                r["filename"],
                r["part"],
                chapter,
                "",  # Caption TBD
                "",  # Page ref TBD
                r["status"],
            ])
    print(f"Manifest written to {manifest_path}")


def main():
    print("=" * 60)
    print("SCC Textbook Figure Quality Checker")
    print("=" * 60)

    results = scan_all_figures()

    if not results:
        print("\nNo figure files found in subdirectories.")
        print("Expected figures in: " + ", ".join(PARTS))
        print("Supported formats: " + ", ".join(VALID_FORMATS))
        # Create empty report
        write_report(results)
        write_manifest(results)
        return

    # Summary
    total = len(results)
    passed = sum(1 for r in results if r["status"] == "PASS")
    print(f"\nScanned {total} figures: {passed} passed, {total - passed} failed")

    # Write outputs
    write_report(results)
    write_manifest(results)

    # Print failures
    failures = [r for r in results if r["status"] == "FAIL"]
    if failures:
        print(f"\n{'='*40}")
        print(f"FAILURES ({len(failures)}):")
        for r in failures:
            print(f"  {r['part']}/{r['filename']}: {'; '.join(r['issues'])}")

    print("\nDone.")


if __name__ == "__main__":
    main()
