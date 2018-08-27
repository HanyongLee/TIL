import webbrowser

keywords = ["아이유","수지","설현"]
url = "https://search.naver.com/search.naver?query="

#webbrowser.open(url + keywords[0])
#webbrowser.open(url + keywords[1])
#webbrowser.open(url + keywords[2])

for name in keywords:
    webbrowser.open(url + name)
