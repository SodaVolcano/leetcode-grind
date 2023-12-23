#
# @lc app=leetcode id=2125 lang=python3
#
# [2125] Number of Laser Beams in a Bank
#


# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        Just a multiplication problem with extra steps:
        - for each row, count the number of lasers
        - find next row with at least one laser and multiply with previous
        - set new row as next number to multiply with
        - if there's no next row or next row has no camera, return 0
        """
        n_beams = 0
        n_cameras = bank[0].count("1")
        for row in bank[1:]:
            n_cameras2 = row.count("1")
            if n_cameras2 != 0:
                n_beams += n_cameras * n_cameras2
                n_cameras = n_cameras2
        return n_beams


# @lc code=end
