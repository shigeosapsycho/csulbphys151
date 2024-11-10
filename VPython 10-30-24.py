from vpython import *

canvas(background=color.white)

def create_objects(L, r):
    ceiling = box(pos=vec(0, 0, 0), size=vec(2,0.1,2), color=color.black)
    spring = helix(pos=ceiling.pos, axis=vec(0, -L, 0), radius=0.5, color=color.red)
    ball = sphere(pos=spring.pos+spring.axis, radius=r, color=color.blue, make_trail=True)
    return spring, ball

def set_up(ball, spring, k, stretch, angle, mass):
    theta = radians(angle)
    spring.L0 = spring.axis.mag
    spring.axis = (spring.L0 + stretch) * vec(sin(theta), -cos(theta), 0)
    spring.k = k
    
    ball.m = mass
    ball.v = vec(0, 0, 0)
    ball.p = ball.m * ball.v
    ball.pos = spring.pos + spring.axis
    ball.Ki = 0.5 * ball.m * ball.v.mag2
    ball.K = 0
    ball.w_sp = 0
    ball.w_g = 0
    ball.w_d = 0

def simulation(spring, ball):
    rate(20000)
    F_sp = -spring.k * (spring.axis.mag - spring.L0) * spring.axis.hat
    F_g = ball.m * vec(0, -9.8, 0)
    F_D = 1 / 2 * c * rho * A * ball.v.mag2 * -ball.v.hat
    F = F_sp + F_g + F_D
    ball.p = ball.p + F * dt
    ball.v = ball.p / ball.m
    ball.pos = ball.pos + ball.v * dt
    ball.K = 0.5 * ball.m * ball.v.mag2
    
    spring.axis = ball.pos - spring.pos
    ball.w_sp = ball.w_sp + F_sp.dot(ball.v) * dt
    ball.w_g = ball.w_g + F_g.dot(ball.v) * dt
    ball.w_d = ball.w_d + F_D.dot(ball.v) * dt

def set_up_graph(title, xlabel, ylabel):
    g = graph(title=title, xtitle=xlabel, ytitle=ylabel)
    c1 = gcurve(graph=g, color=color.red)
    c2 = gcurve(graph=g, color=color.blue)
    return g, c1, c2

def plot(c1, c2, x1, y1, x2, y2):
    c1.plot(pos=(x1, y1))
    c2.plot(pos=(x2, y2))

################################################################################################################
L = 6
k = 10
stretch = 2
angle = 30
mass = 1
r = 0.5
c = 0.2
rho = 0.2
A = 4 * pi * r**2
energy_graph, kinetic_curve, work_curve = set_up_graph('Energy', 't', 'J')

spring, ball = create_objects(L, r)
set_up(ball, spring, k, stretch, angle, mass)

t = 0
dt = 0.0001
while t < 30:
    simulation(spring, ball)
    plot(kinetic_curve, work_curve, t, ball.K - ball.Ki, t, ball.w_sp + ball.w_g + ball.w_d)
    t += dt