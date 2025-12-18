# LeetCode: Best Time to Buy and Sell Stock
# Problem: Find maximum profit by buying on one day and selling on a later day

from typing import List

# ============================================
# YOUR ORIGINAL CODE (WITH ISSUES)
# ============================================
class Solution_Original:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        smallest_index = 0
        
        # ISSUE 1: range(len(prices)-1) misses the last element
        for i in range(len(prices)-1):
            if prices[i] < smallest:
                smallest = prices[i]
                smallest_index = i
        
        largest = smallest
        
        # ISSUE 2: Wrong range calculation - doesn't correctly iterate through remaining elements
        for j in range(len(prices)-smallest_index-1):
            if prices[smallest_index+j] > largest:
                largest = prices[smallest_index+j] 
        
        if largest == smallest:
            return 0
        else:
            return(largest-smallest)


# ============================================
# ISSUES IDENTIFIED:
# ============================================
# 1. First loop: range(len(prices)-1) doesn't check the last element
#    Should be: range(len(prices)) or range(1, len(prices))
#
# 2. Second loop: range(len(prices)-smallest_index-1) is incorrect
#    Should iterate from smallest_index+1 to end: range(smallest_index+1, len(prices))
#
# 3. Algorithm flaw: Finding global minimum doesn't guarantee best profit
#    Example: prices = [3, 2, 6, 5, 0, 3]
#    - Global min is 0 at index 4
#    - Max after index 4 is 3
#    - Profit = 3
#    - But better profit: buy at 2 (index 1), sell at 6 (index 2) = profit 4
#
# 4. Edge case: If smallest_index is the last element, second loop won't run correctly


# ============================================
# CORRECTED VERSION (FIXING YOUR APPROACH)
# ============================================
class Solution_Fixed:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        smallest = prices[0]
        smallest_index = 0
        
        # Fix 1: Check all elements including the last one
        for i in range(1, len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
                smallest_index = i
        
        # Fix 2: Correctly iterate from smallest_index+1 to end
        largest = smallest
        for j in range(smallest_index + 1, len(prices)):
            if prices[j] > largest:
                largest = prices[j]
        
        if largest == smallest:
            return 0
        else:
            return largest - smallest


# ============================================
# OPTIMAL SOLUTION (Recommended)
# ============================================
# The issue with finding global minimum is that it might not give the best profit.
# Better approach: Track minimum price seen so far AND maximum profit simultaneously.

class Solution_Optimal:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        min_price = prices[0]  # Minimum price seen so far
        max_profit = 0        # Maximum profit we can make
        
        # For each day, calculate profit if we sell today
        # (bought at the minimum price seen so far)
        for i in range(1, len(prices)):
            # Update minimum price if we see a lower price
            if prices[i] < min_price:
                min_price = prices[i]
            
            # Calculate profit if we sell today
            profit = prices[i] - min_price
            
            # Update maximum profit if this is better
            if profit > max_profit:
                max_profit = profit
        
        return max_profit


# ============================================
# TEST CASES
# ============================================
def test_solutions():
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),      # No profit possible
        ([2, 4, 1], 2),             # Buy at 2, sell at 4
        ([3, 2, 6, 5, 0, 3], 4),   # Buy at 2, sell at 6 (not 0->3)
    ]
    
    print("Testing Original Solution:")
    sol_orig = Solution_Original()
    for prices, expected in test_cases:
        result = sol_orig.maxProfit(prices)
        status = "✓" if result == expected else "✗"
        print(f"  {status} prices={prices}, expected={expected}, got={result}")
    
    print("\nTesting Fixed Solution:")
    sol_fixed = Solution_Fixed()
    for prices, expected in test_cases:
        result = sol_fixed.maxProfit(prices)
        status = "✓" if result == expected else "✗"
        print(f"  {status} prices={prices}, expected={expected}, got={result}")
    
    print("\nTesting Optimal Solution:")
    sol_opt = Solution_Optimal()
    for prices, expected in test_cases:
        result = sol_opt.maxProfit(prices)
        status = "✓" if result == expected else "✗"
        print(f"  {status} prices={prices}, expected={expected}, got={result}")

if __name__ == "__main__":
    test_solutions()

