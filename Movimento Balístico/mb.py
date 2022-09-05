import matplotlib.pyplot as plt
import calc as c

angulo = float(input("Digite o ângulo: "))
v_inicio = float(input("Digite a velocidade inicial: "))
inicio = float(input("Digite a posição inicial: "))
intervalo = 0

posicoes_x = []
posicoes_y = []


while(intervalo >= 0):
    
    pos_x = c.pos_x(intervalo, angulo, v_inicio)
    pos_y = c.pos_y(intervalo, angulo, inicio, v_inicio)
    posicoes_x.append(pos_x)
    posicoes_y.append(pos_y)
    
    if intervalo > 0:
        print("velocidade x:", c.v_x(v_inicio, angulo, intervalo))
        ang = c.ang(c.v_x(v_inicio, angulo, intervalo), c.v_y(v_inicio, angulo, intervalo))
        print("Ângulo: {0:.2f}".format(ang))
    if intervalo > 0 and pos_y < 0:
        break

    intervalo += 0.1


plt.figure('Movimento balístico')
plt.ylabel('Altura')
plt.xlabel('Distância')
plt.plot(posicoes_x, posicoes_y)
plt.xlim(left = -1)
plt.xlim(right = 1000)

plt.show()

