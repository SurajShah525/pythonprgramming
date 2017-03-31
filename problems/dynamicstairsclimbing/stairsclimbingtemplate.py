"""
https://leetcode.com/articles/climbing-stairs/#approach-3-dynamic-programming-accepted
Reference Java solution to turn to python - comparison understanding
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}
"""
##Start here





if __name__=="__main__":
    val = Solution().climbStairs(10)
    print val
