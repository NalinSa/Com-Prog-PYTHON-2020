# Prog-11: Weather report (EP.2)
# 6330271121 Nalin Baipluthong
import json
import math
#-------------------------------------------------------------------------------------------------------
def top_K_max_temp_by_region(data, K):
    dic = {}
    for va in data.values():
        if va['city']['region'] in dic:        
            l = []
            name = va['city']['name']
            for dic_lis in va['list']:
                tem = dic_lis['main']['temp']
                time = dic_lis['dt_txt']
                tup = [-tem, name, time]
                l.append(tup)
            dic[va['city']['region']] += l
        else:
            l = []
            name = va['city']['name']
            for dic_lis in va['list']:
                tem = dic_lis['main']['temp']
                time = dic_lis['dt_txt']
                tup = [-tem, name, time]
                l.append(tup)
            dic[va['city']['region']] = l
    dic_want = {}
    for key in dic:
        l_want = []
        for [a,b,c] in sorted(dic[key])[:K:]:
            tupl = (-a,b,c)
            l_want.append(tupl)
        dic_want[key] = l_want
    return dic_want
#-------------------------------------------------------------------------------------------------------
def average_temp_by_date(data, region):
    dic = {}
    if region in [ 'N', 'E', 'W', 'S', 'C', 'NE']:
        for va in data.values():
            if va['city']['region'] == region:
                for dic_lis in va['list']:
                    tem = dic_lis['main']['temp']
                    date = dic_lis['dt_txt'][:10:]
                    if date in dic:
                        dic[date][0] += tem
                        dic[date][1] += 1
                    else:
                        dic[date] = [tem,1]
    elif region == 'ALL':
        for va in data.values():
            for dic_lis in va['list']:
                tem = dic_lis['main']['temp']
                date = dic_lis['dt_txt'][:10:]
                if date in dic:
                    dic[date][0] += tem
                    dic[date][1] += 1
                else:
                    dic[date] = [tem,1]
    lis = []
    for key in dic:
        su,co = dic[key]
        tu = (key,su/co)
        lis.append(tu)
    lis.sort()
    return lis        
#-------------------------------------------------------------------------------------------------------
def max_rain_in_3h_periods(data, region, date):
    dic = {}
    if region in [ 'N', 'E', 'W', 'S', 'C', 'NE']:
        for va in data.values():
            if va['city']['region'] == region:
                for dic_lis in va['list']:
                    dat = dic_lis['dt_txt'][:10:]
                    if 'rain' in dic_lis and dat == date:
                        rain = dic_lis['rain']['3h']
                        time = int(dic_lis['dt_txt'][11:13:])
                        if time in dic:
                            if rain>dic[time]:
                                dic[time] = rain
                        else:
                            dic[time] = rain
    elif region == 'ALL':
        for va in data.values():
            for dic_lis in va['list']:
                dat = dic_lis['dt_txt'][:10:]
                if 'rain' in dic_lis and dat == date:
                    rain = dic_lis['rain']['3h']
                    time = int(dic_lis['dt_txt'][11:13:])
                    if time in dic:
                        if rain>dic[time]:
                            dic[time] = rain
                    else:
                        dic[time] = rain
    lis = []
    for key in dic:
        tu = (key,dic[key])
        lis.append(tu)
    lis.sort()
    return lis
#-------------------------------------------------------------------------------------------------------
def AM_PM_weather_description_by_region(data, date):
    dic = {}
    for va in data.values():
        for dic_lis in va['list']:
            dat = dic_lis['dt_txt'][:10:]
            if dat == date:
                time = int(dic_lis['dt_txt'][11:13:])
                half = ''
                if 0<=time<12:
                    half = 'AM'
                elif 12<= time< 24:
                    half = 'PM'
                lis_weather = dic_lis['weather']
                lis_say = []
                for dicc in lis_weather:
                    lis_say.append(dicc['description'])
                if va['city']['region'] in dic:
                    if half in dic[va['city']['region']]:
                        dic[va['city']['region']][half] += lis_say
                    elif half != '':
                        dic[va['city']['region']][half] = lis_say
                else:
                    if half != '':
                        dic_f = {}
                        dic_f[half] = lis_say
                        dic[va['city']['region']] = dic_f
    for key in dic:
        for half in dic[key]:
            lis_name = []
            lis_count = []
            for e in dic[key][half]:
                if e not in lis_name:
                    lis_count.append([-dic[key][half].count(e),e])
                    lis_name.append(e)
            x,y = sorted(lis_count)[0]
            dic[key][half] = y
    return dic
#-------------------------------------------------------------------------------------------------------
def most_varied_weather_provinces(data):
    dic = {}
    for va in data.values():
        name = va['city']['name']
        set_say = set()
        for dic_lis in va['list']:
            lis_weather = dic_lis['weather']
            for dicc in lis_weather:
                set_say.add(dicc['description'])
        if len(set_say) in dic:
            dic[len(set_say)].add(name)
        else:
            dic[len(set_say)] = {name}
    if len(dic) > 0:
        c = sorted(dic)[-1]
        return dic[c]
    else: return set()
#-------------------------------------------------------------------------------------------------------
def main():
    return
#-------------------------------------------------------------------------------------------------------
main()