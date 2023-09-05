class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Time complexity is O(M*N)
        #Hashmap of letters method to avoid sorting
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26 #an array with a 0 for each character i.e. lowercase letter in alphabet  
        # for each string in strs, loop through and get the count array for it         
            for c in s: #the letters in the string
                count[ord(c) - ord("a")] += 1 #changing that position from 0 default to 1 to create the pattern
            ans[tuple(count)].append(s) #append that string to the key to create the map
        return ans.values()

        #Time complexity O(m*nlogn)
        # map = defaultdict(list)
        # result = []
        # for s in strs:
            #tuple makes it able to be used as a key i.e. storing an array as a single variable
            # sorted_s = tuple(sorted(s))            
            #get the sorted form and use it as a key, hence all anagrams add to it
            #appending the values themselves not adding the occurences like in 1 + map(s[i],0)
            # map[sorted_s].append(s)
            
        # for value in map.values():
        #     result.append(value)
        # return result
