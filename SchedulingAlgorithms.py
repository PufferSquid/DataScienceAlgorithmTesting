import math


# Based off pseudocode (returns a dictionary of the most optimal distances from the destination to the start node)
# e.g. with a result of: {1: 0, 2: 6, 3: 2, 4: 6, 5: 7, 6: 4, 7: 5, 8: 7, 9: 7, 10: 4}
# The most optimal distance from node 3 to node 1 (assuming start node is 1), is 2. "Key = destination and value = optimal distance"
def Dijkstra(graph : dict, start_node : int):
    
    distances = {node: math.inf for node in graph}
    distances[start_node] = 0
    
    visited : list = []
    
    for i in range(len(graph)):
        min_distance = math.inf
        current_node = None
        
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node
        
        if current_node is None:
            break
            
        visited.append(current_node)
        
        for neighbor, cost in graph[current_node].items():
            if neighbor not in visited:
                new_distance = distances[current_node] + cost
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances


# Based off pseudocode (returns a dictionary of the most optimal distances from the destination to the start node)
# e.g. with a result of: {1: 0, 2: 6, 3: 2, 4: 6, 5: 7, 6: 4, 7: 5, 8: 7, 9: 7, 10: 4}
# The most optimal distance from node 3 to node 1 (assuming start node is 1), is 2. "Key = destination and value = optimal distance"
def BellmanFord(graph: dict, start_node: str):

    edges = []
    node_to_index = {}
    index_to_node = {}
    
    for i, node in enumerate(graph.keys()):
        node_to_index[node] = i
        index_to_node[i] = node
    
    num_vertices = len(graph)
    
    for u, neighbors in graph.items():
        for v, weight in neighbors.items():
            edges.append((node_to_index[u], node_to_index[v], weight))
    
    num_edges = len(edges)
    
    distances = [math.inf] * num_vertices
    distances[node_to_index[start_node]] = 0
    
    for i in range(num_vertices):
        for j in range(num_edges):
            u, v, weight = edges[j]
            
            if distances[u] != math.inf and distances[u] + weight < distances[v]:
                if i == num_vertices - 1:
                    return None  
                
                distances[v] = distances[u] + weight
     
    result = {}
    for i in range(num_vertices):
        node_name = index_to_node[i]
        result[node_name] = distances[i] if distances[i] != math.inf else math.inf
    
    return result



