from collections import Counter, deque

def make_tree(str):
    count = Counter(str)
    el = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(el) != 1:
        while len(el) > 1:
            weight = el[0][1] + el[1][1]
            comb = {0: el.popleft()[0], 1: el.popleft()[0]}
            for n, j in enumerate(el):
                if weight > j[1]:
                    continue
                else:
                    el.insert(n, (comb, weight))
                    break
            else:
                el.append((comb, weight))
        else:
            weight = el[0][1]
            comb = {0: el.popleft()[0], 1: None}
            el.append((comb, weight))
        return el[0][0]

def haffman_code(tree, string=''):
    if not isinstance(tree, dict):
        res_code[tree] = string
    else:
        haffman_code(tree[0], string=f'{string}0')
        haffman_code(tree[1], string=f'{string}1')

res_code = dict()
str = "i hate haffman and recursion"
haffman_code(make_tree(str))

for i in str:
    print(res_code[i], end='')
