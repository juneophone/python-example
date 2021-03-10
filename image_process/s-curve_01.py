# -*- coding: utf-8 -*-
"""
@author		: 	jongwaye.ou
@Version 	: 	1.0
@Description:	S-Curve value.
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn")
D_total = []

fig = plt.subplots(figsize=(16, 8))
 
t = np.linspace(0, 255, 256)                    # data array
'''
# L: is the curve’s maximum value
# K: is the logistic growth rate or steepness of the curve
# t: is the input
# t0:is the midpoint of the sigmoid
'''
L, k = 255., 0.05                               # L 曲線最大值, K 曲線斜率
for t0 in np.arange(64, 192, 32):               # curve 中點數值
    D = L / (1. + np.exp(-k * (t - t0)))        # curve algorithm
    D1 = np.round(np.array(D)).astype(np.uint8) # Normalize curve value to integer 
    D_total += [D1]                             # curve total value table
    _ = plt.plot(t, D, label=f't0={t0}')
    
font = {'axes.labelsize': 22,                
        'xtick.labelsize': 25,
        'ytick.labelsize': 40,        
        'figure.titlesize': 16,        
        
        
        'axes.titlesize': 20,
        'legend.fontsize': 16,
        'legend.title_fontsize': 18
        }
plt.rcParams.update(font)    

plt.legend()    # 顯示圖例
plt.title('S-Curve')
plt.xlabel('Gray scale', fontsize=16)
plt.ylabel('Max value', fontsize=16)
plt.xticks(np.arange(0, 270, 32), fontsize=16)
plt.yticks(np.arange(0, 270, 16), fontsize=16)

