/*
 * @lc app=leetcode id=1190 lang=cpp
 *
 * [1190] Reverse Substrings Between Each Pair of Parentheses
 */

// @lc code=start
#include <iostream>

class Solution {
   public:
    string reverseParentheses(string s) {
        // for i in string, if see (, execute reverse parenthesis with this
        // index as start
        // reverse: find ")", and the start index, and return reversed string
        string ans = "";
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                string temp = reverseParenthesis(++i, s);
                ans += temp;
            } else {
                ans += s[i];
            }
        }
        return ans;
    }
    string reverseParenthesis(int &start, string s) {
        string revStr = "";
        while (start < s.length()) {
            if (s[start] == '(') {
                revStr += reverseParenthesis(++start, s);
            } else if (s[start] == ')') {
                reverse(revStr.begin(), revStr.end());
                return revStr;
            } else {
                revStr += s[start];
            }
            ++start;
        }
        return revStr;
    }
};
// @lc code=end
