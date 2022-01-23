class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        number_to_add=1
        numbers=[]
        for i in range(1,9):
            number_to_add = number_to_add*10+1+i
            numbers.append(number_to_add)

        answer=[]
        number_to_add=11
        for i in range(9):
            for j in range(8-i):
                if numbers[i] > high: return answer
                if numbers[i]>= low:
                    answer.append(numbers[i])   
                numbers[i]+=number_to_add
            number_to_add = number_to_add*10+1

        return answer
