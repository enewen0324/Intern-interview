def reverse(str):
    return str[::-1]
def reverse_split(str):
    s_split =  str.split(' ')
    str = ""
    for i in s_split:
        str+=i[::-1]
        str+=" "
    str=str[:len(str)-1]
    return str

if __name__ == '__main__':
    str = input('input: ')
    print(reverse(str))
    print(reverse_split(str))
    