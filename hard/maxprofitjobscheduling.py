import heapq
class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        mix = []
        for i in range(len(profit)):
            mix.append((startTime[i], endTime[i], profit[i]))
        mix.sort()
        pq = []
        maxVal = 0
        for start, end, val in mix:
            while pq and pq[0][0] <= start:
                _, curVal = heapq.heappop(pq)
                maxVal = max(maxVal, curVal)
            heapq.heappush(pq,(end, maxVal + val))
            print(pq)

        while pq:
            _, curVal = heapq.heappop(pq)
            maxVal = max(maxVal, curVal)
        return maxVal


sol = Solution()
print(sol.jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70]))

'''
Let N be the length of the jobs array.

Time complexity: O(N\log N)O(NlogN)

Sorting jobs according to their starting time will take O(N\log N)O(NlogN) time.

We iterate over all NN jobs. For each job, we push the maximum profit job chain into the heap once which takes O(\log N)O(logN) time.

The total time complexity is therefore equal to O(N\log N)O(NlogN).

Space complexity: O(N)O(N)

Storing the start time, end time, and profit of each job takes 3\cdot N3⋅N space. Hence the complexity is O(N)O(N).

The space complexity of the sorting algorithm depends on the implementation of each programming language. For instance, in Java, the Arrays.sort() for primitives is implemented as a variant of quicksort algorithm whose space complexity is O(\log N)O(logN). In C++ sort() function provided by STL is a hybrid of Quick Sort, Heap Sort and Insertion Sort with the worst-case space complexity of O(\log N)O(logN). Thus the use of inbuilt sort() function adds O(\log N)O(logN) to space complexity.

Each of the NN jobs will be pushed into the heap. In the worst-case scenario, when all NN jobs end later than the last job starts, the heap will reach size NN.

The total space complexity is therefore equal to O(N)O(N).
'''
