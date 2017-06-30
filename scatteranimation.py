import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

FLOOR = -10
CEILING = 10

class AnimatedScatter(object):
    def __init__(self, numpoints=5):
        self.numpoints = numpoints
        self.stream = self.data_stream()
        self.angle = 0

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111,projection = '3d')
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=100,
                                           init_func=self.setup_plot, blit=True)

    def change_angle(self):
        self.angle = (self.angle + 1)%360

    def setup_plot(self):
        X = next(self.stream)
        c = ['b', 'r', 'g', 'y', 'm']
        self.scat = self.ax.scatter(X[:,0], X[:,1], X[:,2] , c=c, s=200, animated=True)

        self.ax.set_xlim3d(FLOOR, CEILING)
        self.ax.set_ylim3d(FLOOR, CEILING)
        self.ax.set_zlim3d(FLOOR, CEILING)

        return self.scat,

    def data_stream(self):
        data = np.zeros(( self.numpoints , 3 ))
        xyz = data[:,:3]
        while True:
            xyz += 2 * (np.random.random(( self.numpoints,3)) - 0.5)
            yield data

    def update(self, i):
        data = next(self.stream)
        data = np.transpose(data)

        self.scat._offsets3d = ( np.ma.ravel(data[:,0]) , np.ma.ravel(data[:,0]) , np.ma.ravel(data[:,0]) )

        self.change_angle()
        self.ax.view_init(30,self.angle)
        plt.draw()
        return self.scat,

    def show(self):
        plt.show()

a = AnimatedScatter()
a.show()