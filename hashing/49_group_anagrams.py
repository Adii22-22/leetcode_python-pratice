# LeetCode 49 - Group Anagrams
# https://leetcode.com/problems/group-anagrams/
#
# Approach:
# Use a hash map to group words based on a common key.
# For each word, generate a key by sorting its characters.
# All anagrams produce the same sorted key.
# Store words in a dictionary where the key maps to a list of anagrams.
# Finally, return all grouped values from the dictionary.
#
# Time Complexity: O(n * k log k), where n is the number of words
# and k is the maximum length of a word.
# Space Complexity: O(n * k)
