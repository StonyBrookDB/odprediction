# odprediction
## Feature Matrix Construction
This folder includes that files for feature matrix construction from raw data.\
The content for each file used in the code:\
e2p: mapping from encounter id to patient id\
position: mapping from encounter id to the position of the encounter in the patient's feature matrix\
opce: clinical evnets information for OD patients\
opdx: diagnosis information for OD patients\
oplab: lab tests information for OD patients\
opmed: medications information for OD patients\
opdemo: demographics for OD patients\
comce: clinical evnets information for negative patients\
comdx: diagnosis information for negative patients\
comlab: lab tests information for negative patients\
commed: medications information for negative patients\
comdemo: demographics for negative patients\
labdict: mapping to position of lab test in feature matrix\
cedict: mapping to position of clinical event in feature matrix\
dxdict: mapping to position of diagnosis in feature matrix\
meddict: mapping to position of medication in feature matrix\



## Prediction
This folder includes the files of training and testing the predictive model.


##ICD Codes
This file includes the ICD-9 and ICD-10 codes used in the project to identify Opioid Use Disorder, Opioid Poisoing and Cancer.
