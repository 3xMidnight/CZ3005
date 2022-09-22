from math import sqrt


def StraightLineDistance(coord, x, y):
    x1 = coord[x][0]
    y1 = coord[x][1]
    x2 = coord[y][0]
    y2 = coord[y][1]
    return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))


def astar(beg, end, G, Distance, Cost, maxCost, coord):
    queue = [[[beg], 0, 0, -1, beg]]
    memory = []
    visited = []
    while (len(queue) > 0):
        queue = sorted(queue)
        TotalDistance, dist, cost, parent, node = queue.pop()
        memory.append([parent, node])
        if (node == end):
            s = end
            for i in range(len(memory)-1, -1, -1):
                if memory[i][1] == parent:
                    s = parent + "->" + s
                    parent = memory[i][0]
            print(f"TASK3:\n")
            print(f"Shortest Path:" + s + "\n")
            print("Shortest Distance: {}".format(dist) + "\n")
            print("Shortest Distance: {}".format(cost) + "\n")
            return
        if node in visited:
            continue
        for i in range(len(G[node])):
            if G[node][i] not in visited:
                d = dist + Distance["{},{}".format(int(node), int(G[node][i]))]
                c = cost + Cost["{},{}".format(int(node), int(G[node][i]))]
                total = d + \
                    StraightLineDistance(coord, end, "{}".format(G[node][i]))
                if c <= maxCost:
                    queue.append([-total, d, c, node, G[node][i]])
        visited.append(node) 
