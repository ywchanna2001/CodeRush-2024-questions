from typing import List

class Solution:
    def minOperationsToMakeMediantargetTemp(self, sensorReadings: List[int], targetTemp: int) -> int:
        sensorReadings.sort()
        n = len(sensorReadings)
        mid = n // 2
        ops = 0
        # If the median is greater than or equal to targetTemp
        if sensorReadings [mid] >= targetTemp:
            for i in range(mid, -1, -1):
                if sensorReadings [i] > targetTemp:
                    ops += sensorReadings[i] - targetTemp	
                else:
                    break
        # If the median is less than targetTemp
        else:
            for i in range(mid, n):
                if sensorReadings[i] < targetTemp:
                    ops += targetTemp - sensorReadings[i]
                else:
                    break
        return ops

#Input handling
sensor_reading = list(map(int, input().split()))
target_temp = int(input())

solution = Solution()

#Call the funcion and print the result
result = solution.minOperationsToMakeMediantargetTemp(sensor_reading,target_temp)
print(result)

