def getResult(score):
    if 60 <= score <=100:
        print("及格")
    elif 0<= score < 60:
        print("不及格")
    else:
        raise OverflowError("成績錯誤")
score = int(input("輸入成績:"))
try:
    getResult(score)
except OverflowError as e:
    print(e)
else:
    print("考試結果:",score)
