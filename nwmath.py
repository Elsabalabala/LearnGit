#!usr/bin/env python
#coding=utf-8

def add(a, b):
        return a + b

def subtract(a, b):
    if isinstance(a,int) and isinstance(b,int):
        return a - b
    else:
        return "error input"

def multiply(a, b):
        return a * b

def divide(numerator, denominator):
    if denominator!=0 and isinstance(denominator,int):
        return float(numerator) / denominator
    else:
        return "wrong input"
