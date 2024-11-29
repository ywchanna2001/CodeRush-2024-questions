class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        possible_strings = set()
        
        # First case: No extra typing - the word is exactly as intended
        possible_strings.add(word)
        
        # Second case: One character might have been typed multiple times
        # For each position where we see repeated characters
        i = 0
        while i < n:
            # Count how many times the current character repeats
            j = i + 1
            while j < n and word[j] == word[i]:
                j += 1
                
            # If we found repeated characters
            if j - i > 1:
                # Try each possible length of repetition from 1 to actual count
                # This represents Alice actually intending to type fewer characters
                for k in range(i + 1, j):
                    new_string = word[:k] + word[j:]
                    possible_strings.add(new_string)
                    
            i = j
        
        return len(possible_strings)

# Create an instance of the Solution class
solution = Solution()

# Get user input
word = input()

# Call the function and print the result
output = solution.possibleStringCount(word)
print(output)
