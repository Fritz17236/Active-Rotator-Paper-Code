import matplotlib.pyplot as ppl
import numpy as np
from PIL import Image
import matplotlib.image as mpimg


name_list = [str(i) for i in range(0,100)]
data = np.genfromtxt('C:\\Users\\fritz\\Desktop\\Model for Nonlinear Oscillators\\fig3_bData.csv', delimiter=',',
                    names=['ts', 'coherence',])




img1 = mpimg.imread('C:\\Users\\fritz\\Desktop\\Model for Nonlinear Oscillators\\K1b0.jpg')
img2 = mpimg.imread('C:\\Users\\fritz\\Desktop\\Model for Nonlinear Oscillators\\K1bPoint5.jpg')
img3 = mpimg.imread('C:\\Users\\fritz\\Desktop\\Model for Nonlinear Oscillators\\K1bPoint95.jpg')
img4 = mpimg.imread('C:\\Users\\fritz\\Desktop\\Model for Nonlinear Oscillators\\K1bPoint99.jpg')

ppl.figure(1)
ppl.subplot(221)
ppl.imshow(img1)
ppl.axis('off')

ppl.subplot(222)
ppl.imshow(img2)
ppl.axis('off')


ppl.subplot(223)
ppl.imshow(img3)
ppl.axis('off')


ppl.subplot(224)
ppl.imshow(img4)
ppl.axis('off')

#ppl.plot(data['ts'],data['coherence'])
#ppl.xlabel('Time (s)')
#ppl.ylabel('Extracted Phase')

ppl.show()
#for i in range(0,100):
#    ppl.plot(data['ts'],data[str(i)],linewidth=1.0,color='r' )
#ppl.plot(data['ts'],data['coherence'],linewidth=2.0,color='black')
#ppl.plot(data['ts'],data['coherence'])
#ppl.plot(data['ts'],data['calc_phase'])
#ppl.xlabel('Time')
#ppl.ylabel('Coherence')
#ppl.title('Periodic Stability in an Ensemble of Simulated Neurons')

#ppl.plot([0, 1],[1, 1])
#$ppl.legend('Coherence')
#ppl.axis([0.0,1, 0,1.05])

#ax = ppl.gca()
#ax.set_autoscale_on(False)
ppl.show()

"""
#for subplots, Two subplots, the axes array is 1-d
f, axarr = ppl.subplots(2, sharex=True)
axarr[0].plot(data['ts'],data['xa'])
axarr[0].plot(data['ts'],data['xb'])
axarr[0].plot(data['ts'],data['xc'])
axarr[0].plot(data['ts'],data['xd'])
axarr[0].plot(data['ts'],data['xe'])
axarr[0].set_title('Phase versus Time for A Single Oscillator')
axarr[1].plot(data['ts'],np.sin(data['xe']))
axarr[1].set_title('Sine of Phase versus Time (b = .99)')
#axarr[0].xlabel('Time (s)')
ppl.xlabel('Time (s)')
#axarr[0].ylabel('Phase (rad)')
#axarr[1].ylabel('Sine of Phase')
ppl.show()
"""


