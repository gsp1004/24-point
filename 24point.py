import os


all_opr = []
all_res = set()
def opr(num,ret):
    global all_opr
    if num > 2:
        for i in range(6):
            my_ret = ret.copy()
            my_ret.append(i)
            opr(num-1,my_ret)
    elif num == 2:
        for i in range(6):
            temp = ret.copy()
            temp.append(i)
            all_opr.append(temp)
    else:
        print("num should great than 1")
        return -1

def calc(num,opr):
    res = 0
    for i in range(len(opr)):
        if i == 0:
            res = num[i]
            
        if opr[i] == 0:
            res = res + num[i+1]
        elif opr[i] == 1:
            res = res - num[i+1]
        elif opr[i] == 2:
            res = res * num[i+1]
        elif opr[i] == 3:
            if num[i+1] == 0:  # 除数为0，非法，所以不行
                return -1
            else:
                res /= num[i+1]
        elif opr[i] == 4:
            res = num[i+1] - res
        elif opr[i] == 5:
            if res == 0:  # 除数为0，非法，所以不行
                return -1
            else:
                res = num[i+1] / res
    if res == 24:
        return 0
    else:
        return -1
        

def trans(num,opr):
    res = ""
    for i in range(len(opr)):
        if i == 0:
            res = str(num[i])
            
        if opr[i] == 0:
            res = res + "+" + str(num[i+1])
        elif opr[i] == 1:
            res = res + "-" + str(num[i+1])
        elif opr[i] == 2:
            if i != 0 and (opr[i-1] == 0 or opr[i-1] == 1 or opr[i-1] == 4):
                res = "(" + res + ")"
            res = res + "*" + str(num[i+1])
        elif opr[i] == 3:
            if i != 0 and (opr[i-1] == 0 or opr[i-1] == 1 or opr[i-1] == 4):
                res = "(" + res + ")"
            res = res + "/" + str(num[i+1])
        elif opr[i] == 4:
            if i != 0 and (opr[i-1] == 0 or opr[i-1] == 1 or opr[i-1] == 4):
                res = "(" + res + ")"
            res = str(num[i+1]) + "-" + res
        elif opr[i] == 5:
            if i != 0:
                res = "(" + res + ")"
            res = str(num[i+1]) + "/" + res

    return res


def arrange_num(rest,ordered):
    global all_opr
    global all_res
    for i in range(len(rest)):
        my_ordered = ordered.copy()
        # ordered里面添加一个取出来的数字
        my_ordered.append(rest[i])
        # temp 里面是剩余的数字，给下一个函数用
        temp = rest.copy()
        temp.pop(i)
        # 还有数据
        if len(temp):
            arrange_num(temp,my_ordered)
        else:
            # print("orderd:",my_ordered)
            for i in all_opr:
                if not calc(my_ordered,i):
                    #print(my_ordered,i)
                    # 翻译成我们看得懂的话
                    all_res.add(trans(my_ordered,i))
                    

"""
# 运算符号有6个, + - * / 还有被减和被除
# 参数一：给我的数字顺序,列表类型，里面存的数字
def insert_opr(num,opr):
    my_opr = opr.copy()
    #最少有2个数字才进行运算
    if len(num) > 1:
        #0-5对于6中运算
        for i in range(6):
            # 假如这里的运算符
            my_opr.append(i)
            

            if i == 0:# +
                pass
            elif i == 1:# -
                pass
            elif i == 2:# *
                pass
            elif i == 3:# /
                pass
            elif i == 4:# --
                pass
            elif i == 5:# //
                pass
"""
        
    
    


def main():
    global all_res
    while True:
        all_res = set()
        s = input("input 4 num in range 1-13,separate by space:")
        temp = s.split(" ")
        res = []
        for i in temp:
            if not i.isspace():
                if i.isnumeric():
                    res.append(int(i))
                else:
                    break
        if len(res)!=4:
            print("res",res)
            #os.system("cls")
            print("your input [%s] is illegal,Please re-enter!" % s)
            continue

        opr(4,[])
        # logic code
        # 1 3 4 6   6/(1-(3/4))
        # + - * / -- //
        arrange_num(res,[])
        for i in all_res:
            print(i)

if __name__ == "__main__":
    main()
