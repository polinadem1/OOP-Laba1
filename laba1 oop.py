import requests
import webbrowser
import json  

def wikipedia_search():
    query = input("Введите поисковый запрос для Википедии: ")
    try:
        
        url = f"https://ru.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch={requests.utils.quote(query)}"
        response = requests.get(url)
        response.raise_for_status()

        
        data = json.loads(response.text)  
        search_results = data.get("query", {}).get("search", [])
        
        if not search_results:
            print("По вашему запросу ничего не найдено.")
            return

        
        print("Результаты поиска:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result['title']}")

        
        choice = int(input("Введите номер статьи для открытия: ")) - 1
        if choice < 0 or choice >= len(search_results):
            print("Некорректный выбор.")
            return

        
        page_id = search_results[choice]['pageid']
        article_url = f"https://ru.wikipedia.org/w/index.php?curid={page_id}"
        webbrowser.open(article_url)
        print(f"Открыта статья: {article_url}")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    while True:
        print("Выберите действие:\n1. Поиск в Википедии\n0. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            wikipedia_search()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()