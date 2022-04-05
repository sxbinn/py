E=int(input("영어 점수를 입력하세요: "))
M=int(input("수학 점수를 입력하세요: "))

if E >=80 and M>=80:
    print("합격")
elif E<80 and M<80:
    print("불합격")
else:
    print("재시험 기회제공")
