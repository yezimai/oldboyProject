# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

def count(n):
  print ("cunting" )
  while n > 0:
    print ('before yield')
    yield n  #生成值：n
    n -= 1
    print ('after yield' )
g1=count(5)
print g1.next()
print '------'
print g1.next()