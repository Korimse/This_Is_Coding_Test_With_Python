direction = input()
r = int(direction[1])
c = int(ord(direction[0]))-int(ord('a')) + 1

knight = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0
for k in knight:
    nr = r + k[0]
    nc = c + k[1]
    if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8:
        result += 1
print(result)