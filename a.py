import os
import sys
INF = float('inf')
input_file = os.path.join(sys.path[0], 'dijkstra.inp')
input1_file = os.path.join(sys.path[0], 'dijkstra.out')
output1_file = os.path.join(sys.path[0], 'dijkstra1.lvm')
################################def input_data():
with open(input_file) as f:
        global vertices, edges 
        global start, finish
        vertices, edges, start, finish = list(map(int, f.readline().split()))
        global a 
        a = [[INF for col in range(vertices + 1)] for row in range(vertices + 1)]
        for i in range(edges):
            u, v, len = list(map(int, f.readline().split()))
            a[u][v] = len
fi = open(input1_file, 'r', encoding='UTF-8')
data3 = fi.read(1)
data4 = fi.read()
print(data4)
i = fi.__sizeof__()
for i in range(i-1):
    j=i+1
    for j in range(i):
        k = a[i][j]
        if(a[i][j] != INF):
            print(k)
            open(output1_file,'a')
            f.write(str(k))
            f.close()
fi.close()