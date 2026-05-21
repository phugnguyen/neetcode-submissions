class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        # dictionary to hold compliments

        # iterate through list, store the compliment
        for i, num in enumerate(nums):
            compliment = target - num
            complimentIndex = compliments.get(compliment)
            if complimentIndex != None:
                return [complimentIndex, i]
            else: 
                compliments.update({ num: i })


        