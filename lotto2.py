import random

luckynumber = []
getnumber = []
count = 0
while(len(luckynumber) != 6):
    number = random.randint(1, 45)
    if number not in luckynumber:
        luckynumber.append(number)
luckynumber.sort()

while luckynumber != getnumber:
    getnumber = []
    count += 1
    while(len(getnumber) != 6):
        number = random.randint(1, 45)
        if number not in getnumber:
            getnumber.append(number)
    getnumber.sort()
print("로또복권을 %d장 사서 당첨되었습니다" % count)
print("로또복권을 %d원 어치 사서 당첨되었습니다" % (count*1000))
print("당첨번호는 :" , luckynumber, getnumber)