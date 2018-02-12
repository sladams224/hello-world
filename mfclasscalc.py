# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:47:35 2017

@author: Azazel
"""

males_int = int(input("Enter number of males:"))
females_int = int(input("Enter number of females:"))
students_tot = int(males_int + females_int)
percentmale_float = (males_int/students_tot)*100
percentmale_int = int(percentmale_float)
percentmale_str = str(percentmale_int)+"%"
percentfemale_float = (females_int/students_tot)*100
percentfemale_int = int(percentfemale_float)
percentfemale_str = str(percentfemale_int)+"%"
print ("Percent males:", percentmale_str". Percent females:", percentfemale_str)
