class Solution:
    def romanToInt(self, s: str) -> int:
        Symbol = {'I':1 , 'V' :5, 'X' :10 , 'L' :50 ,'C' :100 , 'D' :500 , 'M' :1000, 'XC':90,'XL':40,'IV':4,'IX':9,'CD':400,'CM':900 , '0':0}
        
        u = len(s)
        array = list(s)
        
        
        for i in range(u-1):

            if array[i]=='I' and array[i+1]=='V':
                array[i] = 'IV'
                array[i+1] = '0'
            elif array[i]=='I' and array[i+1]=='X':
                array[i] = 'IX'
                array[i+1] = '0'
            elif array[i]=='X' and array[i+1]=='L':
                array[i] = 'XL'
                array[i+1] = '0'
            elif array[i]=='X' and array[i+1]=='C':
                array[i] = 'XC'
                array[i+1] = '0'
            elif array[i]=='C' and array[i+1]=='D':
                array[i] = 'CD'
                array[i+1] = '0'
            elif array[i]=='C' and array[i+1]=='M':
                array[i] = 'CM'
                array[i+1] = '0'
                
        tong = 0
        for i in range(u):
            
            tong=tong+Symbol[array[i]]
         
        return tong
