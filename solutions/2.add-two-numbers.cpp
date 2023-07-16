/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <iostream>
using namespace std;

class Solution {
   public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        bool carry = false;
        ListNode *ans = new ListNode();
        ListNode *c1 = l1;
        ListNode *c2 = l2;
        ListNode *c3 = ans;
        while (c1 != NULL || c2 != NULL) {
            c3->val = c1->val + c2->val;

            if (carry) {
                carry = false;
                ++c3->val;
            }
            if (c3->val >= 10) {
                carry = true;
                c3->val -= 10;
            }

            c1 = c1->next;
            c2 = c2->next;

            if (c1 != NULL || c2 != NULL) {
                c3->next = new ListNode();
                c3 = c3->next;
            }
            if (c1 == NULL && c2 != NULL) {
                c1 = new ListNode(0);
            }
            if (c2 == NULL && c1 != NULL) {
                c2 = new ListNode(0);
            }
        }
        if (carry) {
            c3->next = new ListNode(1);
        }

        return ans;
    }
};
// @lc code=end
