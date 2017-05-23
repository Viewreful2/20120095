t = int(input())
arr = [ [ 0 for j in range(5) ] for i in range(5) ]
for text_case in range(t) :
    for i in range(5) :
        arr[i] = list(map(int, input().split()))
    num = list(map(int, input().split()))
    for k in range(len(num)) :
        flag = False
        for i in range(5) :
            for j in range(5) :
                if(arr[i][j] == num[k]) :
                    arr[i][j] = 0
                    flag = True
                    break
            if(flag == True) :
                break
        if(flag == True ) :
            if(arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3] + arr[4][4] == 0 ) : # 오른쪽 아래 대각선
                print(k+1)
                break
            if(arr[0][4] + arr[1][3] + arr[2][2] + arr[3][1] + arr[4][0] == 0 ) : # 왼쪽 아래 대각선
                print(k+1)
                break
            if(arr[0][0] + arr[0][4] + arr[4][0] + arr[4][4] == 0 ) : # 네개의 모서리
                print(k+1)
                break
            flag = False
            for i in range(5) :
                if(arr[i][0] + arr[i][1] + arr[i][2] + arr[i][3] + arr[i][4] == 0 ) :
                    print(k+1)
                    flag = True
                    break
                if(arr[0][i] + arr[1][i] + arr[2][i] + arr[3][i] + arr[4][i] == 0 ) :
                    print(k+1)
                    flag = True
                    break
            if(flag == True) : 
                break