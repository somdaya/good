from itertools import permutations
time = list(permutations(map(int,input().split(":"))))
count = 0

for h, m ,s in time :
    if 1<=h<=12 and 0<=m<=59 and 0<=s<=59 :
        count += 1

print(count)

# 한세트씩 시/분/초 될수있는 경우의수 생각
# but, 숫자가 같을경우 힘듦.

# 경우의수 3*2*1 이런식으로 할 수 있지만
# 시에서 24넘을경우?

# for i in time :
#     if 1 <= i <= 12 : # 시, 분, 초 가능
#         count += 3
    
#     elif 0 == i or 13 <= i <= 59 :
#         count += 2

# if len(jungbok) == 2 :
#     if jungbok[0] == 0 and 1<= jungbok[1]<=12:
#         count -
    