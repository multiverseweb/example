class Solution(object):
    def countOfAtoms(self, formula):
        freq=[]
        atoms=[]
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums="23456789"
        multiplier=1
        flag=False
        if "(" in formula:
            opening=formula.index("(")
            closing=formula.index(")")
            flag=True
        
        for i in range(len(formula)):
            count=1
            multiplier=1
            if flag==True:
                if opening<i<closing:
                    multiplier=int(formula[closing+1])
            if formula[i] in alphabet:
                atoms.append(formula[i])
                freq.append(count*multiplier)
            elif formula[i] in alphabet.lower():
                atoms[-1]=atoms[-1]+formula[i]
            elif formula[i] in nums:
                count=formula[i]
                freq[-1]=int(count*multiplier)
            else:
                pass
        return atoms,freq
        
        
#paste testCase here
formula = "K4(ON(SO3)2)2"
obj = Solution()
print(obj.countOfAtoms(formula))