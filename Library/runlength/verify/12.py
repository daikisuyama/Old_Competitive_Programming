#愚直にシミュレートできないがそれぞれで戦う人がわかれば繰り返しをまとめて計算するだけ
#繰り返しで残りの余った部分はうまく処理する
n,k=map(int,input().split())
s=input()
#[[繰り返しの部分,繰り返しの回数],余りの部分]
t=[[s,(2**k)//n],s[:(2**k)%n]]
#k回の対戦を愚直に繰り返す
for i in range(k):
    #繰り返しの部分の長さを偶数にする操作
    #余った部分はそのまま"余りの部分"に追加する
    if len(t[0][0])%2==1:
        if t[0][1]%2==1:
            t[1]=t[0][0]+t[1]
            t[0][1]//=2
            t[0][0]=2*t[0][0]
        else:
            t[0][1]//=2
            t[0][0]=2*t[0][0]
    #繰り返しの部分でじゃんけんを行う(隣同士を見るだけ)
    l=len(t[0][0])
    nt=""
    for i in range(l//2):
        if t[0][0][2*i]=="R":
            if t[0][0][2*i+1]=="P":
                nt+="P"
            else:
                nt+="R"
        elif t[0][0][2*i]=="S":
            if t[0][0][2*i+1]=="R":
                nt+="R"
            else:
                nt+="S"
        else:
            if t[0][0][2*i+1]=="S":
                nt+="S"
            else:
                nt+="P"
    #繰り返しの部分の更新
    t[0][0]=nt
    #余りの部分でじゃんけんを行う
    l=len(t[1])
    nt=""
    for i in range(l//2):
        if t[1][2*i]=="R":
            if t[1][2*i+1]=="P":
                nt+="P"
            else:
                nt+="R"
        elif t[1][2*i]=="S":
            if t[1][2*i+1]=="R":
                nt+="R"
            else:
                nt+="S"
        else:
            if t[1][2*i+1]=="S":
                nt+="S"
            else:
                nt+="P"
    #余りの部分の更新
    t[1]=nt
if t[1]=="":
    print(t[0][0])
else:
    print(t[1])