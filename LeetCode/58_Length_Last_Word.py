from typing import List
class Solution:
    def lengthOfLastWord(self, s : str) -> int:
        words = s.strip().split()   
        # strip(): Removes all leading and trailing spaces
        # split(): Splits the words in the string by whitespaces into a list
        print(words)
        return len(words[-1])   # Returns of the length of the last element in the list
    
    def lengthOfLastWord_alternate(self, s : str) -> int:
        
        # Skip the trailing spaces - blank characters at the end of the string
        idx = len(s) - 1        # This is the last index in the string which might be a space - idx is initialized to this value
        while idx >= 0 and s[idx] == " ":
            idx = idx - 1       # At this stage, when the control comes out of the while loop, idx =  last non-space character in the str
        
        #Count the characters in the last word:
        length = 0
        while idx > 0 and s[idx] != " ":
            length += 1
            idx -= 1
        return length
            
        
s = Solution()
print(s.lengthOfLastWord_alternate("   fly me   to   the moon  "))