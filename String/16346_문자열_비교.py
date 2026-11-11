'''
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''

'''
#1 1
#2 0
#3 1
'''

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)
    
    answer = 0

    
    for i in range(M - N + 1):
       
        for j in range(N):
            
            if str2[i + j] != str1[j]:
               
                break
     
        else:
            
            answer = 1

    print(f"#{tc} {answer}")