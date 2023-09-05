class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = collections.defaultdict(list)

        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord("a")] += 1
        #     ans[tuple(count)].append(s)
        # return ans.values()

        map = defaultdict(list)
        
        result = []
        for s in strs:
            #tuple makes it able to be used as a key i.e. storing an array as a single variable
            sorted_s = tuple(sorted(s))            
            #get the sorted form and use it as a key, hence all anagrams add to it
            #appending the values themselves not adding the occurences like in 1 + map(s[i],0)
            map[sorted_s].append(s)
            
        for value in map.values():
            result.append(value)
        return result
