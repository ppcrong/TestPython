import multiprocessing as mp
import time


# https://www.maxlist.xyz/2020/03/15/python-threading/

def main(url, num):
    print('開始執行', url)
    time.sleep(2)
    print('結束', num)


url_list1 = ['11111, 1-1-1-1-1']
url_list2 = ['22222, 2-2-2-2-2']
url_list3 = ['33333, 3-3-3-3-3']

# 定義線程
p_list = []
p1 = mp.Process(target=main, args=(url_list1, 1))
p_list.append(p1)

p2 = mp.Process(target=main, args=(url_list2, 2))
p_list.append(p2)

p3 = mp.Process(target=main, args=(url_list3, 3))
p_list.append(p3)

# 開始工作
for p in p_list:
    p.start()

# 調整多程順序
for p in p_list:
    p.join()
