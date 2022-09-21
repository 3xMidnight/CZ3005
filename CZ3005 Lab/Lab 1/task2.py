from queue import PriorityQueue

def ucs(source, dest,budget,dist ,g, cost):
    final_path = "No path found"
    final_dist = 0
    final_energy = 0


    prio_queue = PriorityQueue()
    prio_queue.put((0,(0, [source])))

    visited = set()

    while prio_queue.not_empty:
        pair = prio_queue.get()

        current_energy, current_path = pair[1]
        current_node = current_path[-1]

        if current_node not in visited:
            visited.add(current_node)

            if current_node == dest:
                final_path = "->".join(current_path)

                total_dist = 0
                for i in range(len(current_path) - 1):
                    total_dist += dist[f"{current_path[i]},{current_path[i+1]}"]
                final_dist = total_dist

                total_energy = 0

                for i in range(len(current_path) - 1):
                    total_energy += cost[f"{current_path[i]},{current_path[i+1]}"]
                final_energy = total_energy
                print(f"Shortest path: {final_path}")
                print(f"Shortest distance: {final_dist}")
                print(f"Total Energy Cost: {final_energy}")

                return final_path, final_dist, final_energy

            for next in g[current_node]:
                new_energy = current_energy + cost[f"{current_node},{next}"]

                if new_energy <= budget:
                    new_dist = dist[f"{current_node},{next}"]
                    score = pair[0] + new_dist

                    new_path = current_path.copy()
                    new_path.append(next)

                    prio_queue.put((score, (new_energy, new_path)))
                
    print(f"Shortest Path: {final_path}")
    print(f"Shortest Distance: {final_dist}")
    print(f"Total Energy Cost: {final_energy}")