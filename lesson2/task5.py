
class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, dis):
        super().__init__(name, price)
        self.__dis = dis


    @property
    def discount(self):
        return self.__dis


    def __str__(self):
        return f'price: {self.price * (1 - self.__dis / 100)}'

    def get_parent_data(self):
        return f'Name: {self.name}, price: {self.price}'


if __name__ == '__main__':
    pr = ItemDiscountReport('Printer', 7002,13)
    try:
        print(pr.get_parent_data())
        pr.price = 33333
        print(pr.get_parent_data())
        print(pr)
    except Exception as err:
        print(err)
