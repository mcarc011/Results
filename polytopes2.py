#%%
from re import A
from xml.etree.ElementTree import SubElement
import numpy as np
import itertools
from time import time

def Traceless(M):
    M2 = M.copy()
    for i in range(len(M2)):
        M2[i,i] = 0
    return M2

def Triality(X,F,p):
    ProjV = np.zeros(len(X))
    ProjM = np.meshgrid(ProjV,ProjV)[0]
    ProjM[p,p] = 1
    Xn = X - np.dot(X,ProjM) + np.transpose(np.dot(X,ProjM)) - np.transpose(np.dot(np.transpose(X),ProjM))
    Xn += np.dot(X,np.dot(ProjM,X)) + np.dot(F,ProjM)
    Fn = np.dot(np.transpose(X),ProjM) + np.dot(X,np.dot(ProjM,F)) - np.dot(F,ProjM)
    Fn = F + (Traceless(Fn) +np.transpose(Fn))


    for i in range(len(X)):
        for j in range(len(X)):
            pairs = min([Xn[i,j],Fn[i,j]])
            Xn[i,j] -= pairs
            Fn[i,j] -= pairs
            if i!=j:
                Fn[j,i] -=pairs
    return np.array(Xn),np.array(Fn)

def Swap(M:np.array, t:tuple):
	Mt = M.copy()
	Mt[t[0]],Mt[t[1]] = M[t[1]],M[t[0]]
	Mt = np.transpose(Mt)
	Mc = Mt.copy()
	Mt[t[0]], Mt[t[1]] = Mc[t[1]], Mc[t[0]]
	return np.transpose(Mt)

def TupFind(L):
	maps = []
	n = 0
	while n!=len(L)-1:
		mt = []
		for m in range(n,len(L)):
			if n!=m:
				mt += [(n,m)]
		if mt != []:
			maps += [mt]
		n+=1
	return list(itertools.product(*maps))

def FindPhases(X: np.array,F: np.array) -> np.array:
    DualityWeb = [(X,F)]
    TrialityMaps = []

    def equivalent(X1, F1, X2, F2,counter=False):
        if np.array_equal(X1,X2) and np.array_equal(F1,F2):
            return True

        ANodes = [(sorted(X1[node]),sorted(np.transpose(X1)[node]),sorted(F1[node])) for node in range(len(X1))]
        BNodes = [(sorted(X2[node]),sorted(np.transpose(X2)[node]),sorted(F2[node])) for node in range(len(X1))]

        try:
            Xt, Ft = X1.copy(), F1.copy()
            for i in range(len(X1)):
                if BNodes[i] != ANodes[i]:
                    b = BNodes[i]
                    j = ANodes[i:].index(b)+i
                    Xt,Ft = Swap(Xt,(j,i)),Swap(Ft,(j,i))
                    ANodes = [(sorted(Xt[node]),sorted(np.transpose(Xt)[node]),sorted(Ft[node])) for node in range(len(X1))]
        except:
            return False 

        if np.array_equal(Xt,X2) and np.array_equal(Ft,F2):
            return True
        
        #final test
        Aswaps = {}
        ANodes = [(sorted(Xt[node]),sorted(np.transpose(Xt)[node]),sorted(Ft[node])) for node in range(len(X1))]
        for i,a in enumerate(ANodes):
            for j,b in enumerate(ANodes):
                if a==b and i!=j:
                    if str(a) not in Aswaps:
                        Aswaps[str(a)] = [i,i,j]
                    if i not in Aswaps[str(a)]:
                        Aswaps[str(a)] += [i]
                    if j not in Aswaps[str(a)]:
                        Aswaps[str(a)] += [j]

        temptylist = [val for val in Aswaps.values()]
        temptlist = [] 
        for tem in temptylist:
            mapto = TupFind(np.array(tem))
            tp = [] 
            for mapper in mapto:
                tp += [[[tem[m[0]],tem[m[1]]] for m in mapper]]
            temptlist += [tp]

        for tlist in itertools.product(*temptlist):
            Xp,Fp = Xt.copy(),Ft.copy()
            for tlistswap in itertools.permutations(tlist):
                for titer in tlistswap: 
                    for step in titer:
                        t = (step[0],step[1])
                        Xp,Fp = Swap(Xp,t),Swap(Fp,t)
                        if np.array_equal(Xp,X2) and np.array_equal(Fp,F2):
                            return True
        return False

    def inweb(xt, ft, dweb, findn=False):
        for d,phase in enumerate(dweb):
            e1 = equivalent(xt,ft,phase[0],phase[1])
            e2 = equivalent(np.transpose(xt),ft,phase[0],phase[1])
            if e1 or e2:# or e3 or e4:
                if findn:
                    return d
                return True
        return False
    
    def anomalies(x1,f1):
        for i in range(len(x1)):
            chirals = np.sum(x1[i]) + np.sum(np.transpose(x1)[i])
            fermis = np.sum(f1[i])
            if chirals - fermis !=2:
                return True
        return False

    for phase in DualityWeb:
        Xt,Ft = phase[0].copy(),phase[1].copy()

        print('Dweb Length: '+str(len(DualityWeb)),end="\r")

        if len(DualityWeb)>100:
            break
        
        # if anomalies(Xt,Ft):
        #     print('Anomaly Found')
        #     break

        for n in range(len(Xt)):
            if np.sum(np.transpose(Xt)[n])==2 and np.trace(np.transpose(Xt))==0:
                Xi,Fi = Triality(Xt, Ft, n)
                if np.trace(Xi)==0 and np.trace(Fi)==0:
                    TrialityMaps += [[(Xt,Ft),(Xi,Fi),n+1]]
                    if not inweb(Xi,Fi,DualityWeb):
                        DualityWeb += [(Xi,Fi)]
                    
            if np.sum(Xt[n])==2 and np.trace(Xt)==0:
                Xi,Fi = Triality(Xt, Ft,n)
                if np.trace(Xi)==0 and np.trace(Fi)==0:
                    Xi,Fi = Triality(Xi, Fi, n)
                    if np.trace(Xi)==0 and np.trace(Fi)==0:
                        TrialityMaps += [[(Xt,Ft),(Xi,Fi),-(n+1)]]
                        if not inweb(Xi,Fi,DualityWeb):
                            DualityWeb += [(Xi,Fi)]    
        

    TrialityTuples = [(inweb(t[0][0],t[0][1],DualityWeb,findn=True),
        inweb(t[1][0],t[1][1],DualityWeb,findn=True)) for t in TrialityMaps]
    print('\n'+str(len(DualityWeb))+' Phase\n')
    return DualityWeb,TrialityMaps,TrialityTuples



