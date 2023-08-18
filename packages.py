#from packaging.version import Version as StrictVersion
from PyQt5 import Qt
#from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
#from gnuradio.eng_arg import eng_float, intx
#from gnuradio import eng_notation
import sip


# importing the required module 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
    
# x axis values 
x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 
    
# plotting the points  
plt.plot(x, y) 
    
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
    
# giving a title to my graph 
plt.title('My first graph!') 
    
# function to show the plot 
plt.show() 