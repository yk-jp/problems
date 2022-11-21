"""
  note -> I set the condition for while loop wrong first and I needed to consider retaining the maximum score.
  submission -> https://leetcode.com/problems/bag-of-tokens/submissions/847642581/
"""

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # we want to play token face up with the minimum and play token face down with the maximum.
        tokens.sort() # n log(n) 

        l, r = 0, len(tokens) - 1

        max_score = 0
        score = 0

        while l <= r: # o(n)
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                max_score = max(max_score, score) # update max_score if score overnumbered current max_score
                l += 1
            elif score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else: 
                break

        return max_score

"""
  time complexity: O(nlog(n)) 
    - n: the length of the list. 
    - Python's sort function has a time complexity of O(n log (n)). Therefore, total time complexity should be o(nlog(n))

  space complexity: O(n)
    - Python's sort function needs extra memory of n.
"""