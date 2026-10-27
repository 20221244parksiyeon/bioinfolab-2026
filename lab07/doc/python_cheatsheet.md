# 나의 Bash·Python 치트시트

## 1. 자주 사용할 명령어

| Bash | 기능 | 같은 일을 하는 Python 코드 |
|---|---|---|
| `ls src` | 파일·폴더 목록 확인 | `import os; print(os.listdir("src"))` |
| `cd lab05` | 폴더 이동 | `import os; os.chdir("lab05")` |
| `grep "^seqs.fasta" seq_counts.txt` | 조건에 맞는 줄 검색 | 아래 검색 예시 참고 |
| `grep -c "^>" data/seqs.fasta` | FASTA 헤더 개수 계산 | 아래 개수 계산 예시 참고 |
| `grep -v "^>" data/seqs.fasta` | 헤더가 아닌 줄 출력 | 아래 제외 출력 예시 참고 |
| `ls \| wc -l` | 현재 폴더 항목 개수 계산 | `import os; print(len([x for x in os.listdir(".") if not x.startswith(".")]))` |
| `cut -f2` | 탭으로 구분된 두 번째 필드 추출 | `print(line.rstrip("\n").split("\t")[1])` |
| `chmod +x src/countseq.sh` | 실행 권한 부여 | `python3 src/countseq.py`로 실행할 때는 실행 권한을 추가할 필요가 없다. |

### 조건에 맞는 줄 검색

```python
import re

with open("seq_counts.txt") as f:
    for line in f:
        if re.search(r"^seqs.fasta", line):
            print(line, end="")
```

### FASTA 헤더 개수 계산

```python
with open("data/seqs.fasta") as f:
    count = sum(1 for line in f if line.startswith(">"))

print(count)
```

### 헤더가 아닌 줄 출력

```python
with open("data/seqs.fasta") as f:
    for line in f:
        if not line.startswith(">"):
            print(line, end="")
```

## 2. 꼭 기억할 Bash 문법과 Python 대응

| Bash 문법 | 의미 | Python 대응 |
|---|---|---|
| `$1`, `$2` | 첫 번째, 두 번째 명령행 인자 | `sys.argv[1]`, `sys.argv[2]` (`import sys` 필요) |
| `$#` | 입력한 인자 개수 | `len(sys.argv) - 1` |
| `$?` | 직전 명령의 종료 상태 | 외부 명령 실행 시 `result.returncode` 사용 |
| `\|` | 앞 명령의 출력을 뒤 명령으로 전달 | 함수의 반환값을 다음 함수에 전달하거나 변수에 저장해 처리 |
| `>` | 파일을 덮어써서 저장 | `open("result.txt", "w")` |
| `>>` | 기존 파일 뒤에 추가 | `open("result.txt", "a")` |
| `$(명령어)` | 명령 실행 결과를 값으로 사용 | `subprocess.check_output()` 또는 Python 함수의 반환값 사용 |
| `*` | 파일 패턴에서 문자 0개 이상과 일치 | `glob.glob("data/*.fasta")` |

※ 정규표현식에서 `*`는 앞의 패턴을 0회 이상 반복한다는 뜻이다.
임의의 문자 0개 이상을 나타내려면 `.*`를 사용한다.

### 외부 명령 실행과 종료 상태 확인

```python
import subprocess

result = subprocess.run(["ls", "src"])
print(result.returncode)
```

### 파일에 저장하거나 추가하기

```python
with open("result.txt", "w") as f:
    f.write("새 결과\n")

with open("result.txt", "a") as f:
    f.write("추가 결과\n")
```

### 명령 실행 결과를 변수에 저장하기

```python
import subprocess

output = subprocess.check_output(["ls", "src"], text=True)
print(output)
```

## 3. 내가 실수했던 것과 Python에서 주의할 점

1. Bash에서는 `DIR=$1`처럼 대입할 때 공백을 넣지 않는다.
   Python에서는 `DIR = sys.argv[1]`처럼 공백을 넣어도 된다.

2. Bash의 `for`문은 마지막에 `done`이 필요하다.
   Python은 `done` 대신 콜론과 들여쓰기로 반복 범위를 구분한다.

3. Bash의 `$1`과 Python의 `sys.argv[1]`을 사용할 때는 실행 인자를 전달해야 한다.
   Python에서는 `len(sys.argv)`로 인자 개수를 먼저 확인한다.

4. 출력 결과를 터미널 명령으로 다시 입력하지 않는다.
   이 주의사항은 Python을 실행할 때도 동일하다.

## 4. 스크립트 만드는 5단계

| 단계 | Bash | Python |
|---|---|---|
| 1 | 터미널에서 명령을 직접 실행한다. | Python REPL에서 코드를 직접 실행한다. |
| 2 | 동작하는 명령을 `.sh` 파일에 넣는다. | 동작하는 코드를 `.py` 파일에 넣는다. |
| 3 | 파일명 등 바뀌는 값을 변수로 만든다. | 파일명 등 바뀌는 값을 변수로 만든다. |
| 4 | `$1`, `$2`로 명령행 인자를 받는다. | `sys.argv[1]`, `sys.argv[2]`로 인자를 받는다. |
| 5 | 인자 개수와 파일 존재 여부를 검사한다. | `len(sys.argv)`와 `os.path.isfile()`로 검사하고, 오류가 있으면 `sys.exit(1)`로 종료한다. |

## 5. 자주 쓰는 반복문

### Bash

```bash
for F in data/*.fasta
do
    COUNT=$(grep -c "^>" "$F")
    echo "$F : $COUNT"
done
```

### Python

```python
import glob

for path in sorted(glob.glob("data/*.fasta")):
    with open(path) as f:
        count = sum(1 for line in f if line.startswith(">"))
    print(f"{path} : {count}")

## 함수와 모듈

### def로 함수 만들기
```python
def add(a, b):
    return a + b
```

### print와 return의 차이
print는 화면에 출력하고, return은 호출한 곳에 값을 돌려준다.

### 모듈에서 함수 불러오기
```python
from fasta import read_fasta
```

### 직접 실행할 때만 실행하기
다음 조건문 안의 코드는 파일을 직접 실행할 때 실행되며, 다른 파일에서 import할 때는 실행되지 않는다.
```python
if __name__ == "__main__":
    main()
```
※ main()은 별도로 정의한 함수이다.

## 함수와 모듈

### def로 함수 만들기
```python
def add(a, b):
    return a + b
```

### print와 return의 차이
print는 화면에 출력하고, return은 호출한 곳에 값을 돌려준다.

### 모듈에서 함수 불러오기
```python
from fasta import read_fasta
```

### 직접 실행할 때만 실행하기
다음 조건문 안의 코드는 파일을 직접 실행할 때 실행되며, 다른 파일에서 import할 때는 실행되지 않는다.
```python
if __name__ == "__main__":
    main()
```
※ main()은 별도로 정의한 함수이다.

## 파일 저장 모드

- "w": 기존 내용을 지우고 새로 저장한다. Bash의 >와 같다.
- "a": 기존 내용 뒤에 추가한다. Bash의 >>와 같다.
- 두 모드 모두 파일이 없으면 새로 만든다.

## 오늘 겪은 오류 두 가지

1. batchinfo.py를 저장하지 않아 실행 시 파일을 찾을 수 없다는 오류가 발생했다. 올바른 경로에 코드를 저장하여 해결했다.
2. 실행이 실패해 summary.tsv가 생성되지 않았으므로 cat 명령어로 결과를 확인할 수 없었다. 프로그램을 정상 실행한 뒤 다시 확인했다.