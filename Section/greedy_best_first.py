#create a graph 
graph ={
    's': [('a' ,1),('b' ,4)],
    'a': [('b' ,2),('c' ,5),('g' ,12)],
    'b': [('c' ,2)],
    'c': [('g' ,3)],
}
#heuristic of each node in graph
h_table ={
    's':7,
    'a':6,
    'b':4,
    'c':2,
    'g':0
}
# create helper function to calculate the H-cost of path
def path_h_cost(path):
    g_cost = 0
    for (node , cost) in path:  #from path recieve each node and it's cost
        g_cost+=cost
    last_node = path[-1][0]      # to store the last node in the graph 
    h_cost =h_table[last_node]   # to recieve the h_cost of last node from h_table
    return  h_cost , last_node   # print the last node and the heuristic cost
#examples
path1 = [('s' ,0) , ('a',1), ('c' , 5)]
print(path_h_cost(path1))
#----------------------------------
path2 = [('s' ,0) , ('a',1), ('b' , 2) , ('c' ,2) , ('g' , 3)]
print(path_h_cost(path2))

# create a greedy best search algorithm
def greedy_search(graph , start , goal):
    visited =[]
    queue = [[(start , 0)]]
    while queue:
        queue.sort(key= path_h_cost) #sorting by h_cost
        path = queue.pop(0)  #choocing smallest h_cost
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)  #if node is not in visited list add it 
        if node == goal:
            return path
        else:
            adj_nodes = graph.get(node , [])
            for(new_node , cost) in adj_nodes:
                new_path = path.copy()
                new_path.append((new_node, cost))
                queue.append(new_path)

#calling greedy search function                 
solution = greedy_search(graph , 's' , 'g')
print( 'Solution = ' , solution)
# to print the h_cost only by calling the path_h_cost function without last_node we write [0]
print('Cost of Solution = ' , path_h_cost(solution)[0])
