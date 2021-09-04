
def func(number):
    if not number % 1:
        print('Received number is integer.')
    else:
        print('Received number is fractional.')
        whole, frac = str(number).split('.')
        return True if whole == frac else False


if __name__ == '__main__':
    float_false = 5.86
    float_true = 52.52
    num = 5

    print(func(float_false))
    print(func(float_true))
    print(func(num))