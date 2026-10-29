# How to Design Programming

Python과 R로 작성한 주차별 프로그래밍 실습을 관리하는 저장소입니다.

## 실습 구성

| 폴더 | 실습 내용 |
| --- | --- |
| `wk1/` | 기본 연산, 문자열, 변수, 조건문과 함수 |
| `wk2/` | 거리 계산, 문자열 연결, 논리 연산 |
| `wk3/` | 시간 단위 변환, 남은 학습 시간 계산, 함수 조합 |

각 폴더에는 같은 주제의 Python(`.py`)과 R(`.R` 또는 `.r`) 예제가 있습니다.

## 실행

사용할 언어의 실행 환경(Python 3 또는 R)을 설치한 뒤 저장소 루트에서 실행합니다. 현재 예제는 별도 패키지 설치 없이 실행할 수 있습니다.

```bash
python3 wk1/wk1_1.py
Rscript wk1/wk1_1.r
```

Windows에서 Python 실행 명령이 `python` 또는 `py`라면 `python3` 대신 해당 명령을 사용합니다.

## 실습 추가 및 저장

새 주차의 실습은 `wk4/`처럼 폴더를 추가해 관리합니다. Git 명령은 이 저장소의 루트에서 실행하며, 주차별 폴더 안에서는 `git init`을 다시 실행하지 않습니다.

```bash
git status
git add .
git commit -m "Add week 4 practice"
git push
```

여러 컴퓨터에서 작업할 때는 작업 전에 `git pull --ff-only`로 최신 변경 사항을 받습니다.
