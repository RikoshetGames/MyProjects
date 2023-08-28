
from basic_word import *
import random
import requests
import urllib3


def load_random_word(url):
    """
    Получит список слов с внешнего ресурса,
    выберет случайное слово,
    создаст экземпляр класса `BasicWord`,
    вернет этот экземпляр.
    :param url: Адрес внешнего ресурса.
    :return: Экземпляр класса.
    """
    urllib3.disable_warnings() # Отключаем предупреждения о безопасности SSL-сертификата
    response = requests.get(url=url, verify=False) # Загружаем данные из внешнего ресурса
    random_words = response.json() # Преобразуем данные в формат JSON в список
    if response.status_code == 200:
        random_word = random.choice(random_words) # Выбираем случайное слово из списка
        instance = BasicWord(random_word["word"], random_word["subwords"]) # Создаем экземпляр класса BasicWord
        return instance
