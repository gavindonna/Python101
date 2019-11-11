# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:40:43 2018

@author: gavind
"""

import sys
import copy
import numpy as np
import pandas as pd
from scipy import stats
#import matplotlib
import matplotlib.pyplot as plt

data=pd.read_csv("summary_statistics.csv")

#print(data)
problem_set = data['problem_set']
problems_per_student_mean=data['problems_per_student_mean']

print(pd.read_csv("summary_statistics.csv", nrows=1).columns)
fig, ax = plt.subplots()
#ax.set_xlabel('Smarts')
#ax.set_ylabel('Probability density')
ax.set_title('Problem set')
problem_set.plot()
plt.show()


fig, ax = plt.subplots()
#ax.set_xlabel('Smarts')
#ax.set_ylabel('Probability density')
ax.set_title('Problems per student mean')
problems_per_student_mean.plot()
plt.show()
#plt.plot(problem_set, problems_per_student_mean)
#plt.figure()