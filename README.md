# odprediction
## Feature Selection
This folder includes that files for feature selection and preparation data needed for matrix construction.
## Feature Matrix Construction
This folder includes that files for feature matrix construction from raw data.\
The content for each file used in the code:\
e2p: mapping from encounter id to patient id\
icd9toicd10: mapping from icd 9 code to icd 10 code, based on the table at https://www.health.govt.nz/nz-health-statistics/data-references/mapping-tools/mapping-between-icd-10-and-icd-9 \
position: mapping from encounter id to the position of the encounter in the patient's feature matrix\
oudce: clinical evnets information for OD patients\
ouddx: diagnosis information for OD patients\
oudlab: lab tests information for OD patients\
oudmed: medications information for OD patients\
ouddemo: demographics for OD patients\
comce: clinical evnets information for negative patients\
comdx: diagnosis information for negative patients\
comlab: lab tests information for negative patients\
commed: medications information for negative patients\
comdemo: demographics for negative patients\
labdict: mapping to position of lab test in feature matrix\
cedict: mapping to position of clinical event in feature matrix\
dxdict: mapping to position of diagnosis in feature matrix\
meddict: mapping to position of medication in feature matrix\
racedict: mapping to position of race type in feature matrix



## Prediction
This folder includes the files of training and testing the predictive model.

## Feature Importance
Using the permutation method to get the features importances.

## ICD Codes
According codes are put in the doc files in seperate folder.

## References
Xinyu Dong, Jianyuan Deng, Wei Hou, Sina Rashidian, Richard N. Rosenthal, Mary Saltz, Joel H. Saltz, Fusheng Wang,
Predicting opioid overdose risk of patients with opioid prescriptions using electronic health records based on temporal deep learning,
Journal of Biomedical Informatics, Volume 116, 2021, 103725, ISSN 1532-0464,
https://doi.org/10.1016/j.jbi.2021.103725.

