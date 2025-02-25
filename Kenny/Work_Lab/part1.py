from typing import List  # Import List for type hinting

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []  # Initialize an empty list
        for i in range(2):  # Iterate twice to concatenate
            for num in nums:
                ans.append(num)  # Append each number twice
        return ans  # Return the concatenated list
    


class Solution2:
      
      def hasduplicateNums(slef, nums: List[int])-> bool:
          # sort list first 
          nums.sort()
          n = len(nums)
          # compare the nums next to eahc other and if they are the same return true 
          
          for  i in range(1, n-1):
            if nums[i] == nums[i + 1]:
                return True
          return False
      


class Solution3:
        
        def isAnagram(self, s: str, t: str) -> bool:   
            if sorted(s) == sorted(t):  # uses pythons sorted library function to return an array of each letter in the string and then comapres them. 
                return True
            return False
            
            
        
          





# Create an instance of Solution
sol = Solution()
sol2 = Solution2()
sol3 = Solution3()



# Solution 1


# Input list
a = [1]

# Call the function and print the result
print(f"solution 1: {sol.getConcatenation(a)}")  # Expected Output: [1, 1]


# Solution 2

b = [2,2,1]
c = [1,2,3,4]
print(f"solution 2: {sol2.hasduplicateNums(b)}")
print(sol2.hasduplicateNums(c))

# Solution 3
# this is a leet code for an anagram 

s = "racecar"
t = "carrace"

print(f"solution 3: {sol3.isAnagram(s,t)}")

