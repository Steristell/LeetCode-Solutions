class Solution(object):
    def candy(self, ratings):
        distribution = [1] * len(ratings)
        j = len(ratings) - 2
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1] and distribution[i] <= distribution[i-1]:
                distribution[i] = distribution[i-1] + 1
            if ratings[j] > ratings[j+1] and distribution[j] <= distribution[j+1]:
                distribution[j] = distribution[j+1] + 1
            j -= 1
        return sum(distribution)
        