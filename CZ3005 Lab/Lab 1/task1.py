
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
           
