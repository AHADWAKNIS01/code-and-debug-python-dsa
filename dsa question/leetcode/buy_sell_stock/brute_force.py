# Description:
# Find the best day to buy and sell a stock to get the maximum profit.
# Return the maximum profit along with the buy and sell indices.
#
# Time Complexity (TC): O(n^2)
# Space Complexity (SC): O(1)


def buy_sell_stock(nums):
    n = len(nums)

    max_profit = 0       # Stores the maximum profit
    buy_sell_stock = 0   # Stores the best buying index
    sell_stock = 0       # Stores the best selling index

    # Choose the buying day
    for i in range(0, n - 1):

        # Choose the selling day after buying
        for j in range(i + 1, n):

            # Calculate the profit
            profit = nums[j] - nums[i]

            # Update only when a better profit is found
            if profit > max_profit:
                max_profit = profit
                buy_sell_stock = i
                sell_stock = j

    # Return profit, buy index, and sell index
    return max_profit, buy_sell_stock, sell_stock


# Input array
nums = [1, 2, 3, 4, 5, 6, 3, 2]

# Call the function
profit, buy, sell = buy_sell_stock(nums)

# Display the result
print(f"The best time to buy is {buy} and sell {sell}, "
      f"and the profit you will get is {profit}")