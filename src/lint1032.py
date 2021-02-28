# https://www.jiuzhang.com/problem/letter-case-permutation/
# 给定一个字符串S，我们可以将其中所有的字符任意切换大小写并得到一个新的字符串。将所有可生成的新字符串以一个列表的形式输出。

def mutate(c):
    if c.islower():
        return c.upper()
    else:
        return c.lower()


def dfs(s, start_index, rst):
    rst.append(s)
    for i in range(start_index, len(s)):
        if s[i].isdigit():
            continue
        else:
            # recursive call here
            new_s = s[:i] + mutate(s[i]) + s[i+1:]
            dfs(new_s, i+1, rst)

if __name__ == '__main__':
    results = []
    str = "a1b2"
    dfs(str, 0, results)
    print(results)
