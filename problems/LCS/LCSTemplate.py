import sys
import os
import json
from ast import literal_eval #sample usecase - converts a string to dict


def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = 
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
#end of function lcs


if __name__=="__main__":
    # Driver program to test the above function
    X = "AGGTAB"
    Y = "GXTXAYB"
    print "Length of LCS is ", lcs(X, Y)
