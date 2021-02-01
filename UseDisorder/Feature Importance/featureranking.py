

## To find the threshold to get the best f1 score

def bestf(testy,predy):
    f1s=[]
    for i in xrange(1,100):
        j=i/100.0
        pren=map(lambda x:rod(x,j),predy)
        f1s.append([f1_score(testy,pren),precision_score(testy,pren),recall_score(testy,pren),i])
    return max(f1s)


def rod(a,b):
    if a>b:
        return 1
    else:
        return 0


## the variable model can be replaced by other predictive model such as lstm, dnn,random forest, decision tree
predy=model.predict(testx)
fscore=bestf(testy,predy)

fdecreases=[]

for i in range(testx.shape[i]):
    testc=np.copy(testx)
    np.random.shuffle(testc[:,:,i])
    predyi=model.predict(testc)
    fscorei=bestf(testy,predyi)[0]
    fdecreases.append([fscore-fscorei,i])

fdecreases.sort(reverese=True)

## print the top 50 important features score and index
print fdecreases[:50]
