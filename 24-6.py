x =  int(input())
cnt = 0
while x > 0:
    cnt = cnt + x % 2
    x = x // 10
print(cnt)
