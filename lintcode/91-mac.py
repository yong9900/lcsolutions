import sys

def MinAdjustmentCost( A, target):
    l = len(A)
    old_res= [sys.maxsize]*100
    for i in range(l):
        res  =[]*100
        for j in range(1,101):
            for k in range(1,101):
                if abs(j-k) <= target:
                    if old_res[j] < res[k]:
                        res[k] = old_res[j]
            
