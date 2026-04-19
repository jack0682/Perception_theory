# Colab에서 로컬 폴더 마운트 방법

## 방법 1️⃣: Google Drive 마운트 (권장)

### 1단계: 로컬 폴더를 Google Drive에 업로드
```bash
# 로컬에서 실행
# 방법 A: Google Drive 웹에서 수동 업로드
#   1. Google Drive 열기 (drive.google.com)
#   2. Perception_theory 폴더 전체 업로드
#   3. 경로 기억: /My Drive/Perception_theory/

# 방법 B: 명령어로 자동 업로드 (macOS)
brew install --cask google-drive
# Google Drive 동기화 설정 후 폴더 복사
```

### 2단계: Colab에서 마운트

```python
# Colab 셀 1: Google Drive 마운트
from google.colab import drive
drive.mount('/content/gdrive')

# Colab 셀 2: 경로 설정
import sys
perception_path = '/content/gdrive/My Drive/Perception_theory'
sys.path.insert(0, perception_path)

# Colab 셀 3: 확인
import os
os.listdir(f'{perception_path}/experiments')
```

**장점:** 파일 자동 동기화, 결과 저장 시 로컬에도 반영  
**단점:** 용량 제한 (Google Drive 기본 15GB)

---

## 방법 2️⃣: GitHub 푸시 후 클론 (베스트 프랙티스)

### 1단계: 로컬 Git 저장소 설정
```bash
cd /Users/ojaehong/Perception
git init
git remote add origin https://github.com/yourusername/Perception.git
git add -A
git commit -m "Initial commit: SCC experiments"
git push -u origin main
```

### 2단계: Colab에서 클론

```python
# Colab 셀 1: 저장소 클론
!git clone https://github.com/yourusername/Perception.git /content/Perception

# Colab 셀 2: 경로 설정
import sys
sys.path.insert(0, '/content/Perception/Perception_theory')

# Colab 셀 3: 실험 실행
%cd /content/Perception/Perception_theory
!python3 experiments/exp_cohesion_scale.py --max-size 256 --n-workers 2
```

**장점:** 버전 관리, 재현성 높음, 공유 용이  
**단점:** 매번 push 필요

---

## 방법 3️⃣: 직접 업로드 (빠른 테스트용)

```python
# Colab 셀 1: 파일 업로드
from google.colab import files
uploaded = files.upload()

# 결과: experiments/ 폴더를 zip으로 압축하여 업로드

# Colab 셀 2: 압축 해제
import zipfile
zipfile.ZipFile('experiments.zip').extractall('/content/')

# Colab 셀 3: 사용
import sys
sys.path.insert(0, '/content')
```

**장점:** 설정 간단, 즉시 사용 가능  
**단점:** 매번 업로드 필요, 용량 제한 (약 1GB)

---

## 방법 4️⃣: Colab Files API + 다운로드 (추천 조합)

```python
# Colab 셀 1: 실험 실행
%cd /content/Perception_theory
!python3 experiments/exp_cohesion_scale.py --max-size 256 --n-workers 2

# Colab 셀 2: 결과 다운로드
from google.colab import files
files.download('experiments/results/cohesion_scale_test.json')
files.download('experiments/results/cohesion_scale_analysis.png')
```

**이 방법:**
- 로컬 폴더를 GitHub에 push
- Colab에서 clone
- 결과를 다운로드하여 로컬에서 보기

---

## 완전한 Colab 스크립트 (GitHub 기반)

```python
# ===== 셀 1: 저장소 클론 및 설정 =====
!git clone https://github.com/yourusername/Perception.git /content/Perception
%cd /content/Perception/Perception_theory

import sys
sys.path.insert(0, '/content/Perception/Perception_theory')

# ===== 셀 2: 의존성 설치 =====
!pip install -q numpy scipy networkx matplotlib

# ===== 셀 3: 실험 실행 =====
!python3 experiments/exp_cohesion_scale.py \
    --max-size 256 \
    --n-workers 2 \
    --output experiments/results/cohesion_scale_test.json

# ===== 셀 4: 결과 확인 =====
import json
with open('experiments/results/cohesion_scale_test.json') as f:
    results = json.load(f)

for key, val in results.items():
    print(f"{key}: Bind={val['bind']:.4f}, Time={val['time_sec']:.1f}s")

# ===== 셀 5: 결과 다운로드 =====
from google.colab import files
files.download('experiments/results/cohesion_scale_test.json')
files.download('experiments/results/cohesion_scale_analysis.png')
```

---

## 빠른 참조 표

| 방법 | 설정 | 속도 | 추천 상황 |
|------|------|------|---------|
| **Google Drive** | 중간 | 보통 | 자주 실행하는 경우 |
| **GitHub** | 쉬움 | 빠름 | 버전 관리 필요 시 |
| **직접 업로드** | 가장 쉬움 | 매우 느림 | 빠른 테스트 용 |
| **GitHub + Download** | 쉬움 | 빠름 | **가장 추천** ⭐ |

---

## 추천 워크플로우

```bash
# 1. 로컬에서 작업 후 GitHub에 push
git add experiments/exp_cohesion_scale.ipynb
git commit -m "Add notebook version"
git push origin main

# 2. Colab에서 실행
# → Colab 셀에서 git clone 실행

# 3. 결과 다운로드
# → files.download() 사용

# 4. 로컬에서 결과 분석
open experiments/results/cohesion_scale_test.json
```
