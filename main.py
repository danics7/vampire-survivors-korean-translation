import json
import lang
import shutil


def close():
    input("\r\n\r\n대충만든놈:danics\r\n종료하시려면 Enter 누르세요")
    exit()


if __name__ == '__main__':
    print(
        '=============================================================\r\n' +
        '-----------------Vampire Survivor 한글패치-------------------\r\n' +
        '=============================================================\r\n\r\n'
          )
    lang = lang.read_translation_file()
    originalPath = '.\\resources\\app\\.webpack\\renderer\\main.bundle.js'
    newPath = '.\\resources\\app\\.webpack\\renderer\\main.bundle.js.new'
    try:
        f = open(originalPath, 'r', encoding='UTF8')
    except FileNotFoundError:
        print('main.bundle.js를 못찾았어요. Vampire Survivors 홈 경로가 맞나요?' +
              '\r\n보통 steamapps\\common\\Vampire Survivors에 있답니다\r\n' +
              '스팀 라이브러리 -> 속성 -> 로컬파일 -> 찾아보기... 하면 나오는 곳에 exe 파일을 위치해주세요')
        close()
    originalCodes = f.read()
    codes = originalCodes
    f.close()
    # 하드코딩부분 번역
    translations = lang['translations']
    for row in translations:
        codes = codes.replace(row['original'], row['korean'])
    codes = codes.replace('Arial, Helvetica, sans-serif', '메이플스토리')
    f = open(newPath, 'w', encoding='UTF-8')
    f.write(codes)
    f.close()
    shutil.move(newPath, originalPath)

    # 폰트변경
    originalPath = '.\\resources\\app\\.webpack\\renderer\\vendors.bundle.js'
    newPath = '.\\resources\\app\\.webpack\\renderer\\vendors.bundle.js.new'
    f = open(originalPath, 'r', encoding='UTF8')
    originalCodes = f.read()
    codes = originalCodes
    f.close()

    codes = codes.replace('Courier', '메이플스토리')

    f = open(newPath, 'w', encoding='UTF-8')
    f.write(codes)
    f.close()
    shutil.move(newPath, originalPath)

    # 번역부분 업데이트
    for row in lang['lang']:
        langOriginalPath = ".\\resources\\app\\.webpack\\renderer\\assets\\lang\\%s" % row['fileName']
        langNewPath = ".\\resources\\app\\.webpack\\renderer\\assets\\lang\\%s.new" % row['fileName']
        f = open(langOriginalPath, 'r', encoding='UTF-8-sig')
        langFile = json.loads(f.read())
        translationLang = row['translations']
        f.close()
        for key, val in langFile['en']['translations'].items():
            langFile['en']['translations'][key] = translationLang[key] if key in translationLang else langFile['en']['translations'][key]
        data = json.dumps(langFile, ensure_ascii=False)
        f = open(langNewPath, 'w', encoding='UTF-8-sig')
        f.write(data)
        f.close()
        shutil.move(langNewPath, langOriginalPath)

    print("main.bundle.js, vendor.bundle.js(폰트수정) 변경.\r\n%d개 lang파일 변경.\r\n패치가 안되었다면 무결성검사 후 다시 실행해주세요~\r\n" % len(lang['lang']))
    print("폰트는 넥슨의 메이플스토리체로 변경되었으며, 같이 압축된 Maplestory Light.ttf 파일을 실행해서 설치해주세요.")
    close()
