class Solution(object):
    def distributeCandies(self, candyType):
        unique_type = len(set(candyType))
        sister_candies = len(candyType)//2
        return min(unique_type,sister_candies)
        