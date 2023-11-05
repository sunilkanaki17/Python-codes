class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lst=[1]
        result=[]
        add=0
        mult=1
        for i in range(len(digits)-1):
            lst.append(lst[i]*10)
        lst.reverse()
        for i in range(len(digits)):
            mult = digits[i] * lst[i]
            add = add+mult
        add+=1
        op=str(add)
        for i in range(len(op)):
            result.append(int(op[i])) 
        return result
        