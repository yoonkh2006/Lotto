from random import *

n = int(input("얼마치 복권을 구매하시겠습니까?(단위: KRW) "))

num = n // 1000
for i in range(num):
  lotto_num = []
  while len(lotto_num) != 6 :
    n = randint(1, 45)
    if n not in lotto_num :
      lotto_num.append(n)
  print(lotto_num)