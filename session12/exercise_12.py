# ex-02
def try_append():
    list_1 = ['old']
    list_1.append('new')
    return list_1

def try_extend():
    list_2 = ['old']
    list_2.extend('new')
    return list_2

def try_sort():
    list_3 = ['old', 'middle', 'new']
    list_3.sort()
    return list_3


def main():
    print(try_append())
    print(try_extend())
    print(try_sort())
    

if __name__ == '__main__':
    main()