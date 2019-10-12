#author: @jessemagni
#Amazon product web scraper

#imports
import requests
from bs4 import BeautifulSoup 
import smtplib

#Url of Website that I want to scrape
URL = "https://www.amazon.com/M-Audio-Keystation-Ultra-Portable-Keyboard-Controller/dp/B07GBNNF23?pf_rd_p=3d4da154-e8dd-4581-b2f1-5a1224d0157e&pd_rd_wg=rI4kg&pf_rd_r=S8XR7M07M7DDBZDWFFAM&ref_=pd_gw_cr_simh&pd_rd_w=mk0WU&pd_rd_r=e1b2f588-7596-4e3c-ab3b-797a4abda10a"

#The User Agent, search "my user agent" to get yours
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.56078'}

def check_price():

    #loading the page so that bs can read it properly
    page = requests.get(URL, headers=headers)

    #the scraper
    soup = BeautifulSoup(page.content, 'html.parser')

    #to make the scraper work
    soup1 = BeautifulSoup(soup.prettify(), "html.parser")

    #title of product
    title = soup1.find(id="productTitle").get_text()

    price = soup1.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:4])

    if converted_price > 50:
        send_mail()

    

    print(title.strip())
    print(converted_price)

def send_mail():
    
    server = smtplib.SMTP(host='smtplib.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('magnijesse@gmail.com', 'wfvfqddwvwauaocf')

    subject = "Price got lower!"
    body = "Check link: https://www.amazon.com/M-Audio-Keystation-Ultra-Portable-Keyboard-Controller/dp/B07GBNNF23?pf_rd_p=3d4da154-e8dd-4581-b2f1-5a1224d0157e&pd_rd_wg=rI4kg&pf_rd_r=S8XR7M07M7DDBZDWFFAM&ref_=pd_gw_cr_simh&pd_rd_w=mk0WU&pd_rd_r=e1b2f588-7596-4e3c-ab3b-797a4abda10a"

    msg = f'Subject:{subject}\n\n{body}'

    server.sendmail(
        'magnijesse@gmail.com',
        'magnijesse@yahoo.com',
        msg
    )

    print("EMAIL SENT!")
    server.quit()

check_price()

