from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """regex para case insensitive mongodb:
    https://stackoverflow.com/questions/4976278/python-mongodb-regex-ignore-case
    """
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    tuple_list = []
    for new in news:
        tuple_list.append((new["title"], new["url"]))
    return tuple_list


# Requisito 8
def search_by_date(date):
    """datetime.strptime para converter string em datetime:
    https://www.programiz.com/python-programming/datetime/strptime
    datetime.strftime para converter datetime em string:
    https://www.programiz.com/python-programming/datetime/strftime"""
    try:
        date_format = datetime.strptime(date, "%Y-%m-%d")
        new_date_format = date_format.strftime("%d/%m/%Y")
        news = search_news({"timestamp": {"$regex": new_date_format}})
        tuple_list = []
        for new in news:
            tuple_list.append((new["title"], new["url"]))
        return tuple_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
