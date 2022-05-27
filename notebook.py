'''
DESCRIPTION:
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
'''




''' 
1. Verify inputs
2.Create a counter starting in 1
3.Create a new empty list.
4.if the counter equals to the first element in the array, counter sums +1
5. if the counter not equals to the first element in the array, counter sums +1 and append the counter in the new empty list
6. Compare if the length of new empty list it's equals to k value
7. if True, return the last element of new empty list 
8. if False, compare counter with the array and repeat the process.

'''
'''
pseudocode
new_list=[]
array =[1 , 2 , 4, 5, 6]
^
k = 1

counter= 1,2,3,4,5,6,7,8,9,10
iterate by elements in array
1.- 1 from counter == 1 in array : True 
        counter == array[0]
    2 from counter == 2 in array: True
    counter ==array[1]
    3 from counter == 3 in array: False
        counter ==array[2]
    4 from counter == 4 in array: True
    5 from counter == 5 in array: True
    6 from counter == 6 in array: True
    7 from counter == 7 in array: False
    8 from counter == 8 in array: False
    9 from counter == 9 in array: False
    
    
2. increase counter

3. if false new_list.append(counter)
new_list=[3]
compare if leng(new_list) is equals to k
leng(new_list): 1 == 1 is True, return: new_list[-1]
leng(new_list): 2 == 2 is True, return: new_list[-1]
leng(new_list): 3 == 4 is False, continue
leng(new_list): 4 == 4 is True, return: new_list[-1]

4. increase counter

'''


numbers =[1, 2, 4, 5, 6]
k = 3

def kth_missing_positive_number(numbers, k):
    counter = 1
    indx=0
    new_list= []
    if k<numbers[0]:
        return k
    
        
    while len(new_list)<k:
        if indx < len(numbers) and counter == numbers[indx]:
            counter+=1
            indx+=1
        elif numbers[-1]<k:
            return (new_list[-1]+(k-len(new_list)))
        else:
            new_list.append(counter)
            counter+=1
            if len(new_list)==k:
                return new_list[-1]
        
        

print (kth_missing_positive_number(numbers, k))





'''
Pseudo Code

if k < arr[0]
    return k
Set index to 0
while index < len(arr) - 1
    current_missing = arr[index + 1] - arr[index] - 1
    if k <= current_missing
        return arr[index] + k
    k = k - current_missing
return the last element of the list plus the remaining value of k.
array =[1 , 2 , 4, 5, 6]
k = 2
expected =8

2<1
index = 4
while 4<4
    current_missing = 6-5-1==0
    if 2<=0
        return arr[index] + k
    k =2-0

return 6+2=8

'''