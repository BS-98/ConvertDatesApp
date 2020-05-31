# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:43:34 2019

@author: Bartek
"""

def data_julianska(sekunda,minuta,godzina,dzien,miesiac,rok):

    A1 = abs(sekunda)/60
    B1 = (abs(minuta) + A1)/60
    C1 = abs(godzina) + B1
    
    if godzina < 0:
        D1 = -C1
    else:
        D1 = C1
        
    dzien2 = int(dzien + D1/24)
    
    if miesiac < 3 :
        rok2 =  rok - 1
        miesiac2 = miesiac + 12
    else:
        rok2 = rok 
        miesiac2 = miesiac
    
    A = int(rok2/100)
    
    if rok > 1582:
        B = 2 - A + int(A/4)
    else:
        B = 0
        
    if rok2 < 0:
        C = int((365.25*rok2)-0.75)
    else:
        C = int(365.25*rok2)
        
    D = int(30.6001*(miesiac2+1))
    
    JD = dzien2 + B + C + D + 1720994.5

    
    return JD


def data_gregorianska(JD):
    
    I = int(JD + 0.5)
    F = JD + 0.5 - I
    A = int((I - 1867216.25)/36524.25)
    
    if I > 2299160:
        B = I + 1 + A - int(A/4)
    else:
        B = I
    
    C = B + 1524
    D = int((C-122.1)/365.25)
    E = int(365.25*D)
    G = int((C - E)/30.6001)
    dzien = int(C - E + F - int(30.6001*G))
    dzien2 = C - E + F - int(30.6001*G)
    
    if G < 13.5:
        miesiac = G - 1
    else:
        miesiac = G - 13
    
    if miesiac > 2.5:
        rok = D - 4716 
    else:
        rok = D - 4715
    
    
    unsigned_decimal = abs(dzien2)
    total_seconds = unsigned_decimal*3600
    seconds = int((total_seconds%60))
    
    if seconds == 60:
        corrected_seconds = 0
    else:
        corrected_seconds = seconds
    
    if seconds == 60:
        corrected_remainder = total_seconds + 60
    else:
        corrected_remainder = total_seconds
        
    minutes = int(int(corrected_remainder/60)%60)
    unsigned_hours = int(corrected_remainder/3600)
    
    if dzien < 0:
        signed_hours = -1*unsigned_hours
    else:
        signed_hours = unsigned_hours
        
    
    godziny = signed_hours
    minuty = minutes
    sekundy = corrected_seconds
    
    wynik = (sekundy, minuty, godziny, dzien, miesiac, rok) 
    return wynik

    
def GPS(sekunda,minuta,godzina,dzien,miesiac,rok):
    GPS_JD = 2444244.5
    NOW_JD = data_julianska(sekunda,minuta,godzina,dzien,miesiac,rok)
    roznica = NOW_JD - GPS_JD
    GPS_WEEK = int(roznica/7)
    DOW = float(roznica - GPS_WEEK*7)
    
    if DOW == 0:
        dzien = "Niedziela"
    elif DOW == 1:
        dzien = "Poniedziałek"
    elif DOW == 2:
        dzien = "Wtorek"
    elif DOW == 3:
        dzien = "Środa"
    elif DOW == 4:
        dzien = "Czwartek"
    elif DOW == 5:
        dzien = "Piątek"
    elif DOW == 6:
        dzien = "Sobota"
        
    SOW = int(DOW * 24 * 3600 + godzina*3600 + minuta*60 + sekunda)
    SOD = int((godzina*3600 + minuta*60 + sekunda))
    
    return (GPS_WEEK, SOW, dzien, SOD)

     
def UTC_2_JD(year,month,day,hour,minute,second):

    A1 = abs(second)/60
    B1 = (abs(minute) + A1)/60
    C1 = abs(hour) + B1
    
    if hour < 0:
        D1 = -C1
    else:
        D1 = C1
        
    dzien2 = int(day + D1/24)
    
    if month < 3 :
        rok2 =  year - 1
        miesiac2 = month + 12
    else:
        rok2 = year
        miesiac2 = month
    
    A = int(rok2/100)
    
    if year > 1582:
        B = 2 - A + int(A/4)
    else:
        B = 0
        
    if rok2 < 0:
        C = int((365.25 * rok2) - 0.75)
    else:
        C = int(365.25 * rok2)
        
    D = int(30.6001 * (miesiac2 + 1))
    
    JD = dzien2 + B + C + D + 1720994.5

    
    return JD

def UTC_2_GPS(year,month,day,hour,minute,second):
    GPS_JD = 2444244.5
    NOW_JD = UTC_2_JD(year,month,day,hour,minute,second)
    diff = NOW_JD - GPS_JD
    GPS_WEEK = int(diff/7)
    DOW = float(diff - GPS_WEEK*7)
        
    SOW = int(DOW * 24 * 3600 + hour*3600 + minute*60 + second)
    
    return SOW   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

