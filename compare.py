import numpy as np
from numpy import linalg

class Comparsion(object):

    def __init__(self):
        pass
    
    def compare(self,a,b):
        pass

class MyComparsion(Comparsion):

    def __init__(self, model):
        super().__init__()
        self.model=model

    def compare(self,a,b):
        a_sum=np.zeros([100,1])
        b_sum=np.zeros([100,1])
        for i in a:
            try:
                a_sum+=np.reshape(self.model[i],[100,1])
            except Exception:
                pass
        for k in b:
            try:
                b_sum+=np.reshape(self.model[k],[100,1])
            except Exception:
                pass
        A=a_sum
        B=b_sum
        num = float(A.T.dot(B))
        denom = linalg.norm(A) * linalg.norm(B)  
        cos = num / denom
        sim = 0.5 + 0.5 * cos
        return sim
