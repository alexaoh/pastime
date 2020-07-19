import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.animation as animation
import matplotlib as mpl

# Some examples of what can be changed. 
# Recommendation: Attempt changing other things also. 
mpl.rcParams['figure.figsize'] = [12, 6] 


def analytic_solution(r, t, dim = 1):
    """One possible analytic solution to the diffusion equation.
    
    The initial condition is a Dirac-Delta function at t=0.
    You have to specify the dimension you are working with.
    """
    D = 1 
    return (1/(4*np.pi*D*t))**(dim/2)*np.exp(-r**2/(4*D*t))
    

L = 1.5 # E.g. length of x-axis. 

mesh = 1000
x = np.linspace(-L,L,mesh+1) # E.g. # of points. 
y = np.linspace(-L,L,mesh+1)
xv, yv = np.meshgrid(x,y)

# Animation stuff.
fps = 10 # frame per sec.
frn = 90 # frame number of the animation.

sol = np.zeros((mesh+1, mesh+1, frn))

for i in range(1, frn):
    temp = analytic_solution(np.sqrt(xv**2+yv**2),0.01*i, dim = 2)
    #temp[np.abs(temp[:,:]) < 1e-2] = 0.0
    #temp = np.clip(temp, None, 1.3) # Clips large values. 
    sol[:, :, i] = temp


def update_plot(frame_number, sol, plot):
    plot[0].remove()
    plot[0] = ax.plot_surface(xv, yv, sol[:,:,frame_number], cmap="bwr")

fig = plt.figure()
ax = fig.gca(projection='3d')

plot = [ax.plot_surface(xv, yv, sol[:,:,0], color='0.75', rstride=1, cstride=1)]
ax.set_zlim(0,1.3)

# Get rid of all 'overhead' in the figure. 
ax.xaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('white')
ax.yaxis.pane.fill = False
ax.yaxis.pane.set_edgecolor('white')
ax.zaxis.pane.fill = False
ax.zaxis.pane.set_edgecolor('white')
ax.w_zaxis.line.set_lw(0.)
ax.w_xaxis.line.set_lw(0.)
ax.w_yaxis.line.set_lw(0.)
ax.set_zticks([])
ax.set_yticks([])
ax.set_xticks([])

ani = animation.FuncAnimation(fig, update_plot, frn, fargs=(sol, plot), interval=1000/fps)

fn = 'Dirac_Diffusion_Anim'
ani.save(fn+'.gif',writer='imagemagick',fps=fps)
#plt.show()