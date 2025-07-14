from typing import List

# Time Complexity: O(n) - As the first for loop is only iterating on the first word and we are using the same idx to iterate on each char of all the remaining words
class Solution:
    # def longestcommonprefix(self, strs:List[str]) -> str:

    #     if not strs:                    # If there is not a input string, return a blank string as longest common prefix
    #         return ""
        
    #     prefix = ""
    #     # Start with iterating over just the first word to find the common string
    #     # We will iterate upto range(len(strs[0])) as the common string could be the entire first word
    #     for idx in range(len(strs[0])):
    #         current_char = strs[0][idx]
    #         for word in strs[1:]:
    #             if idx >= len(word) or word[idx] != current_char:
    #                 return prefix
    #         # Add the new word[idx] after all characters match at this index
    #         prefix += current_char
    #     return prefix
    
# Time Complexity: O(n) - Using startswith function:
    def longestcommonprefix(self, strs):
        if not strs:
            return ""
        
        prefix =strs[0]                     # We are assigning the complete first word to prefix 
        for word in strs[1:]:               # Now we iterate from 1 idx to end on strs
            # Shrink prefix until it matches the start of word
            while not word.startswith(prefix):
                prefix = prefix[:-1]        # prefix[:-1] - Complete string but the last element
                if not prefix:
                    return ""               # If there is no common prefix, return blank - This will happen when the prefix string is shrinked all the way to empty string
# 1. Prefix = 'flower', Start with strs[1] = flow, flow does not start with prefix, prefix = 'flowe' -> still flow does not start with prefix, prefix = 'flow' -> now flow starts with flow
# 2. Prefix = 'flow' , move to strs[2] = flight, flight does not start with prefix, prefix = 'flo' -> still flight does not start with prefix, prefix = 'fl' -> now flight starts with fl
# Jump out of while as while not condition is not satisfied anymore for word = strs[2], with prefix = 'fl'
            

obj = Solution()
print(obj.longestcommonprefix(["flower","flow","flight"]))


