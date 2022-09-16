
def ucs(start, end, G, Distance, Cost):
    Queue = [[0, 0, -1, start]]
    Memory = []
    Visited = []
    while (len(Queue) > 0):
        Queue = sorted(Queue)
        Distance, Cost, Parent, Node = Queue.pop()
        Memory.append([Distance, Cost, Parent, Node])
        Distance = -Distance

        if (Node == end):
            s = end
            for i in range(len(Memory)-1, -1, -1):
                if Memory[i][3] == Parent:
                    s = Parent + "->" + s
                    Parent = Memory[i][2]
            f = open("task1output.txt", "w")
            f.write("TASK1:\n")
            f.write("Shortest Path:" + s + "\n")
            f.write("Shortest distance: {}". format(Distance) + "\n")
            f.write("Total Energy Cost: {}".format(Cost) + "\n\n")
            return

        if Node in Visited:
            continue
        for i in range(len(G[Node])):
            if G[Node][i] not in Visited:
                d = Distance + \
                    Distance["{}, {},".format(int(Node), int(G[Node][i]))]
                c = Cost + Cost["{}, {},".format(int(Node), int(G[Node][i]))]
                Queue.append([-d, c, Node, G[Node][i]])
        Visited.append(Node)
