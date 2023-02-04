a = int(input('정수1를 입력하세요 :'))
b = int(input('정수2를 입력하세요 :'))

sum = 0

if a > b:
    a, b = b, a

for i in range(a, b+1):
    if i < b:
        print(f'{i}+', end='')
    sum += i
print(f'{i} = {sum}')