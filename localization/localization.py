### Programing example developpend during class.

# Initial probabilistic pose (position)
p=[0.2, 0.2, 0.2, 0.2, 0.2]

## World -----------------------------------------
# World colormarks description
world=['green', 'red', 'red', 'green', 'green']
# Measurements recorded on each step
measurements = ['red', 'red']

## Motion -----------------------------------------
# steps vector
motions = [1,1]
# probability of moving exacctly,
pExact = 0.8
# too much
pOvershoot = 0.1
# too few
pUndershoot = 0.1
def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q


## Sensing -----------------------------------------
# factor for getting color right
pHit = 0.6
# factor for getting color wrong 
pMiss = 0.2
def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

## Program execution -------------------------------
for k in range(len(measurements)):
    p = sense(p, measurements[0])
    p = move(p, motions[k])
    
print p         

