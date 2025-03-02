# PyPI 패키지 업로드 가이드

## PyPI에 업로드될 파일 목록

1. **패키지 소스 코드**:
   - `lakeel/` 디렉토리 (패키지 루트)
   - `lakeel/__init__.py` (패키지 초기화 파일)
   - `lakeel/lakeel.py` (실제 코드 파일)

2. **패키지 메타데이터**:
   - `setup.py` (패키지 빌드 및 배포 설정)
   - `README.md` (패키지 설명서)
   - `LICENSE` (라이센스 정보)

3. **빌드 및 배포 파일** (자동 생성되며 업로드 과정에서 생성됨):
   - `dist/` 디렉토리 (wheel 및 tar.gz 파일이 포함됨)
   - `build/` 디렉토리 (빌드 중간 파일)
   - `lakeel.egg-info/` 디렉토리 (메타데이터 파일)

## main 브랜치에 merge 해야 할 필수 파일들

main 브랜치에 merge할 때 필요한 파일들:

1. `lakeel/` 디렉토리 (모든 내용 포함)
2. `setup.py` (버전 업데이트 필수)
3. `README.md`
4. `LICENSE`

## merge하지 않아도 되는 파일들

다음 파일들은 테스트용이거나 자동 생성되므로 merge하지 않아도 됩니다:

- `test.py`, `test_llama.py`, `test.ipynb`, `temp_task.py` 등의 테스트 파일
- `__pycache__/` 디렉토리 (캐시 파일)
- `.git/` 디렉토리
- `dist/`, `build/`, `lakeel.egg-info/` 디렉토리 (자동 생성됨)

## PyPI 업로드 과정 및 실행 명령어

### 1. 버전 업데이트

`setup.py` 파일에서 버전 번호 업데이트:

```python
setup(
    name="lakeel",
    version="x.x.x",  # 여기서 버전 번호 변경 (현재 0.0.5)
    ...
)
```

### 2. 필요한 패키지 설치

```bash
pip install --upgrade setuptools wheel twine
```

### 3. 배포 파일 생성

```bash
python setup.py sdist bdist_wheel
```

### 4. PyPI에 업로드

테스트 PyPI에 업로드 (선택사항):
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

정식 PyPI에 업로드:
```bash
twine upload dist/*
```

### 5. Git 작업 과정

dev 브랜치에서 개발 완료 후 main에 merge하는 과정:

```bash
# 현재 브랜치가 dev인지 확인
git branch

# 변경 사항 확인
git status

# 필요한 파일만 스테이징
git add lakeel/ setup.py README.md LICENSE

# 커밋
git commit -m "버전 x.x.x 업데이트"

# main 브랜치로 전환
git checkout main

# dev 브랜치의 변경 사항을 main에 merge
git merge dev

# 원격 저장소에 push
git push origin main
```

## 참고사항

- 새 버전을 배포할 때마다 `setup.py`의 버전 번호를 반드시 업데이트해야 합니다.
- 같은 버전 번호로 PyPI에 재배포할 수 없습니다.
- `dist/` 디렉토리의 이전 버전 파일이 있으면 삭제 후 새로 빌드하는 것이 좋습니다. 