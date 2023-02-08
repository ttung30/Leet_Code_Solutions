class Solution:
 
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        for i in range(len(strs)):
            strs[i]=list(strs[i])
        t=[]      
        u=strs[0]
        for i in range(len(strs)-1):
            if len(u)<len(strs[i+1]):
                z=len(u)
            else:
                z=len(strs[i+1])
            
            for y in range(z):
                
                if u[y] ==  strs[i+1][y]:
                    t.append(strs[i+1][y])
                else: 
                    break
            u=t
            t=[]
        str1 = ""
 
    
        for ele in u:
            str1 += ele
        return str1
