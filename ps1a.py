#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:04:09 2022

@author: sithusan
"""

annual_salary = float(input("Enter your annual salary : "));
monthly_salary = annual_salary / 12;

portion_save = float(input("Enter percent of your salary to save, as a decimal : "));
portion_save = monthly_salary * portion_save;

total_cost = float(input("Enter total cost of your house : "));
down_payment = total_cost * 0.25;

current_savings = 0;

i = 0;

while(down_payment >= current_savings):
    i+=1
    current_savings += portion_save + ((current_savings * 0.04)/12)
    print(current_savings)
 

print("Month",i,"Current Saving",current_savings,"Downpayment",down_payment)


