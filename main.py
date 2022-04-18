#######################################################################################################################
# This class is based on the Leetcode problem "Binary Search"
# This was a learning experience for me, for sure. I had never really dealt with algorithms before, since my
# background is not in CS. So, after doing some digging, and seeing how the algorithm works, I decided to write
# the code in my own terms. To reinforce understanding, I will comment each line to establish what the code is doing,
# that way I'm not just copy/pasting code. Shoutout to mageshyt on Leetcode for the awesome explanation and
# breakdown for the methodology!
#######################################################################################################################

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0 # define the left index. We set it to 0 because "0" is the first index in a list/array
        right_index = len(nums) - 1 # defines the right index. We subtract one from len(nums) to get an index that
                                    # exists, since we start counting from 0

        while left_index <= right_index: # Set up a while loop to continuously check conditions
            middle_index = (left_index + right_index) // 2 # This is to separate the array from the middle
            if nums[middle_index] == target:
                return middle_index # Immediately outputs the target if the middle index just so happens to be the target
            elif nums[middle_index] < target:
                left_index = middle_index + 1 # Part of the loop, continuously checks the "left half" for the target,
                                              # splitting the new index until it finds what it is looking for
            else:
                right_index = middle_index - 1 # If it can't find the target in the left index, the program will
                                               # immediately start checking for the target in the "right half" we created.
        return - 1 # If the target does not exist, returns -1, and ends the process. 