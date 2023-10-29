class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #create an adjacency list (graph) to store vertices(denominators) and edges(values)
        adj = collections.defaultdict(list)
        #populate the adjacency list with numerators mapped to their denom and values
        for i,eq in enumerate(equations):
            a,b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a,1/values[i]])
        
        #create a bsf function to calculate value and find target from source
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q,visit = deque(),set()
            #start with the numerator itself(source) with a weight of 1
            q.append([src,1])
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                #adj[n] can have multiple paths
                for nei,wei in adj[n]:
                    #if you dont check for visited neighbors, loop might be infinite(cycles)
                    if nei not in visit:
                        q.append([nei, w * wei])
                        visit.add(nei)
            return -1
        #do the bsf for each query in queries (source, target) i.e., (numerator, target denom)
        return[bfs(q[0],q[1]) for q in queries]