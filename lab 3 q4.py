# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:31:45 2023

@author: edwar
"""
import matplotlib.pylab as plt
import numpy as np
import math as math

B = 1.6e-4
C = 0.25
g = 9.80
D = 10e-4
b = D * B
c = (D**2) * C
dt = 1e-3
tol = 1e-10
m = 8.377e-9
v = 0
v_old = 10
t = 0
n_steps = 0
t_arr = []
v_arr = []
h = 10
s = h
tg_arr = []
mass_arr = []


v = 40
vx = v
vy = v

sy = 0
sx = 0

m = 0.00001
sx_arr = []
sy_arr = []


def velyq(vy):
    vy = vy -g*dt -((c/m)*(math.sqrt(vx**2+vy**2))*vy*dt)
    return vy

def velxq(vx):
    vx = vx -((c/m)*(math.sqrt(vx**2+vy**2))*vx*dt)
    return vx

def vely(vy):
    vy = vy -g*dt -((b/m)*vy*dt)
    return vy

def velx(vx):
    vx = vx -((b/m)*vx*dt)
    return vx

def velya(vy):
    vy = vy -g*dt
    return vy

while sy >= 0: 
    sx_arr.append(sx)
    sy_arr.append(sy)
    sx = sx + vx*dt
    sy = sy + vy*dt
    vx = velx(vx)
    vy = vely(vy)

vy = v
vx = v
sy = 0
sx = 0
sxa_arr = []
sya_arr = []

while sy >= 0:
    sxa_arr.append(sx)
    sya_arr.append(sy)
    sx = sx + vx*dt
    sy = sy + vy*dt
    vy = velya(vy)
    
vy = v
vx = v
sy = 0
sx = 0
sxq_arr = []
syq_arr = []
   
while sy >= 0: 
    sxq_arr.append(sx)
    syq_arr.append(sy)
    sx = sx + vx*dt
    sy = sy + vy*dt
    vx = velxq(vx)
    vy = velyq(vy)


print (sxq_arr)
plt.plot(sx_arr,sy_arr, label = "vacum")
plt.plot(sxa_arr,sya_arr, label = " linear")
plt.plot(sxq_arr,syq_arr, label = "quadratic")
plt.xlabel("displacement in x direction")
plt.ylabel("displacement in y direction")
plt.title("trajectories")
plt.legend()
plt.savefig("quadratic.pdf")
plt.show()


plt.show()