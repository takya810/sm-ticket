import requests
from bs4 import BeautifulSoup
import re

def check_resale_tickets():
    url = "https://relief-ticket.jp/events/artist/11/121"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 「購入手続きへ」リンクを探す
    # purchase_links = soup.find_all('a', string="購入手続きへ")
    purchase_links = soup.find_all('button', string="購入手続きへ")
    
    available_events = []
    for link in purchase_links:
        # 親要素を取得
        parent = link.parent
        # 公演情報を含むテキストを取得
        event_text = parent.get_text()
        # 価格を抽出
        price_match = re.search(r'¥[\d,]+', event_text)
        price = price_match.group(0) if price_match else 'N/A'
        # 日付を抽出
        date_match = re.search(r'\d{4}/\d{2}/\d{2}\(\w+\) \d{2}:\d{2}', event_text)
        date = date_match.group(0) if date_match else 'N/A'
        # 会場を抽出
        venue_match = re.search(r'\[.*?\] .*', event_text)
        venue = venue_match.group(0) if venue_match else 'N/A'
        
        available_events.append({
            'date': date,
            'venue': venue,
            'price': price
        })
    
    if available_events:
        print("リセール販売可能な公演:")
        for event in available_events:
            print(f"日付: {event['date']}")
            print(f"会場: {event['venue']}")
            print(f"価格: {event['price']}")
            print("-" * 30)
    else:
        print("現在、リセール販売可能な公演はありません。")

if __name__ == "__main__":
    check_resale_tickets()
