import requests
import webbrowser
import json

def wikipedia_search():
    """Выполняет поиск по Википедии и открывает выбранную статью в браузере."""
    query = input("Введите поисковый запрос для Википедии: ")
    try:
        # Формируем URL для API-запроса
        url = f"https://ru.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch={requests.utils.quote(query)}"
        response = requests.get(url)
        response.raise_for_status()

        # Обрабатываем данные ответа
        data = json.loads(response.text)
        search_results = data.get("query", {}).get("search", [])
        
        if not search_results:
            print("По вашему запросу ничего не найдено.")
            return

        # Выводим результаты поиска
        print("Результаты поиска:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result['title']}")

        # Пользователь выбирает статью
        choice = int(input("Введите номер статьи для открытия: ")) - 1
        if choice < 0 or choice >= len(search_results):
            print("Некорректный выбор.")
            return

        # Открываем выбранную статью в браузере
        page_id = search_results[choice]['pageid']
        article_url = f"https://ru.wikipedia.org/w/index.php?curid={page_id}"
        webbrowser.open(article_url)
        print(f"Открыта статья: {article_url}")
    except Exception as e:
        print(f"Ошибка: {e}")
