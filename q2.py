print('+와-를 번갈아 출력합니다.')
num = int(input('개수를 입력하세요:'))

for i in range(num):
    if i % 2 == 0:
        print(f'+', end='')
    else:
        print(f'-', end='')