num = int(input('정수를 입력하세요:'))
count = 0

for i in range(2,num):
    for j in range(2, 6+1):
        if i**j == num:
            print(f'{i} ** {j} = {num} 입니다.')
            count = 1

if count == 0:
    print('결과가 없음')