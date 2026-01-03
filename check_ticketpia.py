from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def open_ticketpia():
    # Chromeオプションを設定（ヘッドレスモードでGUIなし）
    options = Options()
    #options.add_argument("--headless")  # GUIなしで実行
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Chromeドライバーを自動でインストール
    service = Service(ChromeDriverManager().install())

    # Chromeを起動
    driver = webdriver.Chrome(service=service, options=options)

    # チケットぴあのサイトを開く
    url = "https://t.pia.jp/"
    driver.get(url)

    # ページが読み込まれるまで少し待つ
    time.sleep(3)

    # ページタイトルを表示（確認用）
    print("ページタイトル:", driver.title)

    # ブラウザを閉じる
    driver.quit()

if __name__ == "__main__":
    open_ticketpia()