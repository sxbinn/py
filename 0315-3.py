id=input("아이디를 입력하세요: ")

if id=="admin":
    print("모든 콘텐츠 이용 가능")
else:
    lv=int(input("회원 레벨을 입력하세요: "))
    if lv >=2 and lv <= 7:
        print("일부 콘텐츠 이용 가능")
    else :
        print("콘텐츠 이용 불가")
