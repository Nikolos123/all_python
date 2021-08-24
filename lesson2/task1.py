class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Name: {self.name}, price: {self.price}'


if __name__ == '__main__':
    print(ItemDiscountReport('Printer', 7002).get_parent_data())