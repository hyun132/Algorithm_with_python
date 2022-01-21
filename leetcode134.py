class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=0
        answer=0
        
        cost_sum =0
        gas_sum=0
        
        for index in range(len(gas)):
            cost_sum += cost[index]
            gas_sum += gas[index]
            total += (gas[index]-cost[index])
            if total<0: 
                answer = index+1
                total = 0
                
        if cost_sum>gas_sum:return -1
        return answer
