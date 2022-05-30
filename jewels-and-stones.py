'''
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels =  "Aa", stones = "aAAbbbb"
Output: 3

Create tracking map for stones. 
    -Iterate trhough stones.
Save the key will character and my value will be the coincidences

Iterate jewels 
i will save (creating a new variable) the value of the key(character that I'm iterating)

my_stones = {"a":1, "A":2, b:4}

              ^
jewels =  "Aa"
            ^
my_counter=2

my_counter=2+1 .:. 3


'''

global_jewels =  "z" 
global_stones = "ZZ"
def get_my_jewels(jewels:str, stones:str) -> int:
    my_stones={}
    counter=0
    for char in stones:
        if char in my_stones:
            my_stones[char]+=1
        else:
            my_stones[char]=1
    
    for jewel in jewels:
        if jewel in my_stones:
            counter += my_stones[jewel]
        
    return counter

print (get_my_jewels(global_jewels, global_stones))

"""
jewels =  "Aa" 
stones = "aAAbbbb"
             ^
my_stones={a:1, A:2, b:4}
^
counter=0
char=a, A, A, b, b, b, b 

jewel: A, a
counter=2+1.:.3

Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0

my_stones={Z:2}

jewels = "aA"
           ^                        
stones = "abbbbAA"
                ^
counter = 3

"""

'''
Runtime: 44 ms
Memory Usage: 13.9 MB
Time complexity
O(n+m)where n is le length fo jewels and m is the length of the stones
O(n) where n is the space that the dictionary uses
See details here --> https://leetcode.com/submissions/detail/708630012/
'''