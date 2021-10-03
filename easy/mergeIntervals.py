# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
        def merge(self, intervals: [Interval]):
            """
            :type intervals: List[Interval]
            :rtype: List[Interval]
            """
            intervals.sort(key = lambda x:x.start, reverse=False)
            result=[]
            for interval in intervals:
                if len(result) == 0 or result[-1].end < interval.start:
                    result.append(interval)
                else:
                    result[-1].end = max(result[-1].end, interval.end)
            for interval in result:
                print(interval.start,interval.end)
            return result


sol = Solution()
print(sol.merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]))

'''
Time complexity : O(n\log{}n)O(nlogn)

Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by the O(n\log{}n)O(nlogn) complexity of sorting.

Space complexity : O(\log N)O(logN) (or O(n)O(n))

If we can sort intervals in place, we do not need more than constant additional space, although the sorting itself takes O(\log n)O(logn) space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.
'''