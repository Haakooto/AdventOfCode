from numpy import prod

def evaluate_1(expr):
    expr = expr.replace(" ", "")
    val = 0
    idx = 0
    prev_op = "+"
    while idx < len(expr):
        if expr[idx] == "(":
            tmp_idx = idx + 1
            cnt = 1
            while cnt:
                if expr[tmp_idx] == "(":
                    cnt += 1
                elif expr[tmp_idx] == ")":
                    cnt -= 1
                tmp_idx += 1
            sub_val = evaluate_1(expr[idx + 1 : tmp_idx - 1])
            val = eval(f"{val}{prev_op}{sub_val}")
            idx = tmp_idx - 1
        elif expr[idx] == "*":
            prev_op = "*"
        elif expr[idx] == "+":
            prev_op = "+"
        else:
            sub_val = int(expr[idx])
            val = eval(f"{val}{prev_op}{sub_val}")
        idx += 1
    return val


def evaluate_2(expr):
    while "(" in expr:
        idx = expr.find("(")
        tmp_idx = idx + 1
        cnt = 1
        while cnt:
            if expr[tmp_idx] == "(":
                cnt += 1
            elif expr[tmp_idx] == ")":
                cnt -= 1
            tmp_idx += 1
        expr = f"{expr[:idx]}{evaluate_2(expr[idx + 1: tmp_idx -1])}{expr[tmp_idx +  1:]}"
    return prod([eval(i) for i in expr.split("*")])


sum_1 = 0
sum_2 = 0
for line in open("input").read().strip().splitlines():
    sum_1 += evaluate_1(line)
    sum_2 += evaluate_2(line)
print(sum_1)
print(sum_2)
