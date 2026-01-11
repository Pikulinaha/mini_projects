class ShopList:
    def __init__(self):
        self.items=[]

    def add_items(self,item_name,price,quantity=1):
        """Добавление товара в список покупок"""
        item={
            "name": item_name,
            "quantity": quantity,
            "price":price,
            "bought": False
        }
        self.items.append(item)
        if price:
            total_price=quantity*price
            print(f"✅ {item_name}: {quantity} * {price}")
        else:
            print(f"✅ Добавлено {item} ({quantity}) шт.")

    def math(self):
        """Общая сумма всех товаров"""
        total=0
        for item in self.items:
            if item["price"] and not item["bought"]:
                total+=item["quantity"]*item["price"]
        return total


    def show(self):
        """Просмотр списка с выводом сколько к оплате и количество товаров"""
        if not self.items:
            print("Список пуст")
            return
        print("Ваш список: ")
        total=0
        for i,item in enumerate(self.items,1):
            print(f"{i}. {item['name']} {item['price']}")
            total+=item['price']*item['quantity']
        print(f"Всего к оплате: {total}₽")
        print(f"Всего товаров: {len(self.items)}")

    def start(self):
        """Меню"""
        while True:
            print("\n--- МЕНЮ ---")
            print("1. Посмотреть список")
            print("2. Добавить товар")
            print("3. Выйти")

            choice = input("Ваш выбор: ")

            if choice == "1":
                self.show()
            elif choice == "2":
                name = input("Название товара: ")
                price = float(input("Цена: "))
                quantity = int(input("Количество: "))
                self.add_items(name, price, quantity)
            elif choice == "3":
                print("Пока!")
                break
if __name__ == "__main__":
    my_list = ShopList()
    my_list.start()