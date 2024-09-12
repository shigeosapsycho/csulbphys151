from vpython import *

canvas(background = color.white)
G = 6.67e-11

def simulation(m_sun, m_earth, v_sun, v_earth, pos_sun, pos_earth):
    sun = sphere(pos = pos_sun, radius = 2e10, color = color.orange)
    earth = sphere(pos = pos_earth, radius = 6.4e9, color = color.blue, make_trail = True)
    
    sun.m = m_sun
    sun.v = v_sun
    sun.p = sun.m * sun.v
    
    earth.m = m_earth
    earth.v = v_earth
    earth.p = earth.m * earth.v
    
    t = 0
    dt = 60  # Reduce time step for higher accuracy (60 seconds)
    T = 0
    period_count = 0  # Counter to ensure we print the period only once per orbit
    
    while t < 2 * 365 * 24 * 3600:  # Simulate for 2 years to ensure we capture at least 1 orbit
        rate(100000)
        r = earth.pos - sun.pos
        old_vel = earth.v.x
        F_e = G * sun.m * earth.m / r.mag2 * (-r.hat)
        earth.p += F_e * dt
        earth.v = earth.p / earth.m
        earth.pos += earth.v * dt
        
        F_s = -F_e
        sun.p += F_s * dt
        sun.v = sun.p / sun.m
        sun.pos += sun.v * dt
        
        # Detect when the Earth completes one orbit (crosses the positive x-axis)
        if old_vel > 0 and earth.v.x < 0 and period_count == 0:
            print("Period is: ", T / 24 / 3600, "days")
            period_count += 1  # Ensure we print only once for the orbit
            T = 0  # Reset the period timer
        T += dt     
        t += dt


# Adjust the Earth's velocity to a more accurate value
simulation(m_sun = 1.989e30, m_earth = 5.97219e24, 
           v_sun = vector(0, 0, 0), v_earth = vector(0, 29784.8, 0),
           pos_sun = vector(0, 0, 0), pos_earth = vector(1.496e11, 0, 0))
