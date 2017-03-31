import numpy
import random
from matplotlib import pyplot


fig = pyplot.figure(0)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.clear()

class Date( object ):
    def __init__(self):
        self.A = numpy.random.random()*60.0
        self.B = numpy.random.random()*60.0

    def success(self):
        return numpy.abs(self.A - self.B) < 15.0


avg_1 = []
success_1 = 0.0
avg_2 = []
success_2 = 0.0
avg_3 = []
success_3 = 0.0

for i in range(1000000):
    d1 = Date()
    d2 = Date()
    d3 = Date()
    if d1.success():
        success_1 += 1.0
    avg_1.append(success_1/(i+1))
    if d2.success():
        success_2 += 1.0
    avg_2.append(success_2/(i+1))
    if d3.success():
        success_3 += 1.0
    avg_3.append(success_3/(i+1))


ax.plot(avg_1, color = 'r')
ax.plot(avg_2, color = 'b')
ax.plot(avg_3, color = 'g')

fig.show()

fig.savefig('SuccessFraction.png")
