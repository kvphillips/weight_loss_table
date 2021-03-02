# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:20:55 2021

@author: katie
"""

member1 = [""]
member2 = [""]

member1[0] = input("Enter the name of the first member? ")
member2[0] = input("Enter the name of the second member? ")

member1.append(eval(input("How many pounds did " + member1[0] + " lose in January? ")))
member2.append(eval(input("How many pounds did " + member2[0] + " lose in January? ")))

member1.append(eval(input("How many pounds did " + member1[0] + " lose in February? ")))
member2.append(eval(input("How many pounds did " + member2[0] + " lose in February? ")))

member1.append(eval(input("How many pounds did " + member1[0] + " lose in March? ")))
member2.append(eval(input("How many pounds did " + member2[0] + " lose in March? ")))

member1.append(eval(input("How many pounds did " + member1[0] + " lose in April? ")))
member2.append(eval(input("How many pounds did " + member2[0] + " lose in April? ")))

member1.append(eval(input("How many pounds did " + member1[0] + " lose in May? ")))
member2.append(eval(input("How many pounds did " + member2[0] + " lose in May? ")))

months = ["","January", "February", "March", "April", "May"]

import pandas as pd
print("Total Weight Loss Chart")
T = pd.DataFrame([months, member1, member2])
print(T)

print (member1[0] + " lost a total weight of: " + str(sum(member1[1:6])) + " lbs")
print (member2[0] + " lost a total weight of: " + str(sum(member2[1:6])) + " lbs")