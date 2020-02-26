if __name__ == "__main__":
    out_put = "Hey Python ! Nice to meet you"
    print(out_put)
print(2 + 2)
print(50 - 6)
print(7 * 7)
print(8 / 2)
print(type(2 + 2))
print(type(50 - 6))
print(type(7 * 7))
print(type(8 / 2))
print(100 / 7)
print(100 // 7)
text = '今天天氣真好呢，真想出去玩。'
print(type(text))
print(text)
text_1 = '今天天氣真好呢，'
text_2 = '真想出去玩。'
print(text_1 + text_2)
print(text_1 * 3)
print(text[0])
print(text[1])
print(text[2])
print(text[:])
for n in range(10):
    print(n)
for n in range(1, 10):
    if n % 3 == 0:
        print(n, '被3整除')
    elif n % 3 == 1:
        print(n, '被3除後餘1')
    else:
        print(n, '被3除後餘2')
# 這是 pass 的迴圈
times = 0
for n in range(10):
    if n == 4:
        pass
    else:
        print(n)

    times += 1
    print('這是本程式執行第%d次' % times)
# 這是 continue 的迴圈
times = 0
for n in range(10):
    if n == 4:
        continue
    else:
        print(n)

    times += 1
    print('這是本程式執行第%d次' % times)


def fibo(n):
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    return fibo(n - 1) + fibo(n - 2)


for num in range(10):
    ans = fibo(num)
    print("fibo({}) = {}".format(num, ans))


def test(n, a=1, b=2):
    print(n + a + b)


test(1, 2, 3)
test(1)


def test1(n, *args):
    a = n
    for arg in args:
        a += arg

    print(a)


test1(1, 2, 3, 4, 5, 6)


def test2(n, **kwargs):
    print(n)
    for a, b in kwargs.items():
        print(a, b)


test2(1, key=3, value=9)

determine = lambda n1: print('%s 大於 50' % n1) if n1 >= 50 else print('%s 小於 50' % n1)

determine(99)
determine(1)

sum = lambda x, y: x + y
sum(1, 2)

data = (1, 2, 3, '今天', '天氣', '真好')

List = []
for value in data:
    List.append(value)
print(List)
print(List.index(2))
print(List.index(3))
print(List[2])
print(List[5])
List.insert(0, 100)
print(List)
List.insert(10000, 100)
print(List)

a = [n for n in data]
b = list(data)  # not recommend
print(a)
print(b)
