#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            print(' sum_n=',n)
            ax = ax + n
        return ax
    return sum

lazy = lazy_sum(1,2,3);
lazy()

def log(text):
    def deco(func):
        def wrapper(*args,**kw):
            print('%s %s' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return deco


def log(func):
    def wrapper(*args, **kw):
        print('call begin %s():' % func.__name__)
        func(*args,**kw)
        print('call end %s ' % func.__name__)
    return wrapper





@log
def now():
    print('2016-09-30')

now()

#lfs = log(now())
#print(lfs)

#lfs()