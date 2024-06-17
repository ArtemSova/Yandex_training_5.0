from F_Миша_и_математика import func

def main():
    test_1()
    test_2()
    test_3()
    print('COMPLITE')


def test_1():
    assert func(3, [5, 7, 2]) == 'x+'
    assert func(2, [4, -5]) == '+' 


def test_2():
    assert func(6, [1, 1, 2, 2, 1, 1]) == '++++x'
    assert func(6, [3, 3, 2, 2, 3, 3]) == '++++x'
    assert func(6, [2, 2, 1, 1, 2, 2]) == '++x++'
    assert func(6, [1, 2, 1, 2, 1, 2]) == '+++++'
    assert func(7, [1, 2, 1, 2, 1, 2, 1]) == '+++++x'
#    assert func(3, [1, 1, 1]) == 'xx'
    assert func(5, [3, 2, 2, 3, 3]) == '++++'
    assert func(6, [1, 2, 2, 1, 2, 2]) == '++x++'

def test_3():
    assert func(4, [-432300451, 509430974, -600857889, -140418957]) == '+++'
    assert func(10, [-196228170, -181402541, 328251237, 624722764, 682518931, 783857631, 969228879, 547715844, -149364638, 823684584]) == '+++++++++'


    
if __name__ == '__main__':
    main()



    
