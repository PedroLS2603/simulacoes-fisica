import math as m

gravidade = 9.80665

def pos_x(tempo, ang, v_inicio):
    return round(v0_x(v_inicio, ang) * tempo, 4)

def pos_y(tempo, ang, inicio, v_inicio):
    return round(inicio + v0_y(v_inicio, ang) * tempo - (gravidade * m.pow(tempo, 2))/2, 4)

def v0_y(v_inicio, ang):
    return round(v_inicio * round(m.sin(m.radians(ang)), 6), 6)

def v_y(v_inicio, ang, tempo):
    return round(v0_y(v_inicio, ang) - round(gravidade * tempo, 6), 4)

def v0_x(v_inicio, ang):
    return round(v_inicio * round(m.cos(m.radians(ang)) , 6), 6)

def v_x(v_inicio, ang, tempo):
    return round(v0_x(v_inicio, ang) * tempo, 6)

def v_t(v_inicio, ang):
    return round(v_x(v_inicio, ang) + v_y(v_inicio, ang), 4)


