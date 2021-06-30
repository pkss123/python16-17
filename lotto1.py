import random

getnumber = []
while(len(getnumber) != 6):
    number = random.randint(1, 45)
    if number not in getnumber:
        getnumber.append(number)
getnumber.sort()
print(getnumber)
secondnum = number
while(secondnum in getnumber):
    secondnum = random.randint(1,45)
print("2등 당첨번호는 %d 입니다" % secondnum)
