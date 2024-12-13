from wikipedia_search import wikipedia_search

def show_menu():
    """Отображает главное меню приложения."""
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
