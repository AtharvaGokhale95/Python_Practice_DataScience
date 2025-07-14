from typing import List

# Time Complexity: O(n) - As the first for loop is only iterating on the first word and we are using the same idx to iterate on each char of all the remaining words
class Solution:
    def longestcommonprefix(self, strs:List[str]) -> str:

        if not strs:                    # If there is not a input string, return a blank string as longest common prefix
            return ""
        
        prefix = ""
        # Start with iterating over just the first word to find the common string
        # We will iterate upto range(len(strs[0])) as the common string could be the entire first word
        for idx in range(len(strs[0])):
            current_char = strs[0][idx]
            for word in strs[1:]:
                if idx >= len(word) or word[idx] != current_char:
                    return prefix
            # Add the new word[idx] after all characters match at this index
            prefix += current_char
        return prefix

obj = Solution()
print(obj.longestcommonprefix(["flower","flow","flight"]))

# Time Complexity: O(n) - Using single for loop:
