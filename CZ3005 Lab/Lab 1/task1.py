
def ucs(start, end, G, Distance, Cost):
    Queue = [[0, 0, -1, start]]
    Memory = []
    Visited = []
    while (len(Queue) > 0):
        Queue = sorted(Queue)
        dist, cost, Parent, Node = Queue.pop()
        Memory.append([distance, cost, Parent, Node])
        dist = -dist

        if (Node == end):
            s = end
            for i in range(len(Memory)-1, -1, -1):
                if Memory[i][3] == Parent:
                    s = Parent + "->" + s
                    Parent = Memory[i][2]
            f = open("task_1_output.txt", "w")
            f.write("TASK1:\n")
            f.write("Shortest Path:" + s + "\n")
            f.write("Shortest distance: {}".format(dist) + "\n")
            f.write("Total Energy Cost: {}".format(cost) + "\n")
            return

        if Node in Visited:
            continue
        for i in range(len(G[Node])):
            if G[Node][i] not in Visited:
                d = dist + Distance["{}, {}".format(int(Node), int(G[Node][i]))]
                c = cost + Cost["{}, {}".format(int(Node), int(G[Node][i]))]
                Queue.append([-d, c, Node, G[Node][i]])
        Visited.append(Node)

