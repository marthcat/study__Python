def solution(n, k):
    i = 0 
    while True :
        i += 1
        if n < k**i :
            i -= 1
            break

    calc = n
    kS = ""    
    while i>=0 :
        s = k**i
        kS += str(calc//s)
        calc = calc % s
        i -= 1        

    answer = 0 
    nums = kS.split("0")    
    for sNum in nums :
        if sNum == "" or sNum == "1":
            continue

        num = int(sNum)
        for ch in range(2, num+1) :
            if num % ch == 0 : 
                if num == ch : 
                    answer += 1
                break     

    return answer