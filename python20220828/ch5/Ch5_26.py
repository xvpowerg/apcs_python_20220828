class student:
    school="NCKU"
    count=0
    def __init__(self, name):
        self.name = name
        student.count += 1
    def displayCount(self):
        print("Total  %d" % student.count)
    def displaystudent(self):
        print("Name : ", self.yourname)
st1 = student("MAX")
#st1.age=18
if hasattr(st1, 'age'):
    print("欄位存在,要刪除")
    delattr(st1, 'age')
    print("存在:"+str(st1.age))
else:
    print("欄位不存在")
    setattr(st1, 'age', 20)
    print("建立:" + str(st1.age))
