from statistics import mean
scores=[87,66,90,65,70]
score_sum=0
counts=len(scores)
score_max=0
score_min=100


score_sum = sum(scores)
score_avg = mean(scores)
score_max = max(scores)
score_min = min(scores)

'''
for i in range(counts):
    print(f"第{i+1}位學生的分數:{scores[i]}")
    score_sum += scores[i]
    if scores[i] > score_max:    
        score_max = scores[i]
    if scores[i] < score_min:
        score_min = scores[i]
'''            
print("================")
print("sum:",score_sum)
print(f"avg:{score_sum/counts:.2f}")
print("max:",score_max)
print("min:",score_min)

