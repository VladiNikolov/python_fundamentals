#автоматизирано извикване на определени табове в браузъра
import webbrowser as wb

def web_automation():
    chrome_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
    URLS = ('dir.bg', 'copyshop.bg', 'abv.bg')

    for url in URLS:
        print("Opening:" + url)
        wb.get(chrome_path).open(url)

web_automation()