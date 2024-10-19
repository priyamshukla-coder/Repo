
def minSubsetSumDifference(arr, n):
    # Calculate the total sum of the array elements.
    totSum = sum(arr)

    # Initialize a DP table to store subset sum information.
    dp = [[False for i in range(totSum + 1)] for j in range(n)]

    # Initialize the base cases for the DP table.
    for i in range(n):
        dp[i][0] = True

    # Handle the base case for the first element in the array.
    if arr[0] <= totSum:
        dp[0][arr[0]] = True

    # Fill in the DP table using dynamic programming.
    for ind in range(1, n):
        for target in range(1, totSum + 1):
            # If the current element is not taken, the result is the same as the previous row.
            notTaken = dp[ind - 1][target]

            # If the current element is taken, subtract its value from the target and check the previous row.
            taken = False
            if arr[ind] <= target:
                taken = dp[ind - 1][target - arr[ind]]

            # Update the DP table with the result of taking or not taking the current element.
            dp[ind][target] = notTaken or taken

    # Initialize a variable to track the minimum absolute difference.
    mini = int(1e9)

    # Iterate through all possible sums.
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            # Calculate the difference between the current sum and the complement sum.
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    return mini

def main():
    arr = [1, 2, 3, 4]
    n = len(arr)

    # Find and print the minimum absolute difference between two subsets.
    print("The minimum absolute difference is:", minSubsetSumDifference(arr, n))

if __name__ == '__main__':
    main()

