from sys import stdin

T = int(stdin.readline().strip())

for i in range(T):
    Input = list(stdin.readline().split())

    R = int(Input[0])
    S = Input[1] 

    word_list = []
    for word in S:
        for count in range(R):
            word_list.append(word)
    
    print("".join(word_list))