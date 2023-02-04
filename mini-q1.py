## 네 정수 입력받고 최댓값 구하기

list_num = list(map(int, input('네 정수를 입력하세요 :').split()))
num1 = list_num[0]   

for i in range(1, len(list_num)):
    if num1 < list_num[i]:
        num1 = list_num[i]
        
print(f'최댓값은 {num1} 입니다.')
