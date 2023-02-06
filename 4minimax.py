import math
import random
def minimax(currentdepth,nodeIndex,maxTurn,score,farDepth):
    if(currentdepth==farDepth):
        return score[nodeIndex]
    if(maxTurn):
        return max(minimax(currentdepth+1,nodeIndex*2,False,score,farDepth),
                   minimax(currentdepth+1,nodeIndex*2+1,False,score,farDepth))
    else:return min(minimax(currentdepth+1,nodeIndex*2,False,score,farDepth),
                    minimax(currentdepth+1,nodeIndex*2+1,False,score,farDepth))
score=random.sample(range(1,50),4)
print(str(score))
treeDepth=math.log(len(score),2)
print("The optimal value is:",end=" ")
print(minimax(0,0,True,score,treeDepth))