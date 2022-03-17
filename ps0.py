#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 22:56:29 2022

@author: sithusan
"""

import numpy

x = int(input("Enter number x : "))

y = int(input("Enter number y: "))

a = pow(x,y);

logx = numpy.log2(x);

print("x raised to the power of y is ",a);
print("log(x) is", logx)