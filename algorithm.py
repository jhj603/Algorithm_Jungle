A = int(input())

if (((0 == A % 4) and (0 != A % 100)) or (0 == A % 400)):
    print(1)
else:
    print(0)
