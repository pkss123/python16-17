# 난수 발생
# 난수란 무작위로 선택된 값을 난수라고 부릅니다
# 파이썬에서는 import random 이라고 최 상단에 적으면 난수를
# 발생시킬 수 있습니다
import random

# 정수 난수 : random.rmadint(시작값, 끝값)
# ex) random.randint(1, 100) 이라고 입력 시 1 ~ 100 범위의 숫자
# 하나를 무작위로 생성합니다
print(random.randint(1, 100))

# 실수 난수 : random.random()
# ex) random.random() 입력시 0이상 1 미만 실수 생성
print(random.random())

print(random.random()*100)
print(random.random() + random.randint(0, 99))
