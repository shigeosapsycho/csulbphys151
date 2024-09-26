from vpython import *

canvas(background = color.white)

# step 1 
#create objects

def create_objects(L0):
    ceiling = box(pos = vec(0, 0, 0), size = vec(0.1, 3, 3), color = color.black)

    platform = box(pos = vec(5, -.5, 0), size = vec(10, .1, 3), color = color.black)

    spring = helix(pos = ceiling.pos, axis = vec(L0, 0, 0), color = color.red)

    ball = sphere(pos = spring.pos + spring.axis, radius = 0.4, color = color.blue)
    
    return ceiling, spring, ball

# step 2
# set_up

def set_up(ball, spring, mass, k, v, strectch):
    ball.m = mass
    ball.v = v
    ball.p = ball.v * ball.m
    spring.k = k
    spring.L0 = spring.axis.mag
    spring.axis = spring.axis + vec(strectch,0, 0)
    ball.pos = spring.pos + spring.axis

# step 3
# simulation 

def simulation(ceiling, spring, ball, dt):
    rate(100)
    delta_L = spring.axis.mag - spring.L0
    F_sp = -spring.k * delta_L * spring.axis.hat
    F_g = vec(0, -9.8,0) * ball.m
    F_f = mu * ball.m * 9.81 * -ball.v.hat
    F = F_sp + F_f
    ball.p +=  F * dt
    ball.v = ball.p / ball.m
    ball.pos += ball.v * dt 
    spring.axis = ball.pos - spring.pos

def set_up_graph(title, x_label, y_label):
    g = graph(title = title, xtitle = x_label, ytitle = y_label)
    c1 = gcurve(graph = g, color = color.red)
    c2 = gcurve(graph = g, color = color.blue)
    return g, c1, c2 

def plot(g, c1, c2, x1, y1, x2, y2):
    c1.plot(x1,y1)
    c2.plot(x2, y2)

#######################################################################################
L0 = 2
mass = 2
k = 5
v = vec(0, 0, 0)
strectch = 0.2
mu = 0.01
ceiling, spring, ball = create_objects(L0)
set_up(ball, spring, mass, k, v, strectch)
velocity_graph, v_x, v_y = set_up_graph("velocity", "t", "v_x")
mom_graph, p_x, p_y = set_up_graph("Momentum", "t", "p")
t = 0
T = 0 
dt = 0.05
old_velocity_count = 0
while t < 10:
    old_velocity = ball.v.y

    simulation(ceiling, spring, ball, dt)
    plot(velocity_graph, v_x, v_y, t, ball.v.x, t, ball.v.y)
    plot(mom_graph, p_x, p_y, t, ball.p.x, t, ball.p.y)
   
    if old_velocity < 0 and ball.v.y > 0:
        old_velocity_count += 1
    if old_velocity_count == 3:
        print(f"the period is {T}") 

    t += dt
