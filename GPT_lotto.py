from random import *

n = int(input("얼마치 복권을 구매하시겠습니까?(단위: KRW) "))

num = n // 1000
print(f"총 {num}개의 로또 번호를 출력합니다:\n")
for _ in range(num):
    lotto_num = []
    while len(lotto_num) != 6:
        rand_num = randint(1, 45)
        if rand_num not in lotto_num:
            lotto_num.append(rand_num)
    
    # 각 번호를 2자리로 맞춰 출력 (정렬 없이)
    formatted_numbers = " ".join(f"{num:2}" for num in lotto_num)
    print(formatted_numbers)