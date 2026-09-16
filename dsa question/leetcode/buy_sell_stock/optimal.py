def buy_sell_stock(nums):
    n=len(nums)

    min_value=nums[0]
    max_profit=0

    for i in range(0,n):

        min_value=min(min_value,nums[i])
        profit=nums[i]-min_value
        max_profit=max(max_profit,profit)


    return max_profit
    
nums = [1, 2, 3, 4, 5, 6, 3, 2]
profit=buy_sell_stock(nums)

print("max profit is :",profit)
        