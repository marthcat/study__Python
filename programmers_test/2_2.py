def timeRangeToMinit(fromTime, toTime):
  fromTimeS = list(map(int, fromTime.split(":")))
  toTimeS = list(map(int, toTime.split(":")))

  return  toTimeS[0]*60 + toTimeS[1] - fromTimeS[0] * 60 - fromTimeS[1] 



def solution(fees, records):
    answer = []
    
    records2 = [rec.split(" ") for rec in  records]    
    
    for i in range(len(records2)) :
        if records2[i][2] == "OUT":
            for j in range(i) :
                if records2[j][2] == "IN" and records2[i][1] == records2[j][1]:
                    iMinitRange = timeRangeToMinit(records2[j][0],records2[i][0])
                    if iMinitRange < fees[0] :
                        answer.append(fees[1])
                        continue
                    iMinitRange -= fees[0]
                    answer.append((iMinitRange // fees[2]+1)*fees[3] + fees[0]) 
    print (answer)

  

    
    return answer

solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
