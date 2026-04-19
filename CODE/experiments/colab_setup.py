#!/usr/bin/env python3
"""
Colab 실행용 셋업 스크립트
Google Colab에서 이 스크립트를 복사하여 셀에 붙여넣고 실행하세요.
"""

# ============================================================================
# Colab 셀 1: 저장소 클론 및 환경 설정
# ============================================================================
"""
!git clone https://github.com/yourusername/Perception.git
%cd /content/Perception/Perception_theory
"""

# ============================================================================
# Colab 셀 2: 의존성 설치 (필요한 경우)
# ============================================================================
"""
!pip install numpy scipy networkx matplotlib
"""

# ============================================================================
# Colab 셀 3: 실험 실행
# ============================================================================
"""
import sys
sys.path.insert(0, '/content/Perception/Perception_theory')

# 작은 스케일로 테스트 (colab에선 리소스가 제한적)
!python3 /content/Perception/Perception_theory/experiments/exp_cohesion_scale.py \\
    --max-size 256 \\
    --n-workers 2 \\
    --output /content/results.json
"""

# ============================================================================
# Colab 셀 4: 결과 다운로드 및 시각화
# ============================================================================
"""
import json
from google.colab import files

# 결과 확인
with open('/content/results.json', 'r') as f:
    results = json.load(f)

for key, val in results.items():
    print(f"{key}: Bind={val['bind']:.4f}, Energy={val['energy']:.6f}, Time={val['time_sec']:.1f}s")

# 다운로드
files.download('/content/results.json')
"""

print("""
===============================================================================
Google Colab에서 사용하는 방법
===============================================================================

1. Google Colab 열기: https://colab.research.google.com

2. 새 노트북 생성

3. 다음을 차례로 실행:

--- 셀 1: 저장소 클론 ---
!git clone https://github.com/yourusername/Perception.git
%cd /content/Perception/Perception_theory

--- 셀 2: 의존성 설치 (필요시) ---
!pip install numpy scipy networkx

--- 셀 3: 작은 규모 테스트 실행 ---
import subprocess
result = subprocess.run([
    'python3',
    'experiments/exp_cohesion_scale.py',
    '--max-size', '128',      # 작은 격자부터 시작
    '--n-workers', '2',       # Colab은 보통 2-4 코어
    '--output', 'results.json'
], capture_output=False, text=True)

--- 셀 4: 결과 확인 및 다운로드 ---
import json
with open('results.json') as f:
    results = json.load(f)
print(json.dumps(results, indent=2))

from google.colab import files
files.download('results.json')

===============================================================================
주의사항
===============================================================================

✓ 가능한 점:
  - 병렬 처리 (multiprocessing) 지원
  - 데이터 저장 및 다운로드 가능
  - CPU 리소스 충분 (2GB RAM 이상)

⚠ 주의점:
  - 런타임이 12시간 후 자동 종료 (장시간 작업은 나누어야 함)
  - 512x512 격자는 시간이 오래 걸릴 수 있음 (128-256 권장)
  - Colab 무료 버전은 리소스 제한 있음

💡 권장 Colab 설정:
  - 메모리: 12GB+ RAM 할당 (런타임 유형: GPU 선택해서 메모리 증가)
  - 최대 격자: 256x256 (512x512는 Pro 버전 권장)
  - 워커: 2-4개 (Colab VM의 코어 제한)

===============================================================================
""")
