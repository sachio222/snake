'''
Disclaimer: This code was taken from flashliquid on stack overflow.
https://stackoverflow.com/questions/38651113/barnsley-fern-python-script
I made the code a tad bit faster using numpy arrays and made it output a nice graph.
'''
 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as style
 
style.use('fast')
 
plt.figure(figsize=(9,16))
ax=plt.gca()
ax.set_aspect('auto')
 
 
A=[]
 
#Matrix storing coefficients and probabilities
mat=[[0.0,0.0,0.0,0.16,0.0,0.0,0.01],
[0.85,0.04,-0.04,0.85,0.0,1.6,0.85],
[0.2,-0.26,0.23,0.22,0.0,1.6,0.07],
[-0.15,0.28,0.26,0.24,0.0,0.44,0.07]]
 
N=10000000
p=np.random.uniform(0,1,N)
 
x=0.0
y=0.0
 
#Iterating Loop
print('Iterating...')
for k in p:
    if k <= mat[0][6]:
        i=0
    elif k <= mat[0][6] + mat[1][6]:
        i=1
    elif k <= mat[0][6] + mat[1][6] + mat[2][6]:
        i=2
    else:
        i=3
 
    x0 = x * mat[i][0] + y * mat[i][1] + mat[i][4]
    y  = x * mat[i][2] + y * mat[i][3] + mat[i][5]
    x = x0
 
    ptn=[x,y]
    A.append(ptn)
 
print('Done Iterating')
 
A = np.array(A)
 
 
#----------
#PLOTTING!
#----------
 
#Dictionary with color codes for plotting
 
#colors={'red':'#ff0018','orange':'#ffa52c','yellow':'#ffff41','green':'#008018','blue':'#0000f9','purple':'#86007d'}
 
#colors={'pink':'#d60270','purple':'#9b4f96','blue':'#0038a8'}
 
colors={'green':'#008018'}
 
#Plot every color in dictionary and save to png
for key,value in colors.items():
    print(key,value)
    plt.figure(figsize=(9,16))
    ax=plt.gca()
    ax.set_aspect('auto')
 
 
    plt.axis('off')
    plt.tight_layout()
 
    plt.plot(A[:,0],A[:,1],',',c='g',alpha=0.4)
    plt.savefig(f'fern_{key}.png',dpi=400)
    plt.clf()
 
 
print('Done!')