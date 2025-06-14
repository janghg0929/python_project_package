class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

Item1 = MenuItem("아메리카노", 3000)
Item2 = MenuItem("라떼", 4000)
Item3 = MenuItem("케이크", 5000)

orderitem = []
orderprice = []
totalprice = []

class Order:
    def __init__(self, items):
        self.items = items
        Order.add_item(self.items)

    def add_item(menu_item):
        if menu_item.name == Item1.name:
            if orderitem.count(Item1.name) < 1:
                orderitem.append(menu_item.name)
        elif menu_item.name == Item2.name:
            if orderitem.count(Item2.name) < 1:
                orderitem.append(menu_item.name)
        elif menu_item.name == Item3.name:
            if orderitem.count(Item3.name) < 1:
                orderitem.append(menu_item.name)
        orderprice.append(menu_item.name)
        totalprice.append(menu_item.price)

    def total_price():
        print(f"총 결제 금액: {sum(totalprice)}원")

    def show_order():
        print("\n=== 주문 내역 ===")
        for i in range(len(orderitem)):
            print(f"{orderitem[i]} - {orderprice.count(orderitem[i]) * Item1.price}원" if orderitem[i] == Item1.name else f"{orderitem[i]} - {orderprice.count(orderitem[i]) * Item2.price}원" if orderitem[i] == Item2.name else f"{orderitem[i]} - {orderprice.count(orderitem[i]) * Item3.price}원")
        Order.total_price()

class main:
    def main():

        print("===== 메뉴 =====")
        print(f"1. {Item1.name} - {Item1.price}원")
        print(f"2. {Item2.name} - {Item2.price}원")
        print(f"3. {Item3.name} - {Item3.price}원")
        print("0. 주문 완료")
        print("=================")

        while True:
            jumun = int(input("메뉴 선택: "))
            if jumun == 1:
                Order(Item1)
                print(f"{Item1.name} 추가되었습니다.")
            elif jumun == 2:
                Order(Item2)
                print(f"{Item2.name} 추가되었습니다.")
            elif jumun == 3:
                Order(Item3)
                print(f"{Item3.name} 추가되었습니다.")
            elif jumun == 0:
                Order.show_order()
                return

main.main()