a,b,i,hap=0,0,0,0
a=int(input("시작값을 입력하세요: "))
b=int(input("끝값을 입력하세요: "))

for i in range (a,b+1,1):
    if (i%2==1):
        hap=hap+i

print("%d과 %d 사이에 있는 홀수의 합계: %d" % (a,b,hap))
