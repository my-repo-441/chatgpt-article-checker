import requests
from bs4 import BeautifulSoup
import json
import re

def extract_article_content(url):
    
    # URLからHTMLを取得
    response = requests.get(url)

    # ステータスコードのチェック
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        article_contents = soup.find_all('p')
        
        # 記事の本文を結合する
        article_text = ' '.join([content.get_text(strip=True) for content in article_contents])
        return article_text
    else:
        return f"Error: Status code {response.status_code}"

