from collections import deque


def print_orders(tasks, prerequisites):
    rst = []
    if tasks <=0:
        return
    inDegree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}
    
    for pre in prerequisites:
        parent, child = pre[0], pre[1]
        inDegree[child] += 1
        graph[parent].append(child)
    
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)
    print_all(graph, inDegree, sources, rst)

def print_all(graph, inDegree, sources, rst):
   if sources:
       for source in sources:
           rst.append(source)
           srcCopy = deque(sources)
           srcCopy.remove(source)
           for child in graph[source]:
               inDegree[child] -= 1
               if inDegree[child] == 0:
                   srcCopy.append(child)
           print_all(graph, inDegree, srcCopy, rst)
           
           rst.remove(source)
           for child in graph[source]:
               inDegree[child] += 1
           pass
       
   if len(rst) == len(inDegree):
       print(rst)

def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
