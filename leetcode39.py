class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = [[] for _ in range(target+1)]
        
        for num in sorted(candidates):
            if num>target: break
            for i in range(num,target+1):
                if i==num: arr[num].append([num])
                elif len(arr[i-num])>0:
                    for case in arr[i-num]:
                        arr[i].append(case+[num])
        return arr[target]
