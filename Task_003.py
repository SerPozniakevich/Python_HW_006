# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

mult = '*'
div = '/'
plus = '+'
minus = '-'

evaluation = '2 + 2 * 2 / 2 - 2'
eval_list = evaluation.split()
i = 0
res = 0
while len(eval_list) != 1:
    while True:
        print(eval_list)
        el = eval_list[i]
        if el == mult or el == div:
            if el == mult:
                res = float(eval_list[i - 1]) * float(eval_list[i + 1])
            else:
                res = float(eval_list[i - 1]) / float(eval_list[i + 1])
            eval_list[i] = str(res)
            eval_list.pop(i + 1)
            eval_list.pop(i - 1)
            i = 0
            if mult and div not in eval_list:
                break
        else:
            i += 1


    while True:
        print(eval_list)       
        el = eval_list[i] 
        if el == plus or el == minus:
            if el == plus:
                res = float(eval_list[i - 1]) + float(eval_list[i + 1])
            else:
                res = float(eval_list[i - 1]) - float(eval_list[i + 1])
            eval_list[i] = str(res)
            eval_list.pop(i + 1)
            eval_list.pop(i - 1)
            i = 0
            if plus and minus not in eval_list:
                break
        else:
            i += 1

print(res)