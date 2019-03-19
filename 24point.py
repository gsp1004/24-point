import os


# 重构
# 函数功能：生成所有运算符的组合情况并返回
# 参数一：要计算的数字个数，例如输入 1 2 3 4 ，那么num = 4，
#           保留这个参数是为了后续可以扩展，比如计算5个数得到36等，这里推荐使用len(all_num)的方式传入
# 参数二：递归调用时候，传给后面用
# 参数三：强制传入一个空列表类型，供return用
# 返回值：返回所有运算符的组合情况
def opr(num, ret, result):
    # 如果的判断意思主要是看是否需要递归调用自己
    if num > 2:
        for i in range(6):
            my_ret = ret.copy()
            my_ret.append(i)
            opr(num-1, my_ret, result)
        return result  # 一定要记得返回
    elif num == 2:
        for i in range(6):
            temp = ret.copy()
            temp.append(i)
            result.append(temp)
        return result  # 如果num == 2 ，那么就从这里返回，所以这个必须要，否则num == 2 的时候没有返回值
    else:
        print("num should great than 1")
        return []


# 函数功能：计算这组数字和这组操作符号的结果是否是24
# 参数一：数字的排列，列表类型，eg：[1,2,3,4]
# 参数二：操作符的排列，列表类型，eg:[0,0,2]
# 参数三：期望最后的得数是多少，默认值是24
# 返回值：  0   表示结果是24
#           -1  表示结果不是24
def calc(num, opr, target_num=24):
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
    if res == target_num:
        return 0
    else:
        return -1
        

# 函数功能：将结果翻译成正常的数学表达式
# 参数一：数字的排列，列表类型，eg: [1,2,3,4]
# 参数二：操作符的排列，列表类型，eg: [0,0,2]
# 返回值：字符串类型，eg："(1+2+3)*4"
def trans(num, opr, target_num=24):
    res = ""
    for i in range(len(opr)):
        if i == 0:  # res初始化为第一个数字
            res = str(num[i])
        if opr[i] == 0:  # 加号
            res = res + "+" + str(num[i+1])
        elif opr[i] == 1:  # 减号
            res = res + "-" + str(num[i+1])
        elif opr[i] == 2:  # 乘号，需要考虑前一个符号是不是加/减/被减，如果是，需要加括号
            if i != 0 and (opr[i-1] == 0 or opr[i-1] == 1 or opr[i-1] == 4):
                res = "(" + res + ")"
            res = res + "*" + str(num[i+1])
        elif opr[i] == 3:  # 除号，需要考虑前一个符号是不是加/减/被减，如果是，需要加括号
            if i != 0 and (opr[i-1] == 0 or opr[i-1] == 1 or opr[i-1] == 4):
                res = "(" + res + ")"
            res = res + "/" + str(num[i+1])
        elif opr[i] == 4:  # 被减号，需要考虑前一个符号是不是加/减/被减，如果是，需要加括号
            if i != 0 and (opr[i-1] == 0 or opr[i-1] == 1 or opr[i-1] == 4):
                res = "(" + res + ")"
            res = str(num[i+1]) + "-" + res
        elif opr[i] == 5:  # 被除号，只要不是第一个运算符（前面有运算），就必须加括号
            if i != 0:
                res = "(" + res + ")"
            res = str(num[i+1]) + "/" + res
    res = res + "=" + str(target_num)
    return res


# 函数功能：将所有数字进行排列
# 参数一：剩余未排列的数字，列表类型，eg: [3,4]
# 参数二：已排列的数字，列表类型，eg: [1,2]
# 参数三：强制传入一个空集合类型，供return用，使用集合是为了去重
# 返回值：集合类型，eg：{[1,2,3,4],[2,1,3,4]}
def arrange_num(rest, ordered, all_ordered_num):
    for i in range(len(rest)):
        my_ordered = ordered.copy()
        # ordered里面添加一个取出来的数字
        my_ordered.append(rest[i])
        # temp 里面是剩余的数字，给下一个函数用
        my_rest = rest.copy()
        my_rest.pop(i)
        # 还有数据
        if len(my_rest):
            arrange_num(my_rest, my_ordered, all_ordered_num)
        else:
            # 将排列的数字添加到，这里必须将my_ordered转化为tuple，因为往集合set中添加list会报错
            #     a.add([1,2])
            # TypeError: unhashable type: 'list'
            all_ordered_num.add(tuple(my_ordered))
    return all_ordered_num


def main():
    INPUT_NUM_COUNT = 4  # 输入的数字的个数
    TARGET_NUM = 24  # 计算的结果
    MIN = 1  # 输入的数字最小值
    MAX = 13  # 输入的数字最大值
    while True:
        s = input("input %d num in range %d-%d,separated by space:" % (INPUT_NUM_COUNT, MIN, MAX))
        # 用于提取用户输入的数字，保存在列表res中
        temp = s.split(" ")
        # res用于保存用户输入的 INPUT_NUM_COUNT 个数字
        res = []
        for i in temp:
            if not i.isspace():
                if i.isnumeric():
                    if MIN <= int(i) <= MAX:
                        res.append(int(i))
                else:
                    break
        if len(res) != INPUT_NUM_COUNT:
            print("your input [%s] is illegal,Please re-enter!" % s)
            continue

        # 获取所有的运算符排列
        all_opr = opr(INPUT_NUM_COUNT, [], [])
        # print(len(all_opr))

        # 获取所有的数字的排列，返回的是列表类型，列表套列表
        all_ordered_num = arrange_num(res, [], set())
        # print(len(all_ordered_num))

        # 用于保存所有要显示的结果，用集合去重
        all_res = set()

        for i in all_ordered_num:
            for j in all_opr:
                if not calc(i, j, target_num=TARGET_NUM):  # 结果是24，就往结果集合中添加
                    all_res.add(trans(i, j, target_num=TARGET_NUM))

        # 输出结果到屏幕上
        for i in all_res:
            print(i)


if __name__ == "__main__":
    main()
