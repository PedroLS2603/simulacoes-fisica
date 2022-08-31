import math as m

gravidade = 9.80665

def pos_x(tempo, ang, v_inicio):

    return round((v_inicio * round(m.cos(m.radians(ang)), 6) * tempo), 4)

def pos_y(tempo, ang, inicio, v_inicio):
    return round(inicio + (v_inicio * round(m.sin(m.radians(ang)), 6) * tempo) - (gravidade * m.pow(tempo, 2))/2, 4) 

