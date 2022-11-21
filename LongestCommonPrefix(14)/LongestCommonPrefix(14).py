"""
  Side note -> The zip function is not compatible with all languages. I solved it without the zip function.
  submission -> https://leetcode.com/problems/longest-common-prefix/submissions/847615183/
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # check if strs is not None or strs is not an empty list
        if not strs or len(strs) == 0:
            return ""

        # Find the string with the minimum length
        min_str_at = 0
        
        for i in range(len(strs)):  #(o(n))
            if len(strs[i]) < len(strs[min_str_at]):
                min_str_at = i 

        min_str = strs[min_str_at]
        common_prefix = ""

        for i in range(len(min_str)): # iterete through minimum string
            for j in range(len(strs)):
                if min_str[i] != strs[j][i]: # check if each char is matched with each other
                    return common_prefix

            common_prefix += min_str[i]

        return common_prefix
      
"""
  time complexity: O(n*m) -> n: the length of list, m: the total length of all string stored in list

  space complexity: O(1) -> extra memory should be used for storing the index data with the minimum length of string and common_prefix
"""
