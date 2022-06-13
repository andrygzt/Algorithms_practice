stocks= [7,6,4,3,1]


# stocks= [1,2,3,4,5]
#len 5
# day    ^
# look           ^
# look+1       ^            


# stocks=[7,1,5,3,6,4]


def max_profit(arr):
    price = 0
    cost = 0
    profit = 0
    day= 0
    
    #looking for minimus
    while day<(len(arr)-1):
        if arr[day]<= arr[day+1]:
            cost = arr[day]
            look = day+1
            #looking for the maximun
            while look<(len(arr)-1):
                if arr[look]>= arr[look+1]:
                    price = arr[look]
                    profit += price-cost
                    day=look+1
                    break
                else:
                    look+=1
                    if look==len(arr)-1:
                        price = arr[look]
                        profit += price-cost
                        day = look+1
                        break
        else:
            day+=1
    return profit


print(max_profit(stocks))


'''
Time complexity is O(n) where n the lenght of the array
Space complexity is O91) because there is no a new array, or data structure.
'''