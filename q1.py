def electricPay(usage):
    if usage < 100:
        Pay = 410 + usage*60.7
    elif usage >= 100 and usage <= 200:
        Pay = 910 + 100*usage + (usage-100)*125.9
    else :
        Pay = 1600 + 100*60.7 + 100*125.9 + (usage-200)*187.9
    
    result = int(Pay + Pay*0.1 + Pay*0.037)
    return result
    
usage = int(input('전기사용량을 입력하세요(kWh):'))
answer = electricPay(usage)
print(f'요금은 {answer}원 입니다')