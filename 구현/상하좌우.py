n = int(input())

move = list(input().split())

direction = ['U', 'D', 'L', 'R']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x = 1
y = 1

for m in move:
    for i in range(len(direction)):
        if m == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    else:
        x = nx
        y = ny
print(x, y)