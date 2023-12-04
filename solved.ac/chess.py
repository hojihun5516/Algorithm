def can_move(x,y):
    return 0<x<=8 and 0<y<=8
    
king, stone, N = input().split()
K = list(map(int, [ord(king[0])-64, king[1]]))
S = list(map(int, [ord(stone[0])-64, stone[1]]))
moving = {"R":[1,0],"B":[0,-1],"L":[-1,0],"T":[0,1],"RT":[1,1],"RB":[1,-1],"LB":[-1,-1],"LT":[-1,1]}

for i in range(int(N)):
    m = input()
    nkx = moving[m][0] + K[0]
    nky = moving[m][1] + K[1]

    if can_move(nkx,nky):
        if nkx==S[0] and nky==S[1]:
            nsx = S[0] + moving[m][0]
            nsy = S[1] + moving[m][1]
            if can_move(nsx, nsy):
                S = [nsx,nsy]
                K = [nkx,nky]
        else:
            K = [nkx,nky]

print(f'{chr(K[0]+64)}{K[1]}')
print(f'{chr(S[0]+64)}{S[1]}')

https://www.acmicpc.net/problem/1063