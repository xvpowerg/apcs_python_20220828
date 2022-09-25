nums = [5, 2, 1, 9, 6]#小到大
print("sorted()函式排序之前:", nums)
print("sorted()函式傳回:", sorted(nums))
print("sorted()函式排序之後:", nums)

print("sort()方法排序之前:", nums)
print("sort()方法傳回:", nums.sort())
print("sort()方法排序之後:", nums)



cars = ['honda','BMW','Toyota','audi']

print("排序之前:", cars)
cars.sort()
print("排序之後:", cars)
cars.sort(reverse=True)
print("反向排序:", cars)
cars.sort(key=len)
print("長度排序:", cars)
cars.sort(key=lambda v: (v.upper(), v))
print("小寫排序:", cars)
