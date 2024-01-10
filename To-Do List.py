def main():
    to_do_list = []
    userChoice = 0
    while userChoice != 4:
        userChoice = get_menu_choice()
        if userChoice == 1:
            show_list(to_do_list)
        elif userChoice == 2:
            add_item(to_do_list)
        elif userChoice == 3:
            delete_item(to_do_list)

def get_menu_choice():
    print("========== МЕНЮ ==========\n"
          "1. Показать список дел\n"
          "2. Внести новый пункт\n"
          "3. Пометить пункт как выполненный\n"
          "4. Выйти из приложения")
    print()
    userChoice = int(input("Выберите пункт: "))
    while userChoice < 1 or userChoice > 4:
        userChoice = int(input("Выберите пункт: "))
    return userChoice

def show_list(to_do_list):  # 1
    for i, item in enumerate(to_do_list, start=1):
        print(i, item)

def add_item(to_do_list): # 2
    new_item = input("Введите название пункта: ")
    if new_item not in to_do_list:
        to_do_list.append(new_item)
        print("Пункт добавлен!\n")
        return to_do_list
    else:
        print("Такой пункт уже существует\n")
        return to_do_list

def delete_item(to_do_list): # 3
    item = str(input("Введите название пункта: "))
    if item in to_do_list:
        to_do_list.remove(item)
        print("Пункт помечен как выполненный\n")
        return to_do_list
    else:
        print("Пункт не найден\n")
        return to_do_list

if __name__ == '__main__':
    main()