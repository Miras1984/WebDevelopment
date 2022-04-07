v = int(input())
t = int(input())
if v < 0:
    if( - v * t  > 109):
        ans = -(109 - v * t) % 109
    else: ans = (109 - v * t) % 109
else:
    ans = (v * t) % 109
print(ans)