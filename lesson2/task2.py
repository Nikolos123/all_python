class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Name: {self.__name}, price: {self.__price}'


if __name__ == '__main__':
    try:
        print(ItemDiscountReport('Printer', 7002).get_parent_data())
    except Exception as err:
        print(err)