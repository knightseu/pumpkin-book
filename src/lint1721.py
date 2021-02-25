# https://www.lintcode.com/problem/1721/
from collections import deque

def check(str):

    if not str:
        return -1;

    stack = deque()

    # import pdb; pdb.set_trace()
            stack.append(c)
        else:
            # assumption here is only () in the string
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
    return len(stack)

if __name__ == '__main__':
    s1 = "((("
    print(check(s1))

    s2 = "()))(("
    print(check(s2))
