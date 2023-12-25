import numpy as np
import matplotlib.pyplot as plt

a=500
panjang = 2.5
waktu = 1
node = 50

dx = panjang/node
dt = 0.5*dx**2/a
t_n = int(waktu/dt)
u = np.zeros(node) + 20

u[0] = 0
u[-1] = 100
fig, ax = plt.subplots()
ax.set_xlabel("x(cm)")
pcm = ax.pcolormesh([u], cmap = plt.cm.jet, vmin = 0, vmax=100)
plt.colorbar(pcm, ax=ax)
ax.set_ylim([-2, 3])

w = u.copy()
for i in range (1, node -1):
    u[i] = dt*a*(w[i-1] - 2*w[i] + w[i+1]  / dx**2) +w[i]
counter = dt
print("t: {:.3f} s, suhu rata-rata: {:.2f} Celcius".format(counter, np.mean(u)))
pcm.set_array([u])
ax.set_title ("Distribusi suhu pada t: {:.3f} s".format(counter))
plt.show()
