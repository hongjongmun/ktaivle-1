# 수도 회사 선택 후 수도 사용량의 요금 출력

def waterPay(company, usage):
    if company == 'A':
        charge = 100*usage
        return company, charge
    elif company == 'B':
        if usage <= 50:
            charge = 150*usage
            return company, charge
        else :
            charge = 50*150 + (usage-50)*75
            return company, charge
        
company = input('회사를 입력하세요:')
usage = int(input('수도 사용량을 입력하세요:'))

answer = waterPay(company, usage)
print(f'{answer[0]}회사의 수도요금은 {answer[1]}원 입니다.')