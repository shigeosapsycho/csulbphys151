from vpython import *

canvas(background=color.white)

def create_objects(L0):
    # Create the ceiling, spring, and ball
    ceiling = box(pos=vector(0, 0, 0), size=vector(3, 0.1, 3), color=color.black)
    spring = helix(pos=ceiling.pos, axis=vector(0, -L0, 0), radius=0.3, color=color.red)
    ball = sphere(pos=spring.pos + spring.axis, radius=0.2, color=color.blue)
    
    # Return the objects
    return ceiling, spring, ball

def set_up(spring, ball, mass, k, v, stretch):
    # Initialize the ball's momentum, velocity, and position
    ball.m = mass
    ball.v = v
    ball.p = ball.m * ball.v
    
    # Initialize the spring's properties
    spring.k = k
    spring.L0 = spring.axis.mag
    spring.axis = spring.axis + vec(0, -stretch, 0)
    
    ball.pos = spring.pos + spring.axis

def simulation(ceiling, spring, ball):
    rate(100)
    
    # Forces
    F_sp = -spring.k * (spring.axis.mag - spring.L0) * spring.axis.hat
    F_g = ball.m * vec(0, -9.8, 0)
    F = F_g + F_sp
    
    # Update momentum, velocity, and position of the ball
    ball.p = ball.p + F * dt
    ball.v = ball.p / ball.m
    ball.pos = ball.pos + ball.v * dt
    
    # Update the spring's axis
    spring.axis = ball.pos - spring.pos

def set_up_graph(title, x_label, y_label):
    # Create a graph
    g = graph(title=title, xtitle=x_label, ytitle=y_label)
    c1 = gcurve(color=color.red)
    c2 = gcurve(color=color.blue)
    return g, c1, c2

def plot(g, c1, c2, x1, y1, x2, y2):
    c1.plot(pos=(x1, y1))
    c2.plot(pos=(x2, y2))

L0 = 2
mass = 2
k = 5
v = vec(0,0,0)
stretch = 0.2

ceiling, spring, ball = create_objects(L0)
set_up(spring, ball, mass, k, v, stretch)
vel_graph, v_x, v_y = set_up_graph("Velocity vs. Time", "Time (s)", "Velocity (m/s)")
m_graph, m_x, m_y = set_up_graph("Momentum vs. Time", "Time (s)", "Momentum (kg*m/s)")
t = 0
dt = 0.05

# Period detection variables
period_count = 0
T = 0  # Timer for the period
equilibrium_length = L0 + (mass * 9.8) / k
y_eq = -equilibrium_length  # Since ceiling.pos.y is 0
old_pos_y = ball.pos.y

while t < 10:
    simulation(ceiling, spring, ball)
        
    plot(vel_graph, v_x, v_y, t, ball.v.x, t, ball.v.y)
    plot(m_graph, m_x, m_y, t, ball.p.x, t, ball.p.y)
            
    T += dt
    t += dt

    # Detect when the ball crosses the equilibrium position moving upwards
    if old_pos_y < y_eq and ball.pos.y >= y_eq:
        if period_count == 0:
            # First crossing, start the timer
            T = 0
            period_count = 1
        else:
            print("Period is:", T, "seconds")
            period_count += 1
            T = 0  # Reset the period timer
    old_pos_y = ball.pos.y
