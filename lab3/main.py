import pandas as pd 
from random import randint
from os import open



def table_creation():
    global NUMBER_OF_CUSTOMERS 
    global NUMBER_OF_PRODUCTS
    nuc = NUMBER_OF_CUSTOMERS = 51
    nup = NUMBER_OF_PRODUCTS = 21

    table = dict()
    table['-'] = [f'Customer {i}' for i in range(1, nuc)]

    for i in range(1, nup):
        table[f'Product {i}'] = [randint(0, 1) for i in range(1, nuc)]

    return table 

def support_def(table):

    table[list(table.keys())[0]].append('Support')
    
    for i in list(table.keys())[1::]:
        sup = sum(table[i])/100
        table[i].append(sup)
    
    return table 

def authencity_counting(table, *prods_nums):

    keys = list(table.keys())
    prods = [*prods_nums]
    list_of_products = [keys[i] for i in prods]
    support = table[list_of_products[0]][-1]

    combinations = 0

    for i in range(NUMBER_OF_PRODUCTS - 1):
        condition = 1
        for e in list_of_products:
            if table[e][i] == 0:
                condition == 0
                break
        combinations += 1
    
    authencity = combinations / support / 100

    return authencity

def lift_counting(authencity, support):
    return authencity / support

def main():
    data = table_creation()
    data = support_def(data)
    
    df = pd.DataFrame(data)

    fw = '//Users/gamzatshakhmanaev/Documents/Projects/SandBox/big data/lab3/table.xlsx'
    df.to_excel(fw)

    print(list(data.keys()))

    #output support, authencity and lift of any product pairs
    print('Product 1 and Product 2 support, authencity and lift')
    s = data['Product 1'][-1]
    a = authencity_counting(data, 1, 2)
    l = lift_counting(a, s)
    print(s, a, l)

    print('\n', 'Product 3, Product 4')
    s = data['Product 3'][-1]
    a = authencity_counting(data, 3, 4)
    l = lift_counting(a, s)
    print(s, a, l)

    print('\n', 'Product 5, Product 6')
    s = data['Product 5'][-1]
    a = authencity_counting(data, 5, 6)
    l = lift_counting(a, s)
    print(s, a, l)

    print('\n', 'Product 7, Product 8')
    s = data['Product 7'][-1]
    a = authencity_counting(data, 7, 8)
    l = lift_counting(a, s)
    print(s, a, l)



    #output support, authencity and lift of any product triples
    print('Product 9, Product 10, Product 11 support, authencity and lift')
    s = data['Product 9'][-1]
    a = authencity_counting(data, 9, 10, 11)
    l = lift_counting(a, s)
    print(s, a, l)
    print('')

    print('Product 12, Product 13, Product 14 support, authencity and lift')
    s = data['Product 12'][-1]
    a = authencity_counting(data, 12, 13, 14)
    l = lift_counting(a, s)
    print(s, a, l)
    print('')

    print('Product 15, Product 16, Product 17 support, authencity and lift')
    s = data['Product 15'][-1]
    a = authencity_counting(data, 15, 16, 17)
    l = lift_counting(a, s)
    print(s, a, l)
    print('')

    print('Product 18, Product 19, Product 20 support, authencity and lift')
    s = data['Product 18'][-1]
    a = authencity_counting(data, 18, 19, 20)
    l = lift_counting(a, s)
    print(s, a, l)
    print('')

    return 0 

if __name__ == '__main__':
    main() 
