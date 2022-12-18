num = int(input())
player_list = []
count = 0

for i in range(num):
    p = input()
    player_list.append(p[0])

first = list(set(player_list))
first.sort()

for i in first :
    if player_list.count(i) >= 5 :
        print(i,end='')
        count += 1
    else :
        continue

if count == 0 :
    print("PREDAJA")
