import threading
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
t_list = []

t1 = threading.Thread(target=main, args=(url_list1, 1))
t_list.append(t1)
t2 = threading.Thread(target=main, args=(url_list2, 2))
t_list.append(t2)
t3 = threading.Thread(target=main, args=(url_list3, 3))
t_list.append(t3)

# 開始工作
for t in t_list:
    t.start()

# 調整多程順序
for t in t_list:
    t.join()
