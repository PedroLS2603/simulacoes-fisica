import math as m

gravidade = 9.80665

def pos_x(tempo, ang, inicio, v_inicio):
    return inicio + (v_inicio * m.cos(m.radians(ang)) * tempo)

def pos_y(tempo, ang, inicio, v_inicio):
    return inicio + (v_inicio * m.sin(m.radians(ang)) * tempo) - (gravidade * m.pow(tempo, 2))/2 
