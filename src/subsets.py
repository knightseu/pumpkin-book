# https://www.jiuzhang.com/problem/subsets/

def dfs(myset, index, result, results):
    results.append(list(result))
    for i in range(index, len(myset)):
        result.append(myset[i])
        dfs(myset, i+1, result, results)
        result.pop()
    return

if __name__ == '__main__':
    myset = [1, 2, 3]
    results = []
    dfs(sorted(myset), 0, [], results)
    for rst in results:
        print(rst)
