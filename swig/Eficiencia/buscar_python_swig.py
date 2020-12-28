#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:32:08 2020

@author: juane99
"""

import example
import time

start_time = time.time()
example.buscarSubcadena("me llamo pepito","ito")
end_time = time.time()

print(end_time-start_time)