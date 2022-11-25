n = int(input())
vote = []
count = 0

for i in range(n) :
    a = int(input())
    vote.append(a)

ex1 = vote.copy()

vote.reverse()

# index 1이 최대값이 될때까지 더 많은것에서 하나씩 빼옴

big = vote.index(max(vote))

while True :
    if big == (n-1) and vote[-1] == max(vote): 
        # VOTE의 최댓값 위치가 1번후보이고, 1번후보의 투표수가 
        break

    vote[big] -= 1 # 
    vote[-1] += 1
    count += 1
    big = vote.index(max(vote))

print(count)