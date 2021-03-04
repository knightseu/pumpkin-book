# ihttps://www.lintcode.com/problem/1707/


m = {
    '0': ['4', '6'],
    '1': ['6', '8'],
    '2': ['7', '9'],
    '3': ['4', '8'],
    '4': ['0', '3', '9'],
    '5': [],
    '6': ['0', '1', '7'],
    '7': ['2', '6'],
    '8': ['1', '3'],
    '9': ['2', '4']
}

def knight_jump(m, step):
    rst = set()
    for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        dfs(m, i, step-1, i, rst)
    print("Total possible strings {}".format(len(rst)))

def dfs(m, c, step, result, results):

    if step == 0:
        results.add(result)
        return
    for nc in m[c]:
        dfs(m, nc, step-1, result+nc, results)

if __name__ == '__main__':
    knight_jump(m, 3)
