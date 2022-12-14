
import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/-/en/Mirrorless-Digital-ILCE-7C-Real-Time-Stabilisation/dp/B08J41GC85/ref=sr_1_7?keywords=sony+a7&qid=1665994489&qu=eyJxc2MiOiI0Ljc5IiwicXNhIjoiNC43MiIsInFzcCI6IjQuNjAifQ%3D%3D&sr=8-7'

headers = {"User_Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

def check_price():

    page = requests.get(URL, headers= headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[0:10])

    if(converted_price < 1.840):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 1.840):
         send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('lordsking.mr@gmail.com', 'sgsiozwbaqnvrsgd')

    subject = 'price fell down now!'
    body = 'please check the amazon link https://www.amazon.de/-/en/Mirrorless-Digital-ILCE-7C-Real-Time-Stabilisation/dp/B08J41GC85/ref=sr_1_7?keywords=sony+a7&qid=1665994489&qu=eyJxc2MiOiI0Ljc5IiwicXNhIjoiNC43MiIsInFzcCI6IjQuNjAifQ%3D%3D&sr=8-7'

    msg =f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'lordsking.mr@gmail.com',
        'mrokniahmadi.mr@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()
    
while(True):
    check_price()
    time.sleep(60 * 60)
