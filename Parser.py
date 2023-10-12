from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://omsk.shop.megafon.ru/mobile/apple'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.findAll('span', class_='b-price-good-list__actual b-price-good-list__actual_one b-price__actual')
    prices = []
    for data in block:
        if data.find('span', class_="b-price-good-list__value b-price__value"):
            price = float(data.text.strip().replace("\n", "").replace("Рублей", "").replace(" ", ""))
            prices.append(price)
    avg_price = sum(prices) / len(prices)
    min_price = min(prices)
    max_price = max(prices)
    print("Список всех цен: ")
    print(*prices, sep = ' рублей, ')
    print(f"Средняя цена: {avg_price:.2f} рублей")
    print(f"Минимальная цена: {min_price:.2f} рублей")
    print(f"Максимальная цена: {max_price:.2f} рублей")