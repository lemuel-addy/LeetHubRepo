class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #the end or target is the N-1 i.e. length-1
        end = len(graph)-1

        #using dfs take the start node i.e. 0 and the path i.e. [0] and output -> []
        def dfs(node,path,output):
            #if node is target, append the path to output(an array of paths) and its is returned
            if node == end:
                output.append(path)
            #traverse through graph and use dfs to create a path for each node until you reach end
            for i in graph[node]:
                dfs(i, path+[i],output)
        output=[]
        #start dfs with 0,[0],[] and it will create the paths for all nodes in graph
        dfs(0,[0],output)
        return output
        