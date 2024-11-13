class Solution(object):
    def maximumBeauty(self, items, queries):
        items.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        max_beauty_at_price = []
        current_max_beauty = 0
        idx = 0
        
        for price, beauty in items:
            current_max_beauty = max(current_max_beauty, beauty)
            max_beauty_at_price.append((price, current_max_beauty))
        
        answer = [0] * len(queries)
        
        for query, original_index in sorted_queries:
            left, right = 0, len(max_beauty_at_price) - 1
            while left <= right:
                mid = (left + right) // 2
                if max_beauty_at_price[mid][0] <= query:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if right == -1:
                answer[original_index] = 0
            else:
                answer[original_index] = max_beauty_at_price[right][1]
        
        return answer
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        