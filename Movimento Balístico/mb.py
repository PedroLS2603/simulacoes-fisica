import matplotlib.pyplot as plt
from IPython.display import display
import pandas as pd
from calc import semResistencia as sr
from calc import comResistencia as cr

ang_inicio = float(input("Digite o ângulo: "))
v_inicio = float(input("Digite a velocidade inicial: "))
inicio = float(input("Digite a posição inicial: "))
intervalo = 0
massa = 2

intervalos = []
posicoes_x = []
posicoes_y = []
vel_x = []
vel_y = []
vel_t = []
comp_vx = []
comp_vy = []
angs = []

intervalos2 = []
posicoes_x2 = []
posicoes_y2 = []
vel_x2 = []
vel_y2 = []
vel_t2 = []
comp_vx2 = []
comp_vy2 = []
angs2 = []

while(intervalo >= 0):
    
    pos_x = sr.pos_x(intervalo, ang_inicio, v_inicio)
    pos_y = sr.pos_y(intervalo, ang_inicio, inicio, v_inicio)
    v0x = sr.v0_x(v_inicio, ang_inicio)
    v0y = sr.v0_y(v_inicio, ang_inicio)
    vx = v0x #velocidade constante
    vy = sr.v_y(v_inicio, ang_inicio, intervalo)
    vt = sr.v_t(v_inicio, ang_inicio, intervalo)

    if intervalo > 0:
        ang = sr.ang(sr.v0_x(v_inicio, ang_inicio), sr.v_y(v_inicio, ang_inicio, intervalo))
    else:
        ang = ang_inicio

    intervalos.append(intervalo)
    posicoes_x.append(pos_x)
    posicoes_y.append(pos_y)
    comp_vx.append(v0x)
    comp_vy.append(v0y)
    vel_x.append(vx)
    vel_y.append(vy)
    vel_t.append(vt)
    angs.append(ang)

    if intervalo > 0 and pos_y <= 0:
        break

    intervalo += 0.1

intervalo = 0


while (intervalo >= 0):
    pos_x2 = cr.pos_x(massa, intervalo, ang_inicio, v_inicio)
    pos_y2 = cr.pos_y(massa, intervalo, ang_inicio, v_inicio)
    v0x2 = cr.v0_x(v_inicio, ang_inicio)
    v0y2 = cr.v0_y(v_inicio, ang_inicio)
    vx2 = cr.v_x(massa, v_inicio, ang_inicio, intervalo)
    vy2 = cr.v_y(massa, v_inicio, ang_inicio, intervalo)
    vt2 = cr.v_t(massa, v_inicio, ang_inicio, intervalo)

    if intervalo > 0:
        ang2 = cr.ang(cr.v_x(massa, v_inicio, ang_inicio, intervalo), cr.v_y(massa, v_inicio, ang_inicio, intervalo))
    else:
        ang2 = ang_inicio


    posicoes_x2.append(pos_x2)
    posicoes_y2.append(pos_y2)
    comp_vx2.append(v0x2)
    comp_vy2.append(v0y2)
    vel_x2.append(vx2)
    vel_y2.append(vy2)
    vel_t2.append(vt2)
    angs2.append(ang2)

    if intervalo > 0 and pos_y2 <= 0:
        break

    intervalo += 0.1

plt.figure('Movimento balístico')
plt.ylabel('Altura (m)')
plt.xlabel('Distância (m)')
plt.plot(posicoes_x, posicoes_y)
plt.plot(posicoes_x2, posicoes_y2)
plt.legend(["Sem resistência", "Com resistência"])
plt.xlim(left = -1)

planilha = pd.DataFrame({'T (s)': intervalos, 'X (m)':posicoes_x, 'Y (m)': posicoes_y, 'V0x (m/s)': comp_vx, 'V0y (m/s)': comp_vy, 'Vx (m/s)': vel_x, 'Vy (m/s)': vel_y, 'Vt (m/s)': vel_t, 'α (°)': angs})

display(planilha)


plt.show()



