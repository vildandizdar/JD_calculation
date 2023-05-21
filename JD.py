#!/usr/bin/env python
# coding: utf-8


# Modülleri yüklüyoruz.
from datetime import date

print ("Julian Day Hesaplama Programı")

Gün = int(input("Gün giriniz."))
Ay = int(input("Ay giriniz.")) 
Yıl = int(input("Yıl giriniz.")) 


dt1 = date(year = Yıl, month = Ay, day = Gün)

dt2 = date(year = Yıl, month = 1, day = 1)

dt3 = (dt1 - dt2).days
dt3 = dt3+1


N = dt3
L = int((Yıl-1901)/4)




JD = 2415020 + 365*(Yıl-1900) + N + L - 0.5
print (dt1, "Tarihinin Julian Günü:", JD)




