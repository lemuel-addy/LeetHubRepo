class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        for i in range(0,len(moves)):
            if moves[i] == "R":
                pos[1]+=1
            if moves[i] == "L":
                pos[1]-=1
            if moves[i] == "U":
                pos[0]+=1
            if moves[i] == "D":
                pos[0] -= 1
        if pos == [0,0]:
            return True
        else:
            return False
