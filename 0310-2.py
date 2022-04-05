money=int(input("교환할 돈(원)을 입력하시오:  "))

c50000=money//50000
money%=50000

c10000=money//10000
money%=10000

c5000=money//5000
money%=5000

c1000=money//1000
money%=1000

c500=money//500
money%=500

c100=money//100
money%=100

c50=money//50
money%=50

c10=money//10
money%=10


print("\n 50000원 %d개" % c50000)
print("10000원 %d개" % c1000)
print("5000원 %d개" % c5000)
print("1000원 %d개" % c1000)
print("500원 %d개" % c500)
print("50원 %d개" % c50)
print("10원 %d개" % c10)
print("\n 바꾸지 못한 돈 => %d원" % money)

