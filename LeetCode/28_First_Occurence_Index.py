# This can be done with .find() method
# In built method
def first_occurrence(needle:str, haystack:str)->int:
    return haystack.find(needle)

print(first_occurrence("sad", "sadbutsad"))

class solution:
    def first_occurrence_idx(self, needle:str, haystack:str) -> int:
        h, n = len(haystack), len(needle)
        if n == 0:
            return -1
        
        for i in range(0, h - n + 1):
            if haystack[i : i + n] == needle:
                return i
        return -1


s = solution()
print(s.first_occurrence_idx("sad", "sabbutsad"))
                
            