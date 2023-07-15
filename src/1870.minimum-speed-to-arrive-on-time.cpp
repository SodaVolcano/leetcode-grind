/*
 * @lc app=leetcode id=1870 lang=cpp
 *
 * [1870] Minimum Speed to Arrive on Time
 */

// @lc code=start
#include <cmath>
#include <numeric>
using namespace std;

class Solution {
   public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        int left = 0;
        int right = pow(10, 7);
        int minSpeed = right;
        bool changed = false;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (mid == 0) break;

            if (travelTime(dist, mid) <= hour) {
                if (mid <= minSpeed) {
                    minSpeed = mid;
                    changed = true;
                }
                right = mid - 1;
            } else
                left = mid + 1;
        }
        return changed ? minSpeed : -1;
    }

    double travelTime(vector<int>& dist, int speed) {
        // return sum: ceil ( dict[n] / speed )
        double time = 0;
        for (int i = 0; i < dist.size(); i++) {
            double temp =
                static_cast<double>(dist[i]) / static_cast<double>(speed);
            if (i != dist.size() - 1)
                temp = ceil(temp);
            else
                temp = ceil(temp * 100) / 100;
            time += temp;
        }
        return round(time * 100) / 100;
    }
};
// @lc code=end
