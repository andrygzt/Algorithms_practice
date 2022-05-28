'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
'''

'''
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

'''

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]


disallowed_characters = "._!:""'';?,"
for character in disallowed_characters:
    paragraph = paragraph.replace(character, " ")


paragraph= paragraph.lower()
paragraph= paragraph.split()
print (paragraph)

if banned == []:
    print(paragraph[0])
            
my_dict={}
for words in paragraph:
    if words in my_dict:
        my_dict[words]+=1
    else:
        my_dict[words]=1
        
for words in banned:
    if words in my_dict: 
        del my_dict[words]
        
most=max(my_dict, key=my_dict.get)
print(most)
        
        

'''
My first int
Runtime: 27 ms
Memory Usage: 14 MB
Time complexity
O(5n+m).:.O(n+m)
See details here --> https://leetcode.com/submissions/detail/708630012/
'''