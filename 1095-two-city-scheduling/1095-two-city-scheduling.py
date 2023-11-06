class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #brute solution -> O(n^2)
        #using dynamic programming, find the best outcome for all possibilties i.e. 2->4->8->16

        #optimized solution: using greedy algorithm
        #runtime is O(nlogn) because you will iterate once to get difference and sort the list
        diffs = []
        res = 0
        for cA,cB in costs:
            diffs.append([cB-cA, cA, cB])
        diffs.sort()
        for i in range(len(diffs)):
            if i < len(diffs)//2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]
        return res


