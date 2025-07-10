Add = [ [-1, 0], [1, 0], [0, -1], [0, 1] ] 

N = int(input())

Count = 1
Max = 0
Min = 101

Array = []
Visit = [[0 for _ in range(N)] for _ in range(N)]
que = []

for i in range(N):
    temp = []
    Input = input().split()

    for j in range(N):
        temp.append(int(Input[j]))

        Max = max(Max, int(Input[j]))
        Min = min(Min, int(Input[j]))

    Array.append(temp)

for i in range(Min, Max):
    Visit = [[0 for _ in range(N)] for _ in range(N)]

    tempCount = 0

    for j in range(N):
        for k in range(N):
            if ((False == Visit[j][k]) and (i < Array[j][k])):
                tempCount += 1
                que.clear()
                Visit[j][k] = True
                que.append([j, k])

                while (0 < len(que)):
                    x = que[0][0]
                    y = que[0][1]

                    que.pop(0)

                    for add in Add:
                        tempx = x + add[0]
                        tempy = y + add[1]

                        if ((0 <= tempx) and (0 <= tempy) and (N > tempx) and (N > tempy) and (False == Visit[tempx][tempy]) and (i < Array[tempx][tempy])):
                            Visit[tempx][tempy] = True
                            que.append([tempx, tempy])

    Count = max(Count, tempCount)

print(Count)