# https://www.lintcode.com/problem/188/?_from=ladder&fromId=29
import math
from collections import deque

def insert_five(num):
    li = deque()
    n = num
    while(n > 0):
        x = n % 10
        n = math.floor(n / 10)
        print("{}, {}".format(x, n))
        li.appendleft(x)
    print(li)
    found  = False
    rst = 0
    for y in li:
        if found or (not found and y >=5):
            rst = rst * 10 + y
        else:
           rst = (rst * 10 + 5) * 10 + y
           found = True
    if not found:
        rst = rst * 10 + 5

    print(rst)

insert_five(12345)
insert_five(59561)
insert_five(9876)
