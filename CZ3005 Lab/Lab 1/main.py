import json
from task1 import ucs
import task2
import task3

g = open("G.json")
cost = open("Cost.json")
coord = open("Coord.json")
dist = open("Dist.json")
G = json.load(g)
Cost = json.load(cost)
Coord = json.load(coord)
Dist = json.load(dist)
ucs ("1", "50", G, Dist, Cost)
with open('task_1_output.txt') as fp:
    data1 = fp.read()

