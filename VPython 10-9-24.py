from vpython import *

def create_objects(height, radius):
    ground = box(pos=vec(0, 0, 0), size=vec(25, 0.1, 5), color=color.green)
    tower = box(pos=vec(0, height/2, 0), size=vec(0.5, height, 0.5), opacity=0.5, color=color.blue)
    ball = sphere(pos=vec(0, height + radius, 0), radius=radius, color=color.red)
    stone = sphere(pos=vec(0, height + radius, 0), radius=radius, color=color.yellow, make_trail=True)
    return ground, tower, ball, stone

def set_up(stone, ball, speed, angle, mass):
    theta = radians(angle)

    stone.m = mass
    stone.v = speed * vec(cos(theta), sin(theta), 0)
    stone.p = stone.m * stone.v
    stone.W = 0
    stone.K = 0
    stone.Ki = stone.p.mag2 / (2 * stone.m)
    
    ball.m = mass
    ball.v = speed * vec(cos(theta), sin(theta), 0)
    ball.p = ball.m * ball.v
    ball.W = 0
    ball.K = 0 
    ball.Ki = ball.p.mag2 / (2 * ball.m)

def simulation(stone, ball, dt):
    rate(1000)
    F = vec(0, 0, 0)
    Fg = vec(0, -9.81 * stone.m, 0)

    ball.p += F * dt
    ball.v = ball.p / ball.m
    ball.pos += ball.v * dt
    ball.k = ball.p.mag2 / (2 * ball.m)
    ball.W += dot(F, ball.v) * dt
        
    stone.p += Fg * dt
    stone.v = stone.p / stone.m
    stone.pos += stone.v * dt
    stone.k = stone.p.mag2 / (2 * stone.m)
    stone.W += dot(Fg, stone.v) * dt

def set_up_graph(title, x_label, y_label):
    g = graph(title=title, xtitle=x_label, ytitle=y_label)
    c1 = gcurve(graph=g, color=color.red)
    c2 = gcurve(graph=g, color=color.blue)
    return g, c1, c2

def plot(c1, c2, x1, y1, x2, y2):
    c1.plot(x1, y1)
    c2.plot(x2, y2)
    return c1, c2

########################################################################
speed = 10
angle = 30
height = 4
mass = 2
radius = 0.3

ground, tower, ball, stone = create_objects(height, radius)
set_up(stone, ball, speed, angle, mass)

kin_graph, stone_k, ball_k = set_up_graph("Kinetic Energy", "t", "K")
work_graph, stone_w, ball_w = set_up_graph("Work", "t", "W")

t = 0
dt = 0.0005

while stone.pos.y >= 0:
    simulation(stone, ball, dt)
    plot(stone_k, ball_k, t, stone.k - stone.Ki, t, ball.k - ball.Ki)
    plot(stone_w, ball_w, t, stone.W, t, ball.W)
    
    t += dt
