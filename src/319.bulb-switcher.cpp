/*
 * @lc app=leetcode id=319 lang=cpp
 *
 * [319] Bulb Switcher
 */

// @lc code=start
#include <cmath>

class Solution {
   public:
    int bulbSwitch(int n) { return static_cast<int>(floor(sqrt(n))); }
};
// @lc code=end
