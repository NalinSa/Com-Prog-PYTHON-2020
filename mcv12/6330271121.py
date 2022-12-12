# Prog-12: COVID-19: The Latest Wave
# 6330271121 Nalin Baipluthong
import numpy as np
def read_data(filename):
    d = np.loadtxt(filename, delimiter=",", encoding='utf-8', dtype=str)
    new_cases = np.array(d[1:,1:], dtype=int)
    norm = new_cases / np.max(new_cases, axis=1).reshape((new_cases.shape[0],1))
    return {'new_cases': new_cases,
            'norm_data': norm,
            'province_names': d[1:,0],
            'dates': d[0,1:]}

def max_new_cases_date(data):
    ar_nc = data['new_cases']
    sum_nc = np.sum(ar_nc,axis=0)
    maxx = np.argmax(sum_nc)
    return (data['dates'][maxx], sum_nc[maxx])

def max_new_cases_province(data, beg_date, end_date):
    date = data['dates']
    nu = np.arange(date.shape[0])
    id_want = nu[(date==beg_date)|(date==end_date)]
    newcase = data['new_cases']
    ar_ncwant = newcase[:,id_want[0]:id_want[1]+1]
    sum_ncwant = np.sum(ar_ncwant,axis=1)
    maxx = np.argmax(sum_ncwant)
    return (data['province_names'][maxx], sum_ncwant[maxx])

def max_new_cases_province_by_dates(data):
    ar_0 = data['dates']
    ar_2 = np.max(data['new_cases'],axis=0)
    id_want = np.argmax(data['new_cases'],axis=0)
    ar_1 = data['province_names'][id_want]
    ar = np.array([ar_0,ar_1,ar_2]).T
    return ar

def most_similar(data, province):
    ar_pv = data['province_names']
    nu = np.arange(ar_pv.shape[0])
    id_want = nu[ar_pv==province][0]
    ar_norm = data['norm_data']
    nw = ar_norm[id_want]
    z = (nw-ar_norm)**2
    z[id_want] = 10**9
    a = np.sum(z,axis=1)
    return ar_pv[np.argmin(a)]

def most_similar_province_pair(data):
    norm = data['norm_data']
    pv = data['province_names']
    date = data['dates']
    a = norm.reshape((pv.shape[0],1,date.shape[0]))
    b = norm.reshape((1,pv.shape[0],date.shape[0]))
    z = (a-b)**2
    d = z.reshape((z.shape[0]*z.shape[1],z.shape[2]))
    r=np.sum(d,axis=1)
    r[0::z.shape[0]+1] = 10**9
    t = r.reshape((  int((r.shape[0])**0.5) ,int((r.shape[0])**0.5) ,1 ))
    kamin = np.argmin(t)
    idr = kamin//t.shape[1]
    idc = kamin%t.shape[1]
    return (pv[idr],pv[idc])

def most_similar_in_period(data, province, beg_date, end_date):
    norm = data['norm_data']
    pv = data['province_names']
    nu1 = np.arange(pv.shape[0])
    id_want1 = nu1[pv==province][0]
    no_pvwant = norm[id_want1]
    date = data['dates']
    nu2 = np.arange(date.shape[0])
    id_want2 = nu2[(date==beg_date)|(date==end_date)]
    normwant = no_pvwant[id_want2[0]:id_want2[1]+1]
    b = norm.reshape((norm.shape[0]*norm.shape[1],))
    y = np.arange(b.shape[0])
    r = (y<date.shape[0]*id_want1)|(y>=date.shape[0]*(id_want1+1))
    norm_cp = b[r].reshape((int(b[r].shape[0]/date.shape[0]),date.shape[0]))
    pv_cp = pv[pv!=province]
    le = id_want2[1]-id_want2[0]+1
    v = np.lib.stride_tricks.sliding_window_view(norm_cp, le,1)
    z = (normwant-v)**2
    d = z.reshape((z.shape[0]*z.shape[1],z.shape[2]))
    rr=np.sum(d,axis=1)
    t = rr.reshape((  v.shape[0] ,v.shape[1] ,1 ))
    kamin = np.argmin(t)
    idr = kamin//t.shape[1]
    idc = kamin%t.shape[1]
    return (pv_cp[idr],date[idc],date[idc+le-1])

def main():
    return

main()    