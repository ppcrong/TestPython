import os

try:
    os.mkdir('./os_practice')
except:
    print("mkdir except!!!")

# os.rmdir('./os_practice')
print(os.listdir('./os_practice/'))
text_list = os.listdir('./os_practice/')
for text in text_list:
    if text.endswith('.txt'):
        print('%s:' % text, open('os_practice/%s' % text, 'r', encoding='utf-8').read())

newContent = '你確定今天天氣真的好嗎？'

open('os_practice/text01.txt', 'w', encoding='utf-8').write(newContent)

print('text01.txt:', open('os_practice/text01.txt', 'r', encoding='utf-8').read())

newContent = '真的假的啊喂。'

open('os_practice/text02.txt', 'a', encoding='utf-8').write(newContent)

print('text02.txt:', open('os_practice/text02.txt', 'r', encoding='utf-8').read())