results = {"David":0,"Amy":0,"Sean":0}
c = ("David","Amy","Sean")
for i in range(5):
    vote = input("投票給:")
    if vote not in c:
        print("無效")
        continue
    results[vote] += 1
print("結果:")
for name in c:
    print(name,results[name],"票")
