t = 43.5  #tempo dado em minutos
d = 10    #distância dada em km

d_mil = d/1.61   #operação para transformar km em milhas
t_h = t/3600     #operação para transformar tempo de segundos para horas

v_mil_h = d_mil/t_h    #equação para achar a velocidade em milhas/h
t_mil_h = 1/v_mil_h    #equação para achar o tempo médio por milha

print('A velocidade média em milhas é:', v_mil_h)
print('O tempo médio por milha é:', t_mil_h)