import pandas as pd
import numpy as np


##Fill in values for diagnosis features
for i in range(comdx.shape[0]):
    e=comdx['encounter_id'][i]
    if e in e2p:
        p=e2p[e]
        x=psk2[p]
        if e in pos[p]:
            y=pos[p][e]
            dx=comdx['diagnosis_code'][i]
            if dx in icd9to10:
                dx=icd9to10[dx]
            dx3=dx[:3]
            if dx3 in dxdict:
                z=dxdict[dx3]
                comx[x,y,z]=1

for i in range(oudx.shape[0]):
    if i%1000000==0:
        print i
    e=ouddx['encounter_id'][i]
    if e in e2p:
        p=e2p[e]
        if e in pos[p] and p in psk:
            x,y=psk[p],pos[p][e]
            dx=ouddx['diagnosis_code'][i]
            if dx in dxdict:
                z=dxdict[dx]
                ouddxx[x,y,z]=1
    
##Fill in values for clinical event features

cevalues={}

for i in range(oudce.shape[0]):
    if i%2000000==0:
        print i
    e=comce['encounter_id'][i]
    ce=comce['event_code_id'][i]
    if ce in cedict and e in e2p:
        p=e2p[e]
        if p in cevalues and e in cevalues[p]:
            v=comce['result_value_num'][i]
            cevalues[p][e][ce].append(v)

for i in range(comce.shape[0]):
    if i%2000000==0:
        print i
    e=comce['encounter_id'][i]
    ce=comce['event_code_id'][i]
    if ce in cedict and e in e2p:
        p=e2p[e]
        if p in cevalues and e in cevalues[p]:
            v=comce['result_value_num'][i]
            cevalues[p][e][ce].append(v)

for e in cevalues:
    if j%200000==0:
        print j
    j+=1
    for ce in cevalues[e]:
        if len(cevalues[e][ce])>0:
            p=e2p[e]
            x,y,z=psk2[p],pos[p][e],cedict[ce]
            comcex[x,y,z*3]=max(cevalues[e][ce])
            comcex[x,y,z*3+1]=min(cevalues[e][ce])
            comcex[x,y,z*3+2]=np.median(cevalues[e][ce])

        
for e in cevalues:
    if j%200000==0:
        print j
    j+=1
    for ce in cevalues[e]:
        if len(cevalues[e][ce])>0:
            p=e2p[e]
            if p in psk:
                x,y,z=psk[p],pos[p][e],cedict[ce]
                oudcex[x,y,z*3]=max(cevalues[e][ce])
                oudcex[x,y,z*3+1]=min(cevalues[e][ce])
                oudcex[x,y,z*3+2]=np.median(cevalues[e][ce])


##Fill in values for Lab test features

for i in range(oudlab.shape[0]):
    labi=oudlab['lab_id'][i]
    if labi in labdict:
        e=oudlab['encounter_id'][i]
        if e in e2p:
            p=e2p[e]
            if p in pos and p in psk and e in pos[p]:
                x,y,z=psk[p],pos[p][e],labdict[labi]
                if oudlab['result_indicator_desc'][i]=='Low':
                    oudlabx[x,y,z*3]+=1
                elif oudlab['result_indicator_desc'][i]=='High':
                    oudlabx[x,y,z*3+1]+=1
                oudlabx[x,y,z*3+2]+=1


for i in range(comlab.shape[0]):
    labi=comlab['lab_id'][i]
    if labi in labdict:
        e=comlab['encounter_id'][i]
        if e in e2p:
            p=e2p[e]
            if p in pos and p in psk2 and e in pos[p]:
                x,y,z=psk2[p],pos[p][e],labdict[labi]
                if comlab['result_indicator_desc'][i]=='Low':
                    comlabx[x,y,z*3]+=1
                elif comlab['result_indicator_desc'][i]=='High':
                    comlabx[x,y,z*3+1]+=1
                comlabx[x,y,z*3+2]+=1


##Fill in values for medication features


for i in range(oudmed.shape[0]):
    medid=str(oudmed['medication_id__hf_d_medication_'][i])
    e=oudmed['encounter_id'][i]
    medset=set([])
    if medid in atc3:
        medset=atc3[medid]
    else:
        medset=set([medid])
    for med in medset:
        if med in meddict and e in e2p:
            p=e2p[e]
            if p in psk and e in pos[p]:
                x,y,z=psk[p],pos[p][e],meddict[med]
                value=oudmed['dose_quantity'][i]
                oudmedx[x,y,z]+=value
                if medid in mme:
                    oudmedx[x,y,-1]+=value*mme[medid]

for i in range(commed.shape[0]):
    medid=str(commed['medication_id__hf_d_medication_'][i])
    e=commed['encounter_id'][i]
    medset=set([])
    if medid in atc3:
        medset=atc3[medid]
    else:
        medset=set([medid])
    for med in medset:
        if med in meddict and e in e2p:
            p=e2p[e]
            if p in psk2 and e in pos[p]:
                x,y,z=psk2[p],pos[p][e],meddict[med]
                value=commed['dose_quantity'][i]
                commedx[x,y,z]+=value
                if medid in mme:
                    commedx[x,y,-1]+=value*mme[medid]


##Fill in values for demographics features
for i in range(comdemo.shape[0]):
    e=comdemo['encounter_id'][i]
    if e in e2p:
        p=e2p[e]
        x=psk[p]
        if e in pos[p]:
            y=pos[p][e]
            gender=comdemo['gender'][i]
            age=comdemo['age'][i]
            race=comdemo['race'][i]
            if gender=='Female':
                comdemox[x,y,0]=1
            comdemox[x,y,1]=age
            if race in racedict:
                z=racedict[race]
                comdemox[x,y,z]=1




for i in range(ouddemo.shape[0]):
    e=ouddemo['encounter_id'][i]
    if e in e2p:
        p=e2p[e]
        x=psk[p]
        if e in pos[p]:
            y=pos[p][e]
            gender=ouddemo['gender'][i]
            age=ouddemo['age'][i]
            race=ouddemo['race'][i]
            if gender=='Female':
                ouddemox[x,y,0]=1
            ouddemox[x,y,1]=age
            if race in racedict:
                z=racedict[race]
                ouddemo[xx,y,z]=1           
            
##Concate the whole matrix
comx=np.concatenate((ouddx,oudlabx,oudmedx,oudcex,ouddemox))
oudx=np.concatenate((comx,comlabx,commedx,comcex,comdemox))






    
