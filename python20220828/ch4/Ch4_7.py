a = 5
def func():
    #a = 10
    global a
    a +=  1
    print("f():",a)
print("全域:a=",a)
func()
print("全域:a=",a)
