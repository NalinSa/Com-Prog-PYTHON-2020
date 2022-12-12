# Prog-12: COVID-19: The Latest Wave
# 6330268321 Narapat Wichob

import numpy as np
def read_data(filename):
    d = np.loadtxt(filename, delimiter=",", encoding='utf-8', dtype=str)
    new_cases = np.array(d[1:,1:], dtype=int)
    norm = new_cases / np.max(new_cases, axis=1).reshape((new_cases.shape[0],1))
    return {'new_cases': new_cases,
            'norm_data': norm,
            'province_names': d[1:,0],
            'dates': d[0,1:]}
data = read_data('TH_20210401_20210416.csv')

#---------------------------------------------------------------
def max_new_cases_date(data):
    a=np.sum(data['new_cases'],axis=0)
    return (data['dates'][np.argmax(a)],np.max(a))
#print(max_new_cases_date(data))
#----------------------------------------------------------------
def max_new_cases_province(data, beg_date, end_date):
    b1=data['dates']==beg_date
    c1=data['dates']==end_date
    a1=np.arange(len(data['dates']))[b1]
    a2=np.arange(len(data['dates']))[c1]
    a3=np.sum(data['new_cases'][:,a1[0]:a2[0]+1,],axis=1)
    return (data['province_names'][np.argmax(a3)],np.max(a3))
#print(max_new_cases_province(data, '2021-04-10', '2021-04-13'))
#-------------------------------------------------------------------
def max_new_cases_province_by_dates(data):
    a=np.ndarray((data['dates'].shape[0],3),dtype=object)
    a[:,0]=data['dates']
    c=np.max(data['new_cases'],axis=0)
    a[:,2]=c
    b1=data['new_cases']==c
    b2=np.arange(len(data['province_names']))[b1]
    b3=data['province_names'][b2]
    
    return a
print(max_new_cases_province_by_dates(data))
    
    

