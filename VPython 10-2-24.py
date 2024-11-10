from vpython import *

canvas(background=color.white)

def create_objects(L):
    ceiling = box(pos=vec(0, 0, 0), size=vec(2, 0.1, 2), color=color.black)
    string = cylinder(pos=ceiling.pos, axis=vec(0, -L, 0), radius=0.1, texture="https://i.imgur.com/1j1vZ9y.jpg")
    ball = sphere(pos=string.pos + string.axis, radius=0.2, texture="https://t3.ftcdn.net/jpg/05/12/62/42/360_F_512624218_TpcoZSJm1JAQtn5DlvJ0Js7HVgrXfmwr.jpg")
    return ceiling, string, ball

def set_up(ball, string, mass, angle):
    theta = radians(angle)  # angle * pi / 180
    string.L = string.axis.mag
    string.axis = string.L * vec(sin(theta), -cos(theta), 0)
    ball.pos = string.pos + string.axis
    ball.m = mass

    ball.omega = 0  # this is like ball .v
    ball.theta = theta  # this is like ball.pos
    ball.p = ball.m * (ball.omega * string.L)

def set_up_graph(title, x_label, y_label): # We are graphing Time vs Angular Velocity and Time vs Theta
    g = graph(title=title, xtitle=x_label, ytitle=y_label)
    c1 = gcurve(graph=g, color=color.red)
    c2 = gcurve(graph=g, color=color.blue)
    return g, c1, c2

def plot(g, c1, c2, x1, y1, x2, y2):
    c1.plot(x1, y1)
    c2.plot(x2, y2)

def simulation(ball, string, dt):
    g = 9.8
    F = -ball.m * g * sin(ball.theta)
    ball.p += F * dt
    ball.omega = ball.p / (ball.m * string.L)
    ball.theta += ball.omega * dt

    ball.pos = string.L * vec(sin(ball.theta), -cos(ball.theta), 0)
    string.axis = ball.pos - string.pos

########################################################################
L = 2
mass = 10
angle = 45

t = 0
T = 0  # Period accumulator
dt = 0.05
old_velocity_count = 0  # To count the zero crossings
ceiling, string, ball = create_objects(L)
set_up(ball, string, mass, angle)
a_graph, theta_curve, omega_curve = set_up_graph("Angular Velocity and Theta", "t", "theta and omega")

prev_omega = ball.omega  # Store the previous omega to detect zero crossings

while t < 20:
    rate(100)  # Run the loop 100 times per second
    simulation(ball, string, dt)

    plot(a_graph, theta_curve, omega_curve, t, ball.theta, t, ball.omega)
    
    # Check for a zero crossing (from negative omega to positive omega)
    if prev_omega < 0 and ball.omega > 0:
        old_velocity_count += 1
        if old_velocity_count == 3:  # We've seen three zero crossings
            T = t / 3  # Calculate the average period (based on 3 oscillations)
            print(f"The period is approximately {T:.3f} seconds")
    
    prev_omega = ball.omega  # Update previous omega
    t += dt