import math as m

gravidade = 9.80665

# ** Equações eixo X ** #

def v0_x(v_inicio, ang_inicio):
    return round(v_inicio * round(m.cos(m.radians(ang_inicio)) , 6), 6)

def v_x(v_inicio, ang_inicio, tempo):
    return round(v0_x(v_inicio, ang_inicio) * tempo, 6)

def pos_x(tempo, ang_inicio, v_inicio):
    return round(v0_x(v_inicio, ang_inicio) * tempo, 4)

# ** Equações eixo y ** #

def v0_y(v_inicio, ang_inicio):
    return round(v_inicio * round(m.sin(m.radians(ang_inicio)), 6), 6)

def v_y(v_inicio, ang_inicio, tempo):
    return round(v0_y(v_inicio, ang_inicio) - round(gravidade * tempo, 6), 4)

def pos_y(tempo, ang_inicio, inicio, v_inicio):
    return round(inicio + v0_y(v_inicio, ang_inicio) * tempo - (gravidade * m.pow(tempo, 2))/2, 4)

# **      Outros     ** #

def ang(v_x, v_y):
    tg_ang = v_y / v_x
    print(m.atan(tg_ang))

    return m.degrees(m.atan(tg_ang))

def v_t(v_inicio, ang_inicio):
    return round(v_x(v_inicio, ang_inicio) + v_y(v_inicio, ang_inicio), 4)
