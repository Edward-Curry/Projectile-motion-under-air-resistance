# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:20:30 2023

@author: ecurry
"""

import matplotlib.pylab as plt
import numpy as np


B = 1.6e-4
C = 0.25

VD = np.arange(0.00, 0.00005, 0.00001) #neglect quadraticic for 0 to 0.0001
                                        #neglect lin after 0.005

def bV(VD) :
    bV = B*VD 
    return bV
    
def cV(V):
    cV = C * VD**2
    return cV


plt.plot(VD, bV(VD), label = "linear")
plt.plot(VD, cV(VD), label = "quadratic")
plt.title("f(V) vs VD")
plt.xlabel("VD")
plt.ylabel("f(V)")
plt.legend()

plt.show()

g = 9.80
D = 10e-4
b = D * B
dt = 1e-3
tol = 1e-10
m = 8.377e-7
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

def vel(v):
    v = v -g*dt -((b/m)*v*dt)
    return v



while np.abs(v - v_old)/dt > tol :
    v_arr.append(v)
    t_arr.append(t)
    t = t+dt
    v_old = v
    v = vel(v)
    n_steps += 1
    

plt.plot(t_arr,v_arr, color = "red")
plt.xlabel("time")
plt.ylabel("Velcity")
plt.title("V vs t estimate ")

plt.show()

def analy(t):
    Ya = (m*g/b)*(np.exp(-b*t/m)-1)
    return Ya

ta = np.arange(0.0, dt*n_steps, dt )

plt.plot(ta, analy(ta),t_arr, v_arr)
plt.title("V vs t analytical")
plt.show()

error = analy(ta) - v_arr
plt.plot(t_arr,error)
plt.title("error")
plt.xlabel("time")
plt.ylabel("error")
plt.title("error vs time")

plt.show()



while m < 100:
    s = h
    t = 0
    while s > 0 :
        v_arr.append(v)
        t_arr.append(t)
        s = s + v*dt
        t = t+dt
        v_old = v
        v = vel(v)
        n_steps += 1
    tg_arr.append(t)
    mass_arr.append(m)
    m += 0.01
    
plt.plot(mass_arr,tg_arr)
plt.xlabel("Fall Time")
plt.ylabel("mass")
plt.title("mass vs Fall time")

plt.show()



vx = 5
vy = 5

sy = 0
sx = 0

m = 0.0000005
sx_arr = []
sy_arr = []


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

vy = 5
vx = 5
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
    
    


plt.xlabel("Displacement x direction")
plt.ylabel("displacement y direction")
plt.title("trajectories of particle")
plt.plot(sx_arr,sy_arr, label = "vacum")
plt.plot(sxa_arr,sya_arr,label = "linear")
plt.legend()

plt.show()

theta = 0.01
dtheta = 0.001
m = 0
v = 10
distance_arr = [1e-5,1e-4]
m_arr = []
theta_arr = []
dm = 1e-6

while m <2e-5:
    v = 10
    distance_arr = [1e-5,1e-4]
    theta = 0.01
    m += dm
    m_arr.append(m)
    while distance_arr[-1] >= distance_arr[-2]:
        vx = v*np.cos(theta)
        vy = v*np.sin(theta)
        sx = 0
        sy = 0
        while sy >= 0: 
            sx_arr.append(sx)
            sy_arr.append(sy)
            sx = sx + vx*dt
            sy = sy + vy*dt
            vx = velx(vx)
            vy = vely(vy)
        
    
        distance_arr.append(sx)
        theta += dtheta
    theta_arr.append((theta))

plt.plot(m_arr,theta_arr)
plt.xlabel("mass")
plt.ylabel("optimum angle")
plt.title("optimum angle vs mass")
plt.savefig("mass angle.pdf")
plt.show()
