#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """skipped maintaining output[]"""
        from collections import defaultdict

        output_map = defaultdict(list)
        for word in strs:
            feat = hash("".join(sorted(word)))
            output_map[feat].append(word)
        return list(output_map.values())

    def attempt_1(self, strs: List[str]) -> List[List[str]]:
        """
        group the anagram - their own list
        anagram: formed by rearranging letters of different word or phrase

        1. map word to one number: words with same character are mapped to same elem
            jsut use dict: key = feature_vector of char count for each word interpreted as str
        2. Map to output array
            maintain a dict of ascii_sum: array_idx
        """
        output_map = {}
        output = []
        for word in strs:
            feat = hash("".join(sorted(word)))
            if feat not in output_map.keys():
                output_map[feat] = len(output)
                output.append([word])
                continue

            output[output_map[feat]].append(word)
        return output


# @lc code=end
