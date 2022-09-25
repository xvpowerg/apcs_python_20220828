def func(thelist):
    print("func():",id(thelist),thelist)
    thelist[2] = 'Hi'
    print("func():",id(thelist),thelist)

myList = [10,20,30]

print("全域:",id(myList),myList)
func(myList)
print("全域:",id(myList),myList)
