score=int(input("점수를 입력하세요: "))
if score >= 95:
    print("A+")
elif score >= 90:
    print("A0")
elif score >= 85:
    print("B+")
elif score >= 80 and score<85:
    print("B0")
elif score >= 75 and score<80:
    print("C+")
elif score >=70 and score<75:
    print("C0")
elif score >= 65 and score<70:
    print("D+")
elif score >= 60 and score<75:
    print("D0")
elif score <60:
    print("F")
print("학점입니다. ")


