class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
            if denominator == 0:
                return 
            if numerator == 0:
                return '0'
        
            ans = ""
            if numerator*denominator<0:        
                ans+="-"
                if numerator<0:
                    numerator *= -1
                    
                elif denominator<0:
                    denominator *= -1
                
                
            if numerator<0 and denominator<0:
                numerator *= -1
                denominator *= -1
            if numerator%denominator == 0:
                ans += str(numerator//denominator)
                return ans

            den = abs(denominator)
            num = abs(numerator)

            
            ans += str(num//denominator)
            
            ans += "."
            

            num_q = []
            while True:
                rem = num%den
                if rem == 0:
                    for val in num_q:
                        ans += str(val[-1])
                    break
                num = rem*10
                q = num//den
                if [num,q]not in num_q:
                    num_q.append([num,q])
                elif [num,q] in num_q:
                    ind = num_q.index([num,q])
                    for val in num_q[:ind]:
                        ans += str(val[-1])
                    
                    ans += "("
                    for val in num_q[ind:]:
                        ans+= str(val[-1])
                    ans += ")"
                    break 
            
            return ans



            
