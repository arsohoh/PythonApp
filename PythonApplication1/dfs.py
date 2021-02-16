
graph = {
            'A' : ['B','C'],
            'B' : ['D', 'E'],
            'C' : ['F'],
            'D' : [],
            'E' : ['F'],
            'F' : []
    }

print(graph);
visited = []; # or use visited = set();

def dfsOrder(v,g,n):

    if n not in v:
        v.append(n);
        print(n, sep=' , ', end=" ");
        for neighbour in graph[n]:
            dfsOrder(v,g,neighbour);


dfsOrder(visited,graph,'A');





    