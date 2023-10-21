# class Solution: 
#     def get_max_cycle_length(self, favorite: List[int]) -> int:
#         person_cnt = len(favorite)
#         max_cycle_length = 0

#         seen = set()

#         # for each person
#         for i in range(person_cnt):
#             # i - person i

#             # if person not part of any chain (chain with cycle)
#             if i in seen:
#                 continue
            
#             # begin of chain (chain with cycle)
#             begin_person = i

#             # visited nodes inside of chain (chain with cycle)
#             cur_visited = set()

#             # cur_person
#             cur_person = i

#             # try to build chain with cycle
#             while cur_person not in seen:
#                 seen.add(cur_person)
#                 cur_visited.add(cur_person)
#                 cur_person = favorite[cur_person]
            
#             # if cycle exists
#             if cur_person in cur_visited:
#                 # length of chain with cycle
#                 visited_person_cnt = len(cur_visited)

#                 # try to find length of cycle
#                 while begin_person != cur_person:
#                     visited_person_cnt -= 1
#                     begin_person = favorite[begin_person]
            
#                 max_cycle_length = max(max_cycle_length, visited_person_cnt)
        
#         return max_cycle_length
    
#     def get_max_chain_without_cycle_length(self, favorite: List[int]) -> int:
#         person_cnt = len(favorite)
#         max_chain_len = 0

#         # find mutal-favorite (a <-> b) pairs
#         pairs = []
#         visited = set()

#         for i in range(person_cnt):
#             if i not in visited and favorite[favorite[i]] == i:
#                 pairs.append((i, favorite[i]))
#                 visited.add(i)
#                 visited.add(favorite[i])

#         # build deps list, list that consits from deps from i (a -> b and c -> b, we shoul build such list [a,c] for b)
#         deps = collections.defaultdict(list)
#         for i in range(person_cnt):
#             deps[favorite[i]].append(i)

#         for src, dst in pairs:
#             # max chain length to src
#             max_dist_to_src = 0
            
#             q = collections.deque()
#             for dep in deps[src]:
#                 if dep != dst: q.append((dep, 1)) # dependent node and dist to dependent node
            
#             while q:
#                 cur_dependency, dist = q.popleft()
#                 max_dist_to_src = max(max_dist_to_src, dist)
#                 for next_dep in deps[cur_dependency]:
#                     q.append((next_dep, dist + 1))
            
#             max_dist_to_dst = 0
#             q = collections.deque()
#             for dep in deps[dst]:
#                 if dep != src: q.append((dep, 1))
            
#             while q:
#                 cur_dependency, dist = q.popleft()
#                 max_dist_to_dst = max(max_dist_to_dst, dist)
#                 for next_dep in deps[cur_dependency]:
#                     q.append((next_dep, dist + 1)) 

#             max_chain_len += 2 + max_dist_to_src + max_dist_to_dst

#         return max_chain_len

#     def maximumInvitations(self, favorite: List[int]) -> int:
#         return max(self.get_max_cycle_length(favorite), self.get_max_chain_without_cycle_length(favorite))


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        ans = 0
        n = len(favorite)
        cycles_of_2 = []
        seen = [False for _ in range(n)]
        for node in range(n):
            if seen[node]:
                continue
            if favorite[favorite[node]] == node:
                cycles_of_2.append((node, favorite[node]))
                seen[node] = True
                seen[favorite[node]] = True
        for node in range(n):
            if seen[node]:
                continue
            cycle_length = self.find_cycle(node, 1, {}, seen, favorite)
            ans = max(ans, cycle_length)
        
        if len(cycles_of_2) != 0:
            revfavorite = defaultdict(list)
            for node, fav in enumerate(favorite):
                if favorite[fav] != node:
                    revfavorite[fav].append(node)
            total_tail = 0
            for x, y in cycles_of_2:
                max_tail = self.max_depth(x, revfavorite) + self.max_depth(y, revfavorite)
                total_tail += max_tail
            ans = max(ans, 2 * len(cycles_of_2) + total_tail)
        return ans

    def find_cycle(self, node, length, path, seen, favorite):
        if seen[node]:
            return -1
        seen[node] = True
        path[node] = length
        if favorite[node] in path:
            return path[node] - path[favorite[node]] + 1
        return self.find_cycle(favorite[node], length+1, path, seen, favorite)
    
    def max_depth(self, node, graph, depth=0):
        res = depth
        for neigh in graph[node]:
            res = max(res, self.max_depth(neigh, graph, depth+1))
        return res