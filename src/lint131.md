# 131. The Skyline Problem
Given N buildings in a x-axis，each building is a rectangle and can be represented by a triple (start, end, height)，where start is the start position on x-axis, end is the end position on x-axis and height is the height of the building. Buildings may overlap if you see them from far away，find the outline of them。

An outline can be represented by a triple, (start, end, height), where start is the start position on x-axis of the outline, end is the end position on x-axis and height is the height of the outline.

Building Outline

# Example
Example 1

Input:
[
    [1, 3, 3],
    [2, 4, 4],
    [5, 6, 1]
]
Output:
[
    [1, 2, 3],
    [2, 4, 4],
    [5, 6, 1]
]
Explanation:
The buildings are look like this in the picture. The yellow part is buildings.
图片

Example 2

Input:
[
    [1, 4, 3],
    [6, 9, 5]
]
Output:
[
    [1, 4, 3],
    [6, 9, 5]
]
Explanation:
The buildings are look like this in the picture. The yellow part is buildings.
图片

Related Problems
