def isValidSubsequence(array, sequence):
    # Write your code here.
    ## Using While Loop
    # i, j = 0, 0
    # while i < len(array):
    #     if array[i] == sequence[j]:
    #         i += 1
    #         j += 1
    #         if j==len(sequence):
    #             break
    #     else:
    #         i += 1
    # print(i,j)
    # if j != len(sequence):
    #     return False
    # else:
    #     return True

    ## Using For Loop
    j=0
    for i in range(len(array)):
        if array[i]==sequence[j]:
            j+=1
        if j==len(sequence):
            return True
    return False


ans=isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[22, 25, 9])
print(ans)