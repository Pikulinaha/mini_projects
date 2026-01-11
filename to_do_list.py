class List:
    def __init__(self):
        self.put=[]


    def addvent(self):
        """Добавление дела"""
        put=input("\nВведите действие,которое хотите выполнить: ")
        self.put.append(put)
        print("\nДело Добавлено")

    def deleted(self):
        """"Удалить последние действие"""
        if self.put:
            mus=self.put.pop()
            print("Действие удалено")
        else:
            print("Список пуст")



    def seek(self):
        """Показ списка"""
        if self.put:
            print("Список ваших дел")
            for i,put in enumerate(self.put,1):
                print(f"{i}-{put}")

    def show_menu(self):
        """Показ действий"""
        print("Добро пожаловать в To-Do-List\n")
        print("Выберите действие: ")
        print("1.Добавить дело")
        print("2.Удалить дело")
        print("3.Просмотр списка")
        print("4.Выход")

    def run(self):
        """Основной цикл"""
        while True:
            self.show_menu()
            choice=input("\nВыберите действие 1-4: ")

            if choice=="1":
                self.addvent()
            elif choice=="2":
                self.deleted()
            elif choice == "3":
                self.seek()
            elif choice == "4":
                print("Спасибо за использование, до свидания!")
                break
            else:
                print("Недопустимое значение")
todo=List()
todo.run()