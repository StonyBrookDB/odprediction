

for i in range(oudlab.shape[0]):
    if i%3000000==0:
        print i
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
    if i%3000000==0:
        print i
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
