def solution(n, lost, reserve):
    answer = 0
    # dictA = {i:True for i in range(1, n+1) }
    # for i in lost :
    #     dictA[i] = False
    
    dictA = {}
    for i in range(n) :
        if i+1 in lost : 
            dictA[i+1] = False
        else : 
            dictA[i+1] = True
        
    for j in reserve :
        if j > 1 and dictA[j-1] == False :
            dictA[j-1] = True
        elif j < n and dictA[j+1] == False :
            dictA[j+1] = True
    
    answer = list(dictA.values()).count(True)
    
    
    return answer

print (solution(2, [1], [2]) )