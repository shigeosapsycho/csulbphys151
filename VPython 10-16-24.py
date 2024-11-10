from vpython import *

canvas(background=color.white)

# Constants:
G = 6.7e-11
mu = 0

s1 = sphere(pos=vec(-1.1e11,0,0), mass = 2e24, radius = 70*7e8, color=color.orange, make_trail = True) 
s2 = sphere(pos=vec(1.5e11,0,0), mass = 1e24, radius = 6*6.4e8, color=color.magenta, make_trail = True)

s1.p = s1.mass*vec(0,10,0)
s2.p = -s1.p

# Initial values:
work = 0
# Define iniial kinetic energy:
KE_initial = 0.5*(mag(s1.p)**2/s1.mass + mag(s2.p)**2/s2.mass)
# Define distance between two bodies:
R = mag(s2.pos - s1.pos)
#Initial potential energy:
PE_initial = -G*s1.mass*s2.mass/R

# Plotting stuff:
graph_p = graph(title='Binary Star Momentum', xtitle='t', ytitle='p(t)')

p_s1_x = gcurve(graph=graph_p, color=color.red)
p_s1_y = gcurve(graph=graph_p, color=color.green)
p_s1_z = gcurve(graph=graph_p, color=color.blue)

p_s2_x = gcurve(graph=graph_p, color=color.red)
p_s2_y = gcurve(graph=graph_p, color=color.green)
p_s2_z = gcurve(graph=graph_p, color=color.blue)

graph_p_total = graph(title='Binary Star Total Momentum', xtitle='t', ytitle='p(t)')

p_total_x = gcurve(graph=graph_p_total, color=color.red)
p_total_y = gcurve(graph=graph_p_total, color=color.green)
p_total_z = gcurve(graph=graph_p_total, color=color.blue)

work_graph = graph(title='Binary Star Work', xtitle='t', ytitle='p(t)')

D_KE = gcurve(graph=work_graph, color=color.red)
D_PE = gcurve(graph=work_graph, color=color.green)

energy_gr = graph(title='Binary star Energy', xtitle='t', ytitle='w(t)')
KE = gcurve(graph=energy_gr, color=color.red)
PE = gcurve(graph=energy_gr, color=color.green)
total_energy = gcurve(graph=energy_gr, color=color.green)

R_E_gr = graph(title='Energy v.s. Distance', xtitle='r', ytitle='e')
Kr = gcurve(graph=R_E_gr, color=color.red)
Pr = gcurve(graph=R_E_gr, color=color.orange)
total_energy = gcurve(graph=R_E_gr, color=color.green)

t = 0
dt = 30*24*60*60

while t < 5*365*24*60*60:
    rate(1000)
    
    # Calculate the force between the two bodies:
    R = mag(s2.pos - s1.pos)
    F = -G*s1.mass*s2.mass*R.norm()/R**2
    
    