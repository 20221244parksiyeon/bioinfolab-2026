import sys
import os

if len(sys.argv) < 2:
    print("사용법: python3 src/mkproject.py <프로젝트이름>")
    sys.exit(1)

project = sys.argv[1]

if os.path.isdir(project):
    print("오류: 이미 존재하는 폴더입니다:", project)
    sys.exit(1)

os.makedirs(project + "/data")
os.makedirs(project + "/doc")
os.makedirs(project + "/src")

print("프로젝트 생성 완료:", project)