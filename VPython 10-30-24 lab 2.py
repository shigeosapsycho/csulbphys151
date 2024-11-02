from vpython import *

canvas(background=color.white)

def create_objects(R):
    ramp = ring(pos=vec(0,0,0), axis=vec(0,0,1), radius=R, opacity=0.5, thickness=0.5, color=color.green)
    car = box(pos=vec(R,-R, 0), size=vec(10,20,10), color=color.red, make_trail=True)
    return car

def set_up(car, speed, mass):
    car.m = mass
    car.v = vec(0, speed, 0)
    car.p = car.m * car.v
    car.K = 0

def simulation(car):
    rate(500)
    F = vec(0,0,0)
    if car.pos.x < 0 or car.pos.y > 0:
        F = mu * car.m * 9.8 * (-car.pos.hat)
        
    car.p = car.p + F * dt
    car.v = car.p / car.m
    car.pos = car.pos + car.v * dt
    car.K = 1 / 2 * car.m * car.v.mag2

def set_up_graph(title, x_label, y_label):
    g = graph(title=title, xtitle=x_label, ytitle=y_label)
    c1 = gcurve(graph=g, color=color.red)
    c2 = gcurve(graph=g, color=color.blue)
    return g, c1, c2

def plot(c1, c2, x1, y1, x2, y2):
    c1.plot(pos=(x1, y1))
    c2.plot(pos=(x2, y2))

####################################################################################
R = 100
mass = 100
mu = 0.2
speed = (mu*R*9.8)**0.5
print(speed)

car = create_objects(R)
set_up(car, speed, mass)
energy_graph, kinetic_curve, zero_curve = set_up_graph('Energy', 't', 'J')
t = 0
dt = 0.01

while car.pos.x < 2*R:
    simulation(car)
    plot(kinetic_curve, zero_curve, t, car.K, t, 0)
    t += dt
