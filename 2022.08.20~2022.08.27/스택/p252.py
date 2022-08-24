# Time limit
def dailyTemperatures(temperatures):
        result = []
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    day = j - i
                    result.append(day)
                    break
                if j == len(temperatures) - 1:
                    result.append(0)
        
        result.append(0)
        

temperatures = [73,74,75,71,69,72,76,73]
dailyTemperatures(temperatures)

# 
