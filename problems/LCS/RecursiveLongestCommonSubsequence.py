import sys
import os
import json
from ast import literal_eval #sample usecase - converts a string to dict

"""
http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/
"""


def lcs(X, Y, m, n):
 
    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1);
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

if __name__=="__main__":
    # Driver program to test the above function
    X = "AGGTAB"
    Y = "GXTXAYB"
    print "Length of LCS is ", lcs(X , Y, len(X), len(Y))
