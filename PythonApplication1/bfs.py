
graph = {
            'A' : ['B','C'],
            'B' : ['D', 'E'],
            'C' : ['F'],
            'D' : [],
            'E' : ['F'],
            'F' : []
    }

print(graph);

visited= [];
queue =[];

def bfsOrder (visited,graph,node):
    visited.append(node);
    queue.append(node);

    while queue:
        s = queue.pop(0);
        print(s , " " );
        
        for neighbor in graph[s]:
            #print(neighbor,":",graph[s])
            if neighbor not in visited:
                visited.append(neighbor);
                queue.append(neighbor);


bfsOrder(visited,graph,'A');

