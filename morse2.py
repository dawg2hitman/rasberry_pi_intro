import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Define Basics
dot = 0.4
dash = 3 * dot
post_d = dot
space_l = dash - post_d
space_w = 7 * dot - post_d

# Define Letters
A = a =[dot, dash]
B = b =[dash, dot, dot, dot]
C = c =[dash, dot, dash, dot]
D = d =[dash, dot, dot]
E = e =[dot]
F = f =[dot, dot, dash, dot]
G = g =[dash, dash, dot]
H = h =[dot, dot, dot, dot]
I = i =[dot, dot]
J = j =[dot, dash, dash, dash]
K = k =[dash, dot, dash]
L = l =[dot, dash, dot, dot]
M = m =[dash, dash]
N = n =[dash, dot]
O = o =[dash, dash, dash]
P = p =[dot, dash, dash, dot]
Q = q =[dash, dash, dot, dash]
R = r =[dot, dash, dot]
S = s =[dot, dot, dot]
T = t =[dash]
U = u =[dot, dot, dash]
V = v =[dot, dot, dot, dash]
W = w =[dot, dash, dash]
X = x =[dash, dot, dot, dash]
Y = y =[dash, dot, dash, dash]
Z = z =[dash, dash, dot, dot]

# Message letters only #NO SPACES#
m1 = 'HAMRADIOISFORLOSERS'

while True:
    i0 = 0
    x0 = 0
    for val1 in m1:
        x0 = globals()[val1]
        print (x0)
        j0 = 0
        
        #while j0 < len(x0):
        for val2 in x0:    
            GPIO.output(18, True)
            time.sleep(val2)
            GPIO.output(18, False)
            time.sleep(post_d)
            
        GPIO.output(18, False)
        time.sleep(space_l)
        
    GPIO.output(18, False)
    time.sleep(space_)