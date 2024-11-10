from vpython import *

canvas(background = color.white)

def create_objects():
    # road = box(pos=vec(0, -0.3, 0), size=vec(100, 0.1, 2), color=color.black)
    car_1 = box(pos=vec(-5, 0, 0), size=vec(1, 0.5, 0.5), color=color.red, make_trail=True)
    car_2 = box(pos=vec(5, 0, 0), size=vec(1, 0.5, 0.5), color=color.blue, make_trail=True)
    return car_1, car_2

def set_up(car_1, car_2, m_1, m_2, v_1, v_2):
    car_1.m = m_1
    car_1.v = v_1
    car_1.p = car_1.m * car_1.v
    
    car_2.m = m_2
    car_2.v = v_2
    car_2.p = car_2.m * car_2.v

def simulation(car_1, car_2):
    rate(500)
    F_1 = vec(0, 0, 0)
    F_2 = vec(0, 0, 0)
    
    r = car_1.pos - car_2.pos
    if mag(r) < interaction_range:
        F_1 = k_interaction * (interaction_range - mag(r)) * r.hat
        F_2 = -F_1
    
    car_1.p = car_1.p + F_1 * dt
    car_1.v = car_1.p / car_1.m
    car_1.pos += car_1.v * dt
    
    car_2.p = car_2.p + F_2 * dt
    car_2.v = car_2.p / car_2.m
    car_2.pos += car_2.v * dt
    
def set_up_graph(title, x_label, y_label):
    g = graph(title=title, xtitle=x_label, ytitle=y_label)
    c1 = gcurve(graph=g, color=color.red)
    c2 = gcurve(graph=g, color=color.blue)
    return g, c1, c2

def plot(c1, c2, x1, y1, x2, y2):
    c1.plot(pos=(x1, y1))
    c2.plot(pos=(x2, y2))

####################################################################################
m_1 = 2
m_2 = 2
v_1 = vec(10, 0, 0)
v_2 = vec(-1, 0, 0)

interaction_range = 1
k_interaction = 1000
# Prediction
v_1_f = ((m_1 - m_2) * v_1.x + 2 * m_2 * v_2.x) / (m_1 + m_2)
v_2_f = ((m_2 - m_1) * v_2.x + 2 * m_1 * v_1.x) / (m_1 + m_2)

print("Prediction, v_1_f = ", v_1_f, "v_2_f = ", v_2_f)



car_1, car_2 = create_objects()
set_up(car_1, car_2, m_1, m_2, v_1, v_2)

g_momentum, m1_curve, m2_curve = set_up_graph('Momentum vs Time', 't (s)', 'p')
g_energy, e1_curve, e2_curve = set_up_graph('Kinetic Energy vs Time', 't (s)', 'KE')

t = 0
dt = 0.005

while t < 3:
    simulation(car_1, car_2)
    t += dt

    plot(m1_curve, m2_curve, t, car_1.p.x + car_2.p.x, t, 0)
    plot(e1_curve, e2_curve, t, (0.5*car_1.m*car_1.v.x**2)+(0.5*car_2.m*car_2.v.x**2), t, 0)
print("From the simulation, v_1_f = ", car_1.v.x, "v_2_f = ", car_2.v.x)
