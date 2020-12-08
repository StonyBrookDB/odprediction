
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

rfc=RandomForestClassifier()
rfc.fit(trainx.reshape(trainx.shape[0],trainx.shape[1]*trainx.shape[2]),trainy)
predrfc=rfc.predict(testx.reshape(testx.shape[0],testx.shape[1]*testx.shape[2]))

dtc=DecisionTreeClassifier()
dtc.fit(trainx.reshape(trainx.shape[0],trainx.shape[1]*trainx.shape[2],trainy))
preddtc=dtc.predict(testx.reshape(testx.shape[0],testx.shape[1]*testx.shape[2]))


lr=LogisticRegression()
lr.fit(trainx.reshape(trainx.shape[0],trainx.shape[1]*trainx.shape[2],trainy))
predlr=lr.predict(testx.reshape(testx.shape[0],testx.shape[1]*testx.shape[2]))
