# lakeel - 한국인을 위한 파이썬 편의성 패키지
### Made by. bunhine0452
- Email: hb000122@gmail.com

---

## 목차
1. [설치 방법](#설치-방법)
2. [패키지 소개](#패키지-소개)
3. [주요 기능](#주요-기능)
   - [패키지 관리 기능](#패키지-관리-기능)
   - [한글 텍스트 처리 기능](#한글-텍스트-처리-기능)
   - [한국식 날짜/시간 처리](#한국식-날짜시간-처리)
   - [한국식 데이터 포맷팅](#한국식-데이터-포맷팅)
   - [한글 파일 경로 처리](#한글-파일-경로-처리)
   - [한글 시각화 지원](#한글-시각화-지원)
   - [기타 유틸리티](#기타-유틸리티)
4. [사용 예제](#사용-예제)
5. [기여 방법](#기여-방법)
6. [라이선스](#라이선스)

---

## 설치 방법

다음 명령어로 pip 패키지 `lakeel`을 설치할 수 있습니다.

```bash
pip install lakeel
```

최신 개발 버전을 직접 설치하려면:

```bash
pip install git+https://github.com/bunhine0452/pip_lakeel.git
```

## 패키지 소개

`lakeel` 패키지는 한국인 개발자를 위한 다양한 편의 기능을 제공하는 파이썬 라이브러리입니다. 패키지 관리부터 한글 텍스트 처리, 한국식 날짜/시간 포맷, 데이터 포맷팅, 파일 경로 처리, 한글 폰트를 지원하는 시각화 등 다양한 기능을 포함하고 있습니다.

기본 사용법:

```python
import lakeel
```

## 주요 기능

### 패키지 관리 기능

#### 현재 작업 디렉토리 확인
```python
lakeel.dir()  # 현재 파이썬 코드가 실행되는 경로를 반환
```

#### 패키지 목록 확인 및 관리
```python
lakeel.pips()  # 설치된 pip 패키지 목록을 알파벳 순서대로 출력

lakeel.install("패키지명")  # 패키지 설치

lakeel.is_installed("패키지명")  # 패키지 설치 여부 확인

lakeel.update()  # 모든 패키지 업데이트
lakeel.update("패키지명")  # 특정 패키지 업데이트

lakeel.uninstall("패키지명")  # 패키지 제거

lakeel.info("패키지명")  # 패키지 정보 조회

lakeel.search("검색어")  # PyPI에서 패키지 검색
```

### 한글 텍스트 처리 기능

#### 한글 음절 분리 및 결합
```python
from lakeel import KoreanTextUtils

# 한글 음절을 초성, 중성, 종성으로 분리
KoreanTextUtils.split_syllable("가")  # ('ㄱ', 'ㅏ', '')

# 초성, 중성, 종성을 합쳐 한글 음절로 변환
KoreanTextUtils.join_syllable('ㄱ', 'ㅏ', '')  # '가'

# 텍스트의 모든 한글 문자를 자모로 분리
KoreanTextUtils.text_to_jamo("안녕하세요")  # 'ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ'
```

#### 한글 정규화 및 오타 수정
```python
# 한글 자소 정규화
KoreanTextUtils.normalize_korean("ㅅㅣㄴㅏㄹ")  # '시날'

# 한영 자판 오타 수정 (한글 자판으로 영어 입력했을 때)
KoreanTextUtils.fix_ko_en_typo("ㅗ디ㅣㅐ")  # 'hello'

# 영한 자판 오타 수정 (영어 자판으로 한글 입력했을 때)
KoreanTextUtils.fix_en_ko_typo("gksrmf")  # '안녕'
```

### 한국식 날짜/시간 처리

```python
from lakeel import KoreanDateTime
from datetime import datetime

# 날짜를 한국식으로 표기 (yyyy년 mm월 dd일)
KoreanDateTime.get_korean_date()  # '2025년 3월 2일'
KoreanDateTime.get_korean_date(datetime(2023, 1, 1))  # '2023년 1월 1일'

# 시간을 한국식으로 표기
KoreanDateTime.get_korean_time()  # '오후 3시 15분 30초'
KoreanDateTime.get_korean_time(datetime(2023, 1, 1, 9, 30, 0))  # '오전 9시 30분 0초'
```

### 한국식 데이터 포맷팅

```python
from lakeel import KoreanDataFormat

# 숫자를 한국식으로 천 단위 쉼표 포맷팅
KoreanDataFormat.format_number(1234567)  # '1,234,567'

# 금액을 원화 표시와 함께 포맷팅
KoreanDataFormat.format_currency(10000)  # '₩10,000'
KoreanDataFormat.format_currency(10000, symbol='$')  # '$10,000'

# 비율을 백분율로 변환
KoreanDataFormat.format_percent(0.123)  # '0.12%'
KoreanDataFormat.format_percent(0.123, decimal_places=1)  # '0.1%'
```

### 한글 파일 경로 처리

```python
from lakeel import KoreanFilePath

# 한글 경로를 안전하게 처리
KoreanFilePath.safe_path("C:/사용자/문서/한글경로")

# 디렉토리가 존재하지 않으면 생성
KoreanFilePath.ensure_dir("./새폴더")

# 안전한 파일명으로 변환 (특수문자 제거)
KoreanFilePath.get_safe_filename("파일명?.txt")  # '파일명_.txt'
```

### 한글 시각화 지원

```python
import matplotlib.pyplot as plt
import numpy as np
from lakeel import KoreanVisualization

# 한글 폰트 설정 (운영체제에 맞게 자동 설정)
KoreanVisualization.setup_korean_font()

# 간단한 그래프 그리기
plt.figure(figsize=(10, 6))
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('한글 제목 사용 가능')
plt.xlabel('X 축')
plt.ylabel('Y 축')
plt.show()

# 한글 지원 히트맵 생성
import pandas as pd
data = pd.DataFrame(np.random.random((5, 5)), 
                    columns=['항목1', '항목2', '항목3', '항목4', '항목5'],
                    index=['행1', '행2', '행3', '행4', '행5'])
heatmap_plt = KoreanVisualization.make_korean_heatmap(data)
heatmap_plt.show()
```

### 기타 유틸리티

#### 폰트 설정 함수
```python
# 운영체제에 맞는 폰트 설정 (시각화를 위한 기본 함수)
lakeel.sfo()
```

#### 문제 없음! 확인 함수
```python
# 귀여운 고양이 이모티콘과 함께 "문제 없음!" 메시지 출력
lakeel.jaebal()
```

## 사용 예제

### 한글 텍스트 처리 및 시각화 예제

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lakeel import KoreanTextUtils, KoreanDateTime, KoreanVisualization, jaebal

# 한글 텍스트 처리
original_text = "안녕하세요! lakeel 패키지입니다."
jamo_text = KoreanTextUtils.text_to_jamo(original_text)
print(f"원본 텍스트: {original_text}")
print(f"자모 분리: {jamo_text}")

# 한국식 날짜 표시
current_date = KoreanDateTime.get_korean_date()
current_time = KoreanDateTime.get_korean_time()
print(f"현재 날짜: {current_date}")
print(f"현재 시간: {current_time}")

# 데이터 시각화
KoreanVisualization.setup_korean_font()

# 간단한 선 그래프
plt.figure(figsize=(10, 6))
x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.title('한글 제목 - 사인 그래프')
plt.xlabel('X축 (각도)')
plt.ylabel('Y축 (사인값)')
plt.grid(True)
plt.tight_layout()
plt.savefig('korean_sine_graph.png')
plt.close()

print("그래프가 생성되었습니다!")
jaebal()  # 성공적으로 완료됨을 알리는 귀여운 고양이와 메시지 출력
```

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새 기능 브랜치를 생성합니다: `git checkout -b feature/기능이름`
3. 변경사항을 커밋합니다: `git commit -m '새 기능 추가'`
4. 브랜치를 푸시합니다: `git push origin feature/기능이름`
5. Pull Request를 제출합니다.

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

© 2023-2025 bunhine0452. All Rights Reserved.