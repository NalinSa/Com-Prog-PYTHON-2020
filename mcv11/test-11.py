# Prog-11: Weather report (EP.2)
# 6330268321 Narapat Wichob
import json
import math
data = json.load(open('th_weather_39.json'))

"""
def top_K_max_temp_by_region(data, K):
#บรรทัด 11718 ---> city
#temp อยู่ใน list และอยู่ใน main
    C=[]
    E=[]
    N=[]
    NE=[]
    S=[]
    W=[]
    #data = json.load(open('th_weather_39.json'))
    top_K={'C':[],'E':[],'N':[],'NE':[],'S':[],'W':[]}
    for e in data:
        if data[e]['city']['region']=='C':
            for i in range(len(data[e]['list'])):
                C.append(((data[e]['list'][i]['main']['temp']),data[e]['city']['name'],str(data[e]['list'][i]['dt_txt'])))
            C=sorted(C)[-1::-1]
        elif data[e]['city']['region']=='E':
            for i in range(len(data[e]['list'])):
                E.append(((data[e]['list'][i]['main']['temp']),data[e]['city']['name'],str(data[e]['list'][i]['dt_txt'])))
            E=sorted(E)[-1::-1]
        elif data[e]['city']['region']=='N':
            for i in range(len(data[e]['list'])):
                N.append(((data[e]['list'][i]['main']['temp']),data[e]['city']['name'],str(data[e]['list'][i]['dt_txt'])))
            N=sorted(N)[-1::-1]
        elif data[e]['city']['region']=='NE':
            for i in range(len(data[e]['list'])):
                NE.append(((data[e]['list'][i]['main']['temp']),data[e]['city']['name'],str(data[e]['list'][i]['dt_txt'])))
            NE=sorted(NE)[-1::-1]
        elif data[e]['city']['region']=='S':
            for i in range(len(data[e]['list'])):
                S.append(((data[e]['list'][i]['main']['temp']),data[e]['city']['name'],str(data[e]['list'][i]['dt_txt'])))
            S=sorted(S)[-1::-1]
        elif data[e]['city']['region']=='W':
            for i in range(len(data[e]['list'])):
                W.append(((data[e]['list'][i]['main']['temp']),data[e]['city']['name'],str(data[e]['list'][i]['dt_txt'])))
            W=sorted(W)[-1::-1]      
    for i in range(K):
        top_K['C'].append(C[i])
        top_K['E'].append(E[i])
        top_K['N'].append(N[i])
        top_K['NE'].append(NE[i])
        top_K['S'].append(S[i])
        top_K['W'].append(W[i])
    return top_K
print(top_K_max_temp_by_region(data, 2))
"""
"""
def average_temp_by_date(data, region):
    av_temp=[]
    Cd={}
    Ed={}
    Nd={}
    NEd={}
    Sd={}
    Wd={}
    ALLd={}
    if region == 'C':
        for e in data:      
            if data[e]['city']['region'] == 'C':
                for i in range(len(data[e]['list'])):
                    if data[e]['list'][i]['dt_txt'][0:10] not in Cd:
                        
                        Cd[data[e]['list'][i]['dt_txt'][0:10]]=[data[e]['list'][i]['main']['temp'],1]
                        
                    else:
                        Cd[data[e]['list'][i]['dt_txt'][0:10]][0]+=data[e]['list'][i]['main']['temp']
                        Cd[data[e]['list'][i]['dt_txt'][0:10]][1]+=1
        for e in Cd:
            av_temp.append((e,Cd[e][0]/Cd[e][1]))
    
    if region == 'E':
        for e in data:      
            if data[e]['city']['region'] == 'E':
                for i in range(len(data[e]['list'])):
                    if data[e]['list'][i]['dt_txt'][0:10] not in Ed:
                        
                        Ed[data[e]['list'][i]['dt_txt'][0:10]]=[data[e]['list'][i]['main']['temp'],1]
                        
                    else:
                        Ed[data[e]['list'][i]['dt_txt'][0:10]][0]+=data[e]['list'][i]['main']['temp']
                        Ed[data[e]['list'][i]['dt_txt'][0:10]][1]+=1
        for e in Ed:
            av_temp.append((e,Ed[e][0]/Ed[e][1]))
    
    if region == 'N':
        for e in data:      
            if data[e]['city']['region'] == 'N':
                for i in range(len(data[e]['list'])):
                    if data[e]['list'][i]['dt_txt'][0:10] not in Nd:
                        
                        Nd[data[e]['list'][i]['dt_txt'][0:10]]=[data[e]['list'][i]['main']['temp'],1]
                        
                    else:
                        Nd[data[e]['list'][i]['dt_txt'][0:10]][0]+=data[e]['list'][i]['main']['temp']
                        Nd[data[e]['list'][i]['dt_txt'][0:10]][1]+=1
        for e in Nd:
            av_temp.append((e,Nd[e][0]/Nd[e][1]))
    if region == 'NE':
        for e in data:      
            if data[e]['city']['region'] == 'NE':
                for i in range(len(data[e]['list'])):
                    if data[e]['list'][i]['dt_txt'][0:10] not in NEd:
                        
                        NEd[data[e]['list'][i]['dt_txt'][0:10]]=[data[e]['list'][i]['main']['temp'],1]
                        
                    else:
                        NEd[data[e]['list'][i]['dt_txt'][0:10]][0]+=data[e]['list'][i]['main']['temp']
                        NEd[data[e]['list'][i]['dt_txt'][0:10]][1]+=1
        for e in NEd:
            av_temp.append((e,NEd[e][0]/NEd[e][1]))
    if region == 'W':
        for e in data:      
            if data[e]['city']['region'] == 'W':
                for i in range(len(data[e]['list'])):
                    if data[e]['list'][i]['dt_txt'][0:10] not in Wd:
                        
                        Wd[data[e]['list'][i]['dt_txt'][0:10]]=[data[e]['list'][i]['main']['temp'],1]
                        
                    else:
                        Wd[data[e]['list'][i]['dt_txt'][0:10]][0]+=data[e]['list'][i]['main']['temp']
                        Wd[data[e]['list'][i]['dt_txt'][0:10]][1]+=1
        for e in Wd:
            av_temp.append((e,Wd[e][0]/Wd[e][1]))
    if region == 'S':
        for e in data:      
            if data[e]['city']['region'] == 'S':
                for i in range(len(data[e]['list'])):
                    if data[e]['list'][i]['dt_txt'][0:10] not in Sd:
                        
                        Sd[data[e]['list'][i]['dt_txt'][0:10]]=[data[e]['list'][i]['main']['temp'],1]
                        
                    else:
                        Sd[data[e]['list'][i]['dt_txt'][0:10]][0]+=data[e]['list'][i]['main']['temp']
                        Sd[data[e]['list'][i]['dt_txt'][0:10]][1]+=1
        for e in Sd:
            av_temp.append((e,Sd[e][0]/Sd[e][1]))
    if region == 'ALL':
        for e in data:
            for i in range(len(data[e]['list'])):
                if data[e]['list'][i]['dt_txt'][0:10] not in ALLd:
                    ALLd[data[e]['list'][i]['dt_txt'][0:10]]=[data[e]['list'][i]['main']['temp'],1]
                else:
                        ALLd[data[e]['list'][i]['dt_txt'][0:10]][0]+=data[e]['list'][i]['main']['temp']
                        ALLd[data[e]['list'][i]['dt_txt'][0:10]][1]+=1
        
        for e in ALLd:
            av_temp.append((e,ALLd[e][0]/ALLd[e][1]))    
    return av_temp         
print(average_temp_by_date(data, 'ALL'))
"""
def max_rain_in_3h_periods(data, region, date):
#list rain
    max_rain=[]
    Ct=[]
    Cr=[]
    C={}
    
    Et=[]
    Er=[]
    E1={}
    E2={}
    Nt=[]
    Nr=[]
    N1={}
    N2={}
    NEt=[]
    NEr=[]
    NE1={}
    NE2={}
    St=[]
    Sr=[]
    S1={}
    S2={}
    Wt=[]
    Wr=[]
    W1={}
    W2={}
    ALLt=[]
    ALLr=[]
    ALL1={}
    ALL2={}
    if region == 'W':
        for e in data:      
                if data[e]['city']['region'] == 'W':
                    
                    for i in range(len(data[e]['list'])):
                        if 'rain' in data[e]['list'][i]:
                            #if data[e]['list'][i]['dt_txt'].split()[0]==date: 
                            q = data[e]['list'][i]['dt_txt']
                            Ct.append([q[0:10],int(q[11:13])])
                            for v in data[e]['list'][i]['rain'].keys():
                                Cr.append(v)  #Cr เก็บค่าฝน
                       
                    for a,b in Ct:
                        if a not in C:
                            dd = {}
                            for i in range(len(Ct)):
                                if Ct[i][0]==a:
                                    if Ct[i][1] not in dd:
                                        dd[Ct[i][1]] = [Cr[i]]
                                    else:
                                        dd[Ct[i][1]].append(Cr[i])
                            C[a] = dd
    if date in C:
        for e in C[date]:
            max_rain.append(e,max(C[data][e]))
    return max_rain
print(max_rain_in_3h_periods(data, 'W', '2021-04-07'))
