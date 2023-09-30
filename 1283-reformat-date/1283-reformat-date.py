class Solution:
    def reformatDate(self, date: str) -> str:
        # dater = date.split(' ')
        # print(dater)
        # ans = ""
        # ans = ans+dater[2]+"-"
        # print(ans)
        # Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        # for i in range(0,len(Month)):
        #     if Month[i]==dater[1]:
        #         ans = ans+str(i+1)+"-"

        # # for i in range(1,len(Day)+1):
        # #     if i.equals(date[0]):
        # #         ans+i
        # ans = ans + dater[0][:-2] if len(dater[0])==4 else ans+"0"+dater[0][:1]
        
        # return ans

        months = { 
            "Jan": '01', 
            "Feb": '02', 
            "Mar": '03', 
            "Apr": '04', 
            "May": '05', 
            "Jun": '06', 
            "Jul": '07', 
            "Aug": '08', 
            "Sep": '09', 
            "Oct": '10', 
            "Nov": '11', 
            "Dec": '12'
        }

        day, month, year = date.split(' ')
        day = day[:2] if len(day) == 4 else '0' + day[:1]
        month = months[month]

        return year+"-"+month+"-"+day


