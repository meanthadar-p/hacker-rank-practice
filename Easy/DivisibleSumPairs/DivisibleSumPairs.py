#
# Rank: EASY
# Score: 10/10
# HackerRank Link: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
#


def divisible_sum_pairs(n, k, ar):
    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                result += 1
    return result
