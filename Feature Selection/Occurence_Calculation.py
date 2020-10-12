import pandas as pd

## Diagnosis selection and dictionary from dx to position construction

ouddx=pd.read_csv('ouddx.csv')

for i in range(ouddx.shape[0]):
    e=ouddx['encounter_id'][i]
    if e in e2p:
        p=e2p[e]
        dx=ouddx['diagnosis_code'][i]
        if dx in icd9to10:
            dx=icd9to10[dx]
        dx3=dx[:3]
        if dx3 in dxcnt:
            dxcnt[dx3].add(p)
        else:
            dxcnt[dx3]=set([p]) 

remaindx=set([])

for dx in dxcnt:
    if dxcnt[dx]>NumOfPatients/100:
        remaindx.add(dx)

dxdict={}
position=0
for dx in remaindx:
    dxdict[dx]=position
    position+=1

# Lab test selection and dictionary from laboratory test to position construction
labcnt={}
for i in range(oplab.shape[0]):
    if i%3000000==0:
        print i
    e=oplab['encounter_id'][i]
    if e in alle2p:
        pski=alle2p[e]
        lab=oplab['lab_id'][i]
        if lab in labcnt:
            labcnt[lab].add(pski)
        else:
            labcnt[lab]=set([pski])
            
remainlab=set([])
for lab in labcnt:
    if labcnt[ce]>NumOfPatients/100:
        remainlab.add(lab)

labdict={}
position=0
for lab in remainlab:
    labdict[lab]=position
    position+=1

# Medication selection and dictionary from  to position construction
# atc4 is mapping from medication id in HealthFacts to ATC code with first 4 digits
medcnt={}
for i in range(oudmed.shape[0]):
    if i%1000000==0:
        print i
    e=oudmed['encounter_id'][i]
    if e in e2p:
        p=e2p[e]
        medid=oudmed['medication_id__hf_d_medication_'][i]
        if str(medid) not in atc4:
            a=str(medid)
            if a in medcnt:
                medcnt[a].add(p)
            else:
                medcnt[a]=set([p])
            continue
        atcset=atc3[str(medid)]
        for a in atcset:
            if a in medcnt:
                medcnt[a].add(p)
            else:
                medcnt[a]=set([p])


remainmed=set([])
for med in medcnt:
    if medcnt[ce]>NumOfPatients/100:
        remainmed.add(med)

meddict={}
position=0
for med in remainmed:
    meddict[med]=position
    position+=1

# Clinical Event selection and dictionary from clinical event to position construction

cecnt={}
for i in range(oudce.shape[0]):
    e=oudce['encounter_id'][i]
    if e in e2p:
        p=e2p[e]
        ce=oudce['event_code_id'][i]
        if ce in cecnt:
            cecnt[ce].add(p)
        else:
            cecnt[ce]=set([p])
            
remaince=set([])
for ce in cecnt:
    if cecnt[ce]>NumOfPatients/100:
        remaince.add(ce)

cedict={}
position=0
for ce in remaince:
    cedict[ce]=position
    position+=1


#Race dictionary construction
length=2
racedict={'Biracial':length, 'Asian/Pacific Islander':length+1, 'Pacific Islander':length+2, 'Hispanic':length+3, 'Other':length+4, 'Asian':length+5, 'Mid Eastern Indian':length+6, 'African American':length+7,'Caucasian':length+8, 'Native American':length+9}
