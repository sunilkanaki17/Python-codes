class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=[]
        add=0
        for i in range(len(digits)):
            add +=(digits[i] * (pow(10,len(digits)-i-1)))
        add+=1
        add=str(add)
        for i in add:
            result.append(int(i)) 
        return result
        