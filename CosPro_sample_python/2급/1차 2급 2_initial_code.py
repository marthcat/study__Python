#You may use import as below.
#import math

def solution(price, grade):
    #Write code here.
    answer = 0
    # if grade == "S":
    #     answer = round(price * 0.95)
    # elif grade == "G":
    #     answer = round(price * 0.90)
    # elif grade == "V":
    #     answer = round(price * 0.85)
    # else:
    #     answer = grade
    gradeSale = { "S":0.95, "G":0.90, "V":0.85 }
    if grade in list(gradeSale.keys()) :
        answer = int(price * gradeSale[grade]) 
    else:
        answer = price

    return answer

#The following is code to output testcase.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")