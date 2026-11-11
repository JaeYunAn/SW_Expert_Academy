for t in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
 
    i = 1
    while True:
 
        if 0 in arr:
            break
 
        inque = arr[0]
        arr = arr[1:]
        c = inque-i
 
        if c > 0:
            arr.append(c)
        else:
            arr.append(0)
 
        i += 1
 
        if i > 5:
            i = 1
 
    print(f'#{tc}', *arr)