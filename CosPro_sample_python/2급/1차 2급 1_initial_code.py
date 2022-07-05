#You may use import as below.
#import math

from random import sample


def solution(shirt_size):
    ##Write code here.
    # samples = ["XS", "S", "M", "L", "XL", "XXL"]
    # answer = [0 for _ in range(len(samples))]

    # for sSize in shirt_size :
    #     if sSize == "XS":
    #         answer[0] += 1
    #     elif sSize == "S":
    #         answer[1] += 1
    #     elif sSize == "M":
    #         answer[2] += 1
    #     elif sSize == "L":
    #         answer[3] += 1
    #     elif sSize == "XL":
    #         answer[4] += 1
    #     elif sSize == "XXL":
    #         answer[5] += 1
    
    samples = {"XS":0, "S":0, "M":0, "L":0, "XL":0, "XXL":0}
    for i in shirt_size :
        samples[i] += 1
    answer = list(samples.values())

    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")