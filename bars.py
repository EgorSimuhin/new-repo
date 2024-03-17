#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib
T1 = 20
h1 = 23 #mm
pmax1 = (0.2 * 9.80665)*np.array([125, 125, 125, 125]) #Па
pmin1 = (0.2 * 9.80665)*np.array([122, 122, 122, 122]) #Па
pmax_sred1 = sum(pmax1)/len(pmax1)
pmin_sred1 = sum(pmin1)/len(pmin1)
pmaxabs1 = max(pmax1)
pminabs1 = min(pmin1)
#print("MAX1 = ", pmaxabs1)
#print("MIN1 = ", pminabs1)
#print("MAXSRED1 = ", pmax_sred1)
#print("MINSRED1 = ", pmin_sred1, "\n")

T2 = 20
h2 = 7 #mm
pmin2 = (0.2 * 9.80665)*np.array([212, 212.5, 213, 214, 213, 213])
pmax2 = (0.2 * 9.80665)*np.array([216, 216, 217, 217, 217, 217])
pmax_sred2 = sum(pmax2)/len(pmax2)
pmin_sred2 = sum(pmin2)/len(pmin2)
pmaxabs2 = max(pmax2)
pminabs2 = min(pmin2)
#print("MAX2 = ", pmaxabs2)
#print("MIN2 = ", pminabs2)
#print("MAXSRED2 = ", pmax_sred2)
#print("MINSRED2 = ", pmin_sred2, "\n")

T3 = 25.3
h3 = 7#mm
pmax3 = (0.2 * 9.80665)*np.array([227, 226, 227, 227])
pmin3 = (0.2 * 9.80665)*np.array([221, 220, 220, 220])
pmax_sred3 = sum(pmax3)/len(pmax3)
pmin_sred3 = sum(pmin3)/len(pmin3)
pmaxabs3 = max(pmax3)
pminabs3 = min(pmin3)
#print("MAX3 = ", pmaxabs3)
#print("MIN3 = ", pminabs3)
#print("MAXSRED3 = ", pmax_sred3)
#print("MINSRED3 = ", pmin_sred3, "\n")



T4 = 30.1
h4 = 7#mm
pmax4 = (0.2 * 9.80665)*np.array([231, 231, 231, 231, 231])
pmin4 = (0.2 * 9.80665)*np.array([219, 219, 221, 220, 219])
pmax_sred4 = sum(pmax4)/len(pmax4)
pmin_sred4 = sum(pmin4)/len(pmin4)
pmaxabs4 = max(pmax4)
pminabs4 = min(pmin4)
#print("MAX4 = ", pmaxabs4)
#print("MIN4 = ", pminabs4)
#print("MAXSRED4 = ", pmax_sred4)
#print("MINSRED4 = ", pmin_sred4, "\n")


T5 = 35.3
h5 = 7#mm
pmax5 = (0.2 * 9.80665)*np.array([228, 228])
pmin5 = (0.2 * 9.80665)*np.array([222, 222])
pmax_sred5 = sum(pmax5)/len(pmax5)
pmin_sred5 = sum(pmin5)/len(pmin5)
pmaxabs5 = max(pmax5)
pminabs5 = min(pmin5)
#print("MAX5 = ", pmaxabs5)
#print("MIN5 = ", pminabs5)
#print("MAXSRED5 = ", pmax_sred5)
#print("MINSRED5 = ", pmin_sred5, "\n")


T6 = 40
h6 = 7#mm
pmax6 = (0.2 * 9.80665)*np.array([233, 232, 232, 231])
pmin6 = (0.2 * 9.80665)*np.array([223, 223, 223, 222])
pmax_sred6 = sum(pmax6)/len(pmax6)
pmin_sred6 = sum(pmin6)/len(pmin6)
pmaxabs6 = max(pmax6)
pminabs6 = min(pmin6)
#print("MAX6 = ", pmaxabs6)
#print("MIN6 = ", pminabs6)
#print("MAXSRED6 = ", pmax_sred6)
#print("MINSRED6 = ", pmin_sred6, "\n")


T7 = 45
h7 = 7#mm
pmax7 = (0.2 * 9.80665)*np.array([202, 204, 204, 204, 204, 204])
pmin7 = (0.2 * 9.80665)*np.array([198, 199, 199, 199, 199, 199])
pmax_sred7 = sum(pmax7)/len(pmax7)
pmin_sred7 = sum(pmin7)/len(pmin7)
pmaxabs7 = max(pmax7)
pminabs7 = min(pmin7)
#print("MAX7 = ", pmaxabs7)
#print("MIN7 = ", pminabs7)
#print("MAXSRED7 = ", pmax_sred7)
#print("MINSRED7 = ", pmin_sred7, "\n")


T8 = 50
h8 = 7#mm
pmax8 = (0.2 * 9.80665)*np.array([205, 205, 205, 205, 205, 205])
pmin8 = (0.2 * 9.80665)*np.array([200, 200, 200, 200, 200, 200])
pmax_sred8 = sum(pmax8)/len(pmax8)
pmin_sred8 = sum(pmin8)/len(pmin8)
pmaxabs8 = max(pmax8)
pminabs8 = min(pmin8)
#print("MAX8 = ", pmaxabs8)
#print("MIN8 = ", pminabs8)
#print("MAXSRED8 = ", pmax_sred8)
#print("MINSRED8 = ", pmin_sred8, "\n")



T9 = 55
h9 = 7#mm
pmax9 = (0.2 * 9.80665)*np.array([224, 223, 222, 224, 223])
pmin9 = (0.2 * 9.80665)*np.array([216, 215, 215, 215, 216])
pmax_sred9 = sum(pmax9)/len(pmax9)
pmin_sred9 = sum(pmin9)/len(pmin9)
pmaxabs9 = max(pmax9)
pminabs9 = min(pmin9)
#print("MAX9 = ", pmaxabs9)
#print("MIN9 = ", pminabs9)
#print("MAXSRED9 = ", pmax_sred9)
#print("MINSRED9 = ", pmin_sred9,"\n")



T10 = 60
h10 = 7#mm
pmax10 = (0.2 * 9.80665)*np.array([222, 222, 223, 223, 223])
pmin10 = (0.2 * 9.80665)*np.array([216, 215, 215, 215, 215])
pmax_sred10 = sum(pmax10)/len(pmax10)
pmin_sred10 = sum(pmin10)/len(pmin10)
pmaxabs10 = max(pmax10)
pminabs10 = min(pmin10)
#print("MAX10 = ", pmaxabs10)
#print("MIN10 = ", pminabs10)
#print("MAXSRED210 = ", pmax_sred10)
#print("MINSRED10 = ", pmin_sred10)


#Данные закончились. Дальше обработка
#======================================================
raznost = np.array([pmaxabs1 - pminabs1, pmaxabs2 - pminabs2, pmaxabs3 - pminabs3, pmaxabs4 - pminabs4, pmaxabs5 - pminabs5, pmaxabs6 - pminabs6, pmaxabs7 - pminabs7, pmaxabs8 - pminabs8, pmaxabs9 - pminabs9, pmaxabs10-  pminabs10])

#print("=====================")
#h  = 1
#for i in raznost:
#    print (f"Разность давлений в опыте{h}:" , i, "Па\n")
#    h += 1

Height = (raznost)/(1000 * 9.8)
#d = 1
#print("=====================")
#for i in Height:
#    print (f"Высота воды в опыте {d}:" , i * 100, "см\n")
#    d += 1

sigmawater = (raznost) * 1.1 * 0.25 * 0.001
#print("Поверхностное натяжение воды")
#print(sigmawater)
T = [1, 2, 3, 3]
Temperature = np.array([T1, T2, T3, T4, T5, T6, T7, T8, T9, T10])
plt.plot(T)
plt.show






