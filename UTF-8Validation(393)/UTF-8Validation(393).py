"""
  note -> bit manipulation, bit masking
  submission -> https://leetcode.com/problems/utf-8-validation/submissions/847719561/
"""

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        num_of_byte = 0

        i = 0
        while i < len(data):
            num_of_byte = self.count_byte(data[i])
            
            if num_of_byte == 1 or num_of_byte > 4:
                return False
            if num_of_byte == 0: # start over
                i += 1
                continue
            
            num_of_byte -= 1
            i += 1
            while i < len(data):
                next_num_of_byte = self.count_byte(data[i]) 
                
                if next_num_of_byte != 1:
                    return False
                
                num_of_byte -= 1

                if num_of_byte == 0:
                    i += 1
                    break
    
                i+=1

        return num_of_byte == 0

    '''
    Bit masking to check if how many digit of 1 first 8 bits have 
    
    time Complexity of count_byte function
        - O(1)
        - the range of for loop is always 0 to 7, meaning that it is going to be constant in time complexity 
    '''
    
    def count_byte(self, num):
        count = 0

        for i in range(7, -1, -1): # 1 byte is 8 bits and it starts from 0 to 7
            if num & (1 << i):
                count += 1
            else:
                break
        
        return count
      
      
"""
  time complexity: O(n)
    - n: the length of list
    - Only one iteration is made to check all byte data. Therefore, Overall time complexity should be O(n)

  space complexity: O(1)
    - Extra memory is only for the variable to retain the count of byte
"""
