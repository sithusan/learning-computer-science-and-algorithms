#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:26:36 2022

@author: sithusan
"""

annual_salary = float(input("Enter your annual salary : "));
monthly_salary = annual_salary / 12;

portion_save_percentage = float(input("Enter percent of your salary to save, as a decimal : "));
portion_save = monthly_salary * portion_save_percentage;

total_cost = float(input("Enter total cost of your house : "));
down_payment = total_cost * 0.25;

semi_annual_raise = float(input("Enter your semi annual raise : "));

current_savings = 0;

i = 0;
j = 1;

while(down_payment >= current_savings):
    i+=1
    current_savings += portion_save + ((current_savings * 0.04)/12)
    
    if((i/6) == j) :
        rise = semi_annual_raise * monthly_salary
        monthly_salary = monthly_salary+rise 
        portion_save = portion_save_percentage * monthly_salary
        j+=1;
        

 

print("Month",i,"Current Saving",current_savings,"Downpayment",down_payment)


