def exclude_35(num):
    return int(num - num/3 - num/5 + 2*(num/15))

if __name__ == '__main__':
    num = input('num: ')
    print(exclude_35(int(num)))
