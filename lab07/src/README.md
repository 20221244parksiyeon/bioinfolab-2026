# 나의 FASTA 도구 상자

fasta.py는 FASTA 파일을 읽고 저장하거나 서열을 분석할 때 사용하는 모듈이다.

## 1. read_fasta(filename)
- 입력과 반환: FASTA 파일 경로를 받아 서열 이름을 키, 서열을 값으로 하는 딕셔너리를 반환한다.
- 사용 예:
```python
seqs = read_fasta("data/seqs.fasta")
```

## 2. gc_content(seq)
- 입력과 반환: 서열 문자열을 받아 전체 길이에서 G와 C가 차지하는 비율을 0~1 사이의 수로 반환한다. 빈 서열은 0.0을 반환한다.
- 사용 예:
```python
gc = gc_content("ATGC")
```

## 3. write_fasta(seqs, filename)
- 입력과 반환: 서열 딕셔너리와 저장할 파일 경로를 받아 FASTA 파일로 저장한다. 별도의 반환값은 없다.
- 사용 예:
```python
write_fasta(seqs, "data/output.fasta")
```

## 4. reverse_complement(seq)
- 입력과 반환: DNA 서열 문자열을 받아 역상보 서열 문자열을 반환한다.
- 사용 예:
```python
rc = reverse_complement("ATGC")
```

## 5. length_stats(seqs)
- 입력과 반환: 서열 딕셔너리를 받아 서열 개수, 전체 길이, 평균 길이, 최소 길이, 최대 길이를 딕셔너리로 반환한다.
- 사용 예:
```python
stats = length_stats(seqs)
```

## 보완하고 싶은 점
잘못된 FASTA 형식이나 중복된 서열 이름을 확인하는 기능이 필요하다. 앞으로 N 같은 불확실한 염기를 처리하고, 원하는 길이의 서열만 골라내는 함수도 추가하고 싶다.