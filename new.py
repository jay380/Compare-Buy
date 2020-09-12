import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.3'}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index1.html")

@app.route('/', methods=['POST'])
def amazon():
    url = 'https://www.amazon.in/s?k=asus&rh=n%3A1375424031&ref=nb_sb_noss'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('.a-color-base.a-text-normal')
    prices = soup.find_all(class_='a-price-whole')
    list1 = []
    list2 = []
    text = request.form.get('search_bar')
    for title in titles:
        list1.append(title.get_text())
    for price in prices:
        list2.append(price.text)
    return render_template("index.html", text=text, list1=list1, list2=list2)

app.run()