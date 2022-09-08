import matplotlib.pyplot as plt
import pandas as pd
import calc as c

ang_inicio = float(input("Digite o ângulo: "))
v_inicio = float(input("Digite a velocidade inicial: "))
inicio = float(input("Digite a posição inicial: "))
intervalo = 0

intervalos = []
posicoes_x = []
posicoes_y = []
vel_x = []
vel_y = []
vel_t = []
comp_vx = []
comp_vy = []
angs = []

while(intervalo >= 0):
    
    pos_x = c.pos_x(intervalo, ang_inicio, v_inicio)
    pos_y = c.pos_y(intervalo, ang_inicio, inicio, v_inicio)
    v0x = c.v0_x(v_inicio, ang_inicio)
    v0y = c.v0_y(v_inicio, ang_inicio)
    vx = v0x #velocidade constante
    vy = c.v_y(v_inicio, ang_inicio, intervalo)
    vt = c.v_t(v_inicio, ang_inicio, intervalo)

    if intervalo > 0:
        ang = c.ang(c.v0_x(v_inicio, ang_inicio), c.v_y(v_inicio, ang_inicio, intervalo))
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

    if intervalo > 0 and pos_y < 0:
        break

    intervalo += 0.1


plt.figure('Movimento balístico')
plt.ylabel('Altura')
plt.xlabel('Distância')
plt.plot(posicoes_x, posicoes_y)
plt.xlim(left = -1)

planilha = pd.DataFrame({'T (s)': intervalos, 'X (m)':posicoes_x, 'Y (m)': posicoes_y, 'V0x (m/s)': comp_vx, 'V0y (m/s)': comp_vy, 'Vx (m/s)': vel_x, 'Vy (m/s)': vel_y, 'Vt (m/s)': vel_t, 'α (°)': angs})

print(planilha)

plt.show()



