
import task1,task2
from timeit import timeit
from typing import Tuple
import json

PERF_SAMPLES = 5000

PathInfo =''
EnergyBudget = 287932


def main():
    G, Cost, Coord, Dist = load_json_files()
    task1.ucs('1', '50', Dist, G)

    task2.ucs('1', '50', EnergyBudget, Dist, G, Cost)
    
    task3.astar('1', '50', G, Dist, Cost, EnergyBudget, Coord)


def load_json_files():
    g = open("G.json")
    cost = open("Cost.json")
    coord = open("Coord.json")
    dist = open("Dist.json")
    G = json.load(g)
    Cost = json.load(cost)
    Coord = json.load(coord)
    Dist = json.load(dist)
    return G, Cost, Coord, Dist
    

if __name__ == "__main__":
    main()
