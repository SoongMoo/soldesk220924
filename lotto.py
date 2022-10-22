import random
lotto = []
qty = int(input("원하는 수를 입력하세요. : "))
cnt = 1
while cnt <= qty:
    i = 1
    while i <= 45:
        lotto.append(i) 
        i+=1
    # print(lotto) # 1~45
    
    lottosize = len(lotto) # 45
    j = 1
    while j <= 6:
        lottosize -= 1
        idx = random.randint(0, lottosize) 
        # 0 ~ 44, 0 ~ 43, 0 ~ 42, 0 ~ 41, 0 ~ 40
        lottoNum = lotto.pop(idx)
        print(lottoNum, end =", ")
        j += 1
    cnt += 1
    lotto.clear()
    print()