import json
import lang


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
    try:
        f = open('./resources/app/.webpack/renderer/main.bundle.js', 'r', encoding='UTF8')
    except FileNotFoundError:
        print('main.bundle.js를 못찾았어요. Vampire Survivors 홈 경로가 맞나요?' +
              '\r\n보통 steamapps\\common\\Vampire Survivors에 있답니다\r\n' +
              '스팀 라이브러리 -> 속성 -> 로컬파일 -> 찾아보기... 하면 나오는 곳에 파일을 위치해주세요')
        close()
    originalCodes = f.read()
    codes = originalCodes
    f.close()
    # 하드코딩부분 번역
    translations = lang['translations']
    for row in translations:
        codes = codes.replace(row['original'], row['korean'])
    f = open('./resources/app/.webpack/renderer/main.bundle.js', 'w', encoding='UTF-8')
    f.write(codes)
    f.close()

    # 번역부분 업데이트
    for row in lang['lang']:
        f = open("./resources/app/.webpack/renderer/assets/lang/%s" % row['fileName'], 'r', encoding='UTF-8-sig')
        langFile = json.loads(f.read())
        translationLang = row['translations']
        f.close()
        for key, val in langFile['en']['translations'].items():
            langFile['en']['translations'][key] = translationLang[key]
        data = json.dumps(langFile, ensure_ascii=False)
        f = open("./resources/app/.webpack/renderer/assets/lang/%s" % row['fileName'], 'w', encoding='UTF-8-sig')
        f.write(data)
        f.close()

    print("%d글자 -> %d글자로 총 길이 변경됨. %d개 lang파일 변경.\r\n패치가 안되었다면 무결성검사 후 다시 실행해주세요~" % (len(originalCodes), len(codes), len(lang['lang'])))
    close()
