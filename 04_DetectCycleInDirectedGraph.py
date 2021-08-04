class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited = [False] * (V + 1)
        recStack = [False] * (V + 1)
        for node in range(V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack, adj) == True:
                    return True
        return False
    
    def isCyclicUtil(self, node, visited, recStack,adj):
        visited[node] = True
        recStack[node] = True
 
        for neighbour in adj[node]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack, adj) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        recStack[node] = False
        return False
