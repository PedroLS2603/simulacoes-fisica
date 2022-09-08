import math as m

gravidade = 9.80665

# ** Equações eixo X ** #

def v0_x(v_inicio, ang_inicio):
    ang_inicio = m.radians(ang_inicio)
    cos_ang = round(m.cos(ang_inicio), 6)

    return round(v_inicio * cos_ang, 6)

def pos_x(tempo, ang_inicio, v_inicio):
    vel = v0_x(v_inicio, ang_inicio)

    return round(vel * tempo, 4)

# ** Equações eixo y ** #

def v0_y(v_inicio, ang_inicio):
    ang_inicio = m.radians(ang_inicio)
    sen_ang = round(m.sin(ang_inicio), 6)

    return round(v_inicio * sen_ang, 6)

def v_y(v_inicio, ang_inicio, tempo):
    v0y = v0_y(v_inicio, ang_inicio)

    return round(v0y - round(gravidade * tempo, 6), 6)

def pos_y(tempo, ang_inicio, inicio, v_inicio):
    v0y = v0_y(v_inicio, ang_inicio)

    return round(inicio + v0y * tempo - ((gravidade * (m.pow(tempo, 2)))/2), 4)

# **      Outros     ** #

def ang(v_x, v_y):
    tg_ang = v_y / v_x

    return m.degrees(m.atan(tg_ang))

def v_t(v_inicio, ang_inicio, tempo):
    return round(m.sqrt(m.pow(v0_x(v_inicio, ang_inicio), 2) + m.pow(v_y(v_inicio, ang_inicio, tempo), 2)), 4)
