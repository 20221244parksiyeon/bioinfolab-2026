# lab07 정리: 함수와 모듈로 FASTA 도구 만들기

## 1. 핵심 내용

- `def`로 함수를 만들고, `return`으로 값을 돌려준다.
- 자주 쓰는 함수를 `src/fasta.py` 한 파일(모듈)에 모아 두고, 다른 스크립트에서 `from fasta import ...`로 불러 쓴다.
- `sys.argv`로 명령행 인자(입력 파일, 출력 파일, 기준값)를 받는다.
- `open(파일, "w")`로 결과를 파일(TSV, FASTA)에 저장한다.
- `if __name__ == "__main__":` 안의 코드는 파일을 직접 실행할 때만 동작하고, import할 때는 동작하지 않는다.

## 2. 폴더 구성

```
lab07/
├── gc_content.py      # gc_content 함수 연습 (빈 서열 처리)
├── summary.tsv        # batchinfo.py 실행 결과
├── data/              # seqs.fasta, seqs2.fasta, lower.fasta
├── doc/               # python_cheatsheet.md, summary.tsv, long.fasta
└── src/               # fasta.py 모듈과 이를 사용하는 스크립트
```

## 3. fasta.py 모듈의 함수

| 함수 | 입력 | 반환 |
|---|---|---|
| `read_fasta(filename)` | FASTA 파일 경로 | `{이름: 서열}` 딕셔너리 (이름은 헤더의 첫 단어, 서열은 대문자로 변환) |
| `gc_content(seq)` | 서열 문자열 | G+C 비율(0~1). 빈 서열은 `0.0` |
| `write_fasta(seqs, filename)` | 서열 딕셔너리, 저장 경로 | 없음 (FASTA 파일로 저장) |
| `reverse_complement(seq)` | DNA 서열 | 역상보 서열 |
| `length_stats(seqs)` | 서열 딕셔너리 | `count`, `total`, `average`, `min`, `max` 딕셔너리 |

함수별 사용 예는 `lab07/src/README.md`에 정리되어 있다.

## 4. 모듈을 사용하는 스크립트

`lab07` 폴더에서 실행한다고 가정한다.

| 스크립트 | 하는 일 | 실행 예 |
|---|---|---|
| `countseq2.py` | 서열 개수 출력 | `python3 src/countseq2.py data/seqs.fasta` |
| `seqlen2.py` | 서열별 이름과 길이 출력 | `python3 src/seqlen2.py data/seqs.fasta` |
| `stats.py` | 개수·전체/평균/최소/최대 길이 출력 | `python3 src/stats.py data/seqs.fasta` |
| `summary.py` | 서열별 이름·길이·GC를 TSV로 저장 | `python3 src/summary.py data/seqs.fasta doc/summary.tsv` |
| `filter_fasta.py` | 최소 길이 이상인 서열만 FASTA로 저장 | `python3 src/filter_fasta.py data/seqs.fasta 20 doc/long.fasta` |
| `batchinfo.py` | 폴더의 모든 `.fasta/.fa/.fna` 파일을 요약해 TSV로 저장 | `python3 src/batchinfo.py data summary.tsv` |
| `filter.py` | 길이 20~40, GC 0.4~0.6, N 5개 미만 조건 검사 (모듈 없이 함수를 직접 정의한 버전) | `python3 src/filter.py data/seqs.fasta` |

그 밖에 `problem1.py`는 print와 return의 차이를 확인하는 연습 문제이고, `check_codespace.sh`는 Codespace 환경을 확인하는 스크립트이다.

## 5. 실행 결과

**`doc/summary.tsv`** (`data/seqs.fasta`의 서열별 요약)

| name | length | gc |
|---|---|---|
| gene1 | 30 | 0.5 |
| gene2 | 15 | 0.4667 |
| gene3 | 29 | 0.2759 |

**`doc/long.fasta`**: 길이 20 이상인 gene1(30), gene3(29)만 저장되었다.

**`summary.tsv`** (`batchinfo.py`로 data 폴더 전체 요약)

| filename | count | total | mean_gc |
|---|---|---|---|
| lower.fasta | 2 | 20 | 0.6500 |
| seqs.fasta | 3 | 74 | 0.4142 |
| seqs2.fasta | 2 | 16 | 0.2500 |

`lower.fasta`는 소문자 서열이지만 `read_fasta`가 대문자로 바꾸기 때문에 GC가 바르게 계산된다.

## 6. print와 return의 차이 (problem1.py)

```python
def f(x):
    print(x * 2)   # 화면에 출력만 하고 반환값은 None

def g(x):
    return x * 2   # 값을 돌려줌
```

- `a = f(3)` → 6을 출력하고, `a`에는 `None`이 들어간다.
- `b = g(3)` → `b`는 6이다. 따라서 `print(a, b)`는 `None 6`을 출력한다.
- `g(g(3))` → 12
- `f(f(3))` → 6을 출력한 뒤 `None * 2`를 계산하다가 `TypeError`가 난다.

## 7. 겪은 오류

1. `batchinfo.py`를 저장하지 않아 파일을 찾을 수 없다는 오류가 났다. 올바른 경로에 저장해서 해결했다.
2. 실행이 실패해 `summary.tsv`가 만들어지지 않아 `cat`으로 확인할 수 없었다. 프로그램을 정상 실행한 뒤 다시 확인했다.

## 8. 보완할 점

- 잘못된 FASTA 형식이나 중복된 서열 이름 검사
- `N` 같은 불확실한 염기 처리
- `reverse_complement`가 A/T/G/C 이외의 문자(예: `N`)를 만나면 `KeyError`가 난다.
- `filter.py`는 길이가 0인 서열이 있으면 GC 계산에서 0으로 나누는 오류가 난다. `fasta.gc_content`를 쓰면 해결된다.
