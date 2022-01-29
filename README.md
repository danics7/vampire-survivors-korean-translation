# vampire-survivors-korean-translation

## 설치경로
 [스팀설치경로]/Vampire Survivors/

## 한글패치 다운로드
https://github.com/danics7/vampire-survivors-korean-translation/releases/latest



여기서 exe파일 다운받아서 쓰세요

경로는 VampireSurvivors 디렉토리에 직접 넣으셔서 실행시키시면 됩니다.

오역은 pr로 올려주시던가 이슈등록해주세요

코드는 이렇게 작성하고 pyinstaller를 통해서 빌드했습니다


만약 패치가 안되었다면 무결성검사 후 한번

자꾸 바이러스로 잡아대서 안잡히는 방법 확인중

## 패치노트

버전은 Vampire Survivors 버전에 맞추고 한글패치 릴리즈별로 패치넘버만 올릴예정

### v0.2.9.2 (2022-01-29)

1. lang파일 업데이트 시 덮어쓰기 방식이 아닌 키 검색 후 수정으로 변경 (업데이트시 버그발생할 위험이 있어 방식 변경)
2. 일부 오역 수정

### v0.2.9.1 (2022-01-28)

1. lang파일들도 한꺼번에 업데이트할 수 있도록 수정
2. 배포방식 구드에서 github로 변경
3. 고유명사 등 미번역 원문으로 나오도록 수정. (검색도 못해서 불편함)

### v0.2.9.0 (2022-01-27)

1. 미번역분 한글패치 배포


## 빌드방식

혹시 몰라서(까먹을것같아서) 올리는 빌드명령어

pip install pyinstaller 로 pyinstaller 설치 후 아래 명령어 입력

```angular2html
pyinstaller --onefile --icon=0.ico -n VamrpireSurvivor_한글패치.exe main.py --version-file version_info.txt
```
