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


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Name: {self.name}, price: {self.price}'


if __name__ == '__main__':
    try:
        print(ItemDiscountReport('Printer', 7002).get_parent_data())
    except Exception as err:
        print(err)