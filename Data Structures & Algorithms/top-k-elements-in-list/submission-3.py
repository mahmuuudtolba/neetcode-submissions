class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First i need a dict to store {number : #show}
        # loop and increase the #show
        # a second loop to get numbers where #show > k
        counter = {}
        for i , n in enumerate(nums):
            counter[n] = counter.get(n , 0) + 1
        
        arr = []
        for num, cnt in counter.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res