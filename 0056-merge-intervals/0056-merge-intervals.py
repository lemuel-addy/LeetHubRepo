class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort and merge intervals
        #runtime => O(nlogn)
        intervals.sort(key = lambda i: i[0]) #sort by the first index of intervals
        output = [intervals[0]]
        for start,end in intervals[1:]:
            #get the second index of the last interval in output to do check
            if output[-1][1] >= start:
                output[-1][1] = max(output[-1][1],end)
            else:
                output.append([start,end])
        return output

        