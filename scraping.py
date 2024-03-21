import openai
import requests
import article_extractor 
import html
from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv('OPENAI_API_KEY')

# ユーザーからURLを入力して受け取る
user_input_url = input("記事のURLを入力してください: ")

# article_extractorから記事内容を取得
article_content = article_extractor.extract_article_content(user_input_url) 


prompt = article_content

messages = [
    {
        "role": "system",
        "content": ("ユーザーから渡されたpromptの具体的な修正案を箇条書きで提案してください。"
                    "修正案を提示するときは、具体的な修正箇所を明記し、元の文章と修正後の文章を比較してください。"
                    "修正案の記載形式は次を参考にして。"
                    "1. 修正前の文章。"
                    "→ 修正後の文章"
                    "最初に、「添削します。」という文字を出力してください。"
                    "出力形式は、以下のようにしてください。"
                    "○修正すべきポイントは以下です。"
                    "最後に、「添削が完了しました」という文字を出力してください。"
                    "出力形式は、No.を1列目に、修正前を2列目に、修正後を3列目にして、json形式で出力して。")
    },
    {
        "role": "user",
        "content": prompt,  # ここでの `prompt` は、このコードの外部で定義されている必要があります。
    }
]


res=openai.ChatCompletion.create(
    model="gpt-4-0125-preview",
    messages=messages,
    max_tokens = 4096
)

answer=res['choices'][0]['message']['content']
print(answer)

