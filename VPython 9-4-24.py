from vpython import (box, color, cos, radians, rate, sin, sphere, vec, graph, gcurve)

def Simulation(speed, angle, height, mass):
    radius = 0.3

    ground = box(pos = vec(0, 0, 0), size = vec(5, 0.1, 5), color = color.green)
    tower = box(pos = vec(0, height/2, 0), size = vec(0.5, height, 0.5), opacity = 0.5, color = color.blue)
    ball = sphere(pos = vec(0, height + radius, 0), radius = 0.3, color = color.red)
    stone = sphere(pos = vec(0, height + radius, 0), radius = 0.3, color = color.yellow, make_trail = True)
    
    theta = radians(angle)

    
    stone.m = mass
    stone.v = speed * vec(cos(angle), sin(angle), 0)
    stone.p = stone.m * stone.v
    
    ball.m = mass
    ball.v = speed * vec(cos(angle), sin(angle), 0)
    ball.p = ball.m * ball.v
    
    vx_graph = graph(title= "x-velocity", xtitle= "t", ytitle= "vx")
    vy_graph = graph(title= "y-velocity", xtitle= "t", ytitle= "vy")
    
    vx_stone = gcurve(graph = vx_graph, color = color.red)
    vy_stone = gcurve(graph = vy_graph, color = color.red)
    vx_ball = gcurve(graph = vx_graph, color = color.blue)
    vy_ball = gcurve(graph = vy_graph, color = color.blue)
    
    t = 0
    dt = 0.0005

    while stone.pos.y >= 0:
        rate(2000)
        F = vec(0, 0, 0)
        Fg = vec(0, -9.81 * stone.m, 0) # Remember F_g = m * g

        ball.p += F * dt # ball.p + f * dt
        ball.v = ball.p / ball.m
        ball.pos += ball.v * dt # ball.pos + ball.v * dt
        
        stone.p += Fg * dt # stone.p + g * dt
        stone.v = stone.p / stone.m
        stone.pos += stone.v * dt # stone.pos + stone.v * dt
        
        vx_stone.plot(pos = (t, stone.v.x))
        vy_stone.plot(pos = (t, stone.v.y))
        vx_ball.plot(pos = (t, ball.v.x))
        vy_ball.plot(pos = (t, ball.v.y))

        t += dt # t + dt

    
Simulation(speed = 1, angle = 1, height = 1, mass = 1)

"""
Theory is about the phyics
Method is about the code

"""
