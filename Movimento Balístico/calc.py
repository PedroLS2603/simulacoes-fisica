import math as m

gravidade = 9.80665 #m/s^2
densidade_ar = 1.2754 #kg/m^3

# ** Equações eixo X ** #

class semResistencia:
    def v0_x(v_inicio, ang_inicio):
        ang_inicio = m.radians(ang_inicio)
        cos_ang = round(m.cos(ang_inicio), 6)

        return round(v_inicio * cos_ang, 6)

    def pos_x(tempo, ang_inicio, v_inicio):
        vel = semResistencia.v0_x(v_inicio, ang_inicio)

        return round((vel * tempo), 4)

    # ** Equações eixo y ** #

    def v0_y(v_inicio, ang_inicio):
        ang_inicio = m.radians(ang_inicio)
        sen_ang = round(m.sin(ang_inicio), 6)

        return round(v_inicio * sen_ang, 6)

    def v_y(v_inicio, ang_inicio, tempo):
        v0y = semResistencia.v0_y(v_inicio, ang_inicio)

        return round(v0y - round(gravidade * tempo, 6), 6)

    def pos_y(tempo, ang_inicio, inicio, v_inicio):
        v0y = semResistencia.v0_y(v_inicio, ang_inicio)

        return round(inicio + v0y * tempo - ((gravidade * (m.pow(tempo, 2)))/2), 4)

    # **      Outros     ** #

    def ang(v_x, v_y):
        tg_ang = v_y / v_x

        return m.degrees(m.atan(tg_ang))

    def v_t(v_inicio, ang_inicio, tempo):
        return round(m.sqrt(m.pow(semResistencia.v0_x(v_inicio, ang_inicio), 2) + m.pow(semResistencia.v_y(v_inicio, ang_inicio, tempo), 2)), 4)


class comResistencia:

    def area_circulo(diametro):
        return round((m.pi * diametro ** 2)/4, 6)

    def coef_arrasto():
        area = comResistencia.area_circulo(1)
        return round(0.5 * 0.47 * densidade_ar * area, 6)

    # Equações eixo x
    def v0_x(v_inicio, ang_inicio):
        ang_inicio = m.radians(ang_inicio)
        cos_ang = round(m.cos(ang_inicio), 6)

        return round(v_inicio * cos_ang, 6)

    def v_x(massa, v_inicio, ang_inicio, tempo):
        v0 = comResistencia.v0_x(v_inicio, ang_inicio)
        ca = comResistencia.coef_arrasto()

        return round( v0 * m.e ** (ca / massa) * tempo, 4)

    def pos_x(massa, tempo, ang_inicio, v_inicio):
        v0 = comResistencia.v0_x(v_inicio, ang_inicio)
        ca = comResistencia.coef_arrasto()

        return round((v0/ca) * ( 1 - m.e ** ((-ca * tempo))), 4)

    # ** Equações eixo y ** #

    def v0_y(v_inicio, ang_inicio):
        ang_inicio = m.radians(ang_inicio)
        sen_ang = round(m.sin(ang_inicio), 6)

        return round(v_inicio * sen_ang, 6)

    def v_y(massa, v_inicio, ang_inicio, tempo):
        v0y = comResistencia.v0_y(v_inicio, ang_inicio)
        ca = comResistencia.coef_arrasto()

        return round(((v0y + ((gravidade * massa)/ca)) * m.e ** (-(ca/massa) * tempo)) - ((gravidade * massa)/ca), 6)

    def pos_y(massa, tempo, ang_inicio, v_inicio):
        v0y = comResistencia.v0_y(v_inicio, ang_inicio)
        ca = comResistencia.coef_arrasto()


        return round(((massa/ca) * (v0y + (gravidade * massa)/ca) * (1 - m.e ** (-(ca/massa) * tempo))) - (((gravidade * massa)/ca) * tempo), 4)

    # **      Outros     ** #

    def ang(v_x, v_y):
        tg_ang = v_y / v_x

        if(v_x == 0):
            return 0

        return m.degrees(m.atan(tg_ang))

    def v_t(massa, v_inicio, ang_inicio, tempo):
        return round(m.sqrt(m.pow(comResistencia.v_x(massa, v_inicio, ang_inicio, tempo), 2) + m.pow(comResistencia.v_y(massa, v_inicio, ang_inicio, tempo), 2)), 4)