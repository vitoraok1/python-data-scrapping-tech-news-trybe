from tech_news.database import search_news


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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
