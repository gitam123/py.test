import numpy as np
def gradientdescent(x,y):
    m_curr=0
    b_curr=0
    learningrate=0.0001
    iter=10
    n=len(x)
    for val in range(iter):
        y_pred=m_curr*x+b_curr
        cost=1/n*sum([val**2 for val in (y-y_pred)])
        md=-2/n*sum(x*(y-y_pred))
        bd=-2/n*sum(y-y_pred)
        m_curr=m_curr-learningrate*md
        b_curr=b_curr-learningrate*bd
        print("m{},b{},iteration{},cost{}".format(m_curr,b_curr,val,cost))
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])
gradientdescent(x,y)

        
