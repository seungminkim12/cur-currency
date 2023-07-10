from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

def get_naver_cur():
    base_url = "https://m.stock.naver.com/marketindex/exchange/FX_JPYKRW"
    
    r = requests.get(base_url)
    
    soup = BeautifulSoup(r.text, "html.parser")

    item = soup.select_one('.DetailInfo_price__I_VJn')
    
    print(item)
    print(item.text)
    print(item.string)

    return item.text[0:6]

app = Flask(__name__)

@app.route('/currency',methods=['GET'])
def get_currency():    
    return get_naver_cur(),200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)