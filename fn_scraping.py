"""
# 参考文献、https://ai-inter1.com/python-selenium/
# pip install selenium==3.141.0

wsl + selenium、https://zenn.dev/takilog/articles/1895975c52727b
    依存関係の修復
    sudo apt-get install -f
pip install chromedriver-binary==99.0.4844.51.0
テストコード実行に伴い
    pip install beautifulsoup4
"""


def get_protext(url):
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    import chromedriver_binary

    # headlessモード
    option = Options()
    option.add_argument("--headless")
    driver = webdriver.Chrome(options=option)
    # url = "https://atcoder.jp/contests/abc283/tasks/abc283_b"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find("div", class_="part")
    content2 = soup.find("title")
    return content.get_text(), content2.text
