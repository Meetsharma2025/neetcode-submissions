class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        indx = {}
        count = 1
        for i in nums:
                if(i not in indx):
                        indx[i] = count
                elif(i in indx):
                        indx[i]+=1 
        sorted_items = sorted(indx.items(), key=lambda x: x[1], reverse=True)
        return [num for num, freq in sorted_items[:k]]