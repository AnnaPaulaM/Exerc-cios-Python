import math           #importando a bilioteca de matemática

def imc(a, m):        #definição da função imc
    i_m_c = m / (a**2)  #calculo do imc
    return i_m_c        #retorno do valor do imc

def vol_esf(r):       #definição da função volume de esfera
    v_esf =  (4/3) * math.pi * (r**3)   #equação para achar o volume de uma esfera
    return v_esf

def d_max(comp_onda, d_ant, d_fen):
    del_y = (comp_onda * d_ant) / d_fen #equação para distância entre máximos
    return d_y


#argumentos para cálculo

a = 1.89    #altura em metros
m = 97      #massa em kg
r = 5       #raio
comp_onda = 632.8
d_ant 1.98
d_fen = 0.25

#aplicando os argumentos nas funções

i_m_c = imc(a,m)
v_esf = vol_esf(r)
d_max = d_max(comp_onda, d_ant, d_fen)


print('O IMC é:', i_m_c)
print('O Volume da esfera é:', v_esf)
print('A distância máxima é:', d_max)