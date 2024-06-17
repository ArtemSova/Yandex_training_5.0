from G_Разрушить_казарму import func

def main():
    test_1()
    test_2()
    test_3()
    print('COMPLITE')

def test_1():
    assert func(1, 1, 1) == 1
    assert func(10, 11, 15) == 4
    assert func(5, 8, 5) == 4
    assert func(2, 3, 2) == 3
    assert func(25, 200, 10) == 13
    assert func(8, 12, 7) == 3
    assert func(31, 495, 15) == 30
    assert func(78, 4934, 77) == 4812
    assert func(78, 126, 77) == 5
    assert func(14, 471, 9) == 92

def test_2():
    assert func(300, 301, 484) == 6
    assert func(250, 500, 230) == 8
    assert func(250, 500, 187) == 4
    assert func(250, 500, 208) == 5
    assert func(250, 500, 209) == 6
    assert func(250, 500, 218) == 6
    assert func(250, 500, 240) == 13
    assert func(250, 500, 249) == 101
    assert func(1092, 2892, 950) == 11
    assert func(1661, 4327, 1107) == 6
    assert func(2500, 5000, 2420) == 16
    assert func(2500, 5000, 2499) == 961
    assert func(3000, 5000, 2998) == 79

def test_3():
    assert func(1, 2, 1) == -1
    assert func(300, 301, 485) == -1
    pass

if __name__ == "__main__":
    main()
