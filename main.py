import requests
from bs4 import BeautifulSoup

bad_words = ["блядь", "хуй", "пизда"]
pohabshina = requests.get("http://www.ermak.su/context/afor_posl_zag/poslov_p.htm").text
# print(pohabshina)
soup = BeautifulSoup(pohabshina, 'lxml')
text_pohabshina = soup.get_text()

text_pohabshina = text_pohabshina.replace("\n", " ").replace("\t", " ").replace("\r", " ").replace("\xa0", " ")\
    .replace("!", ".").replace("...", ".").split(".")

for trigger in bad_words:
    for sentence in text_pohabshina:
        if trigger in sentence:
            print(sentence)
            print('========================================')
# Оператор in в Python используется для проверки наличия элемента в последовательности или наличия подстроки в строке.