def d_mi_m(d_mil):      #função que converte milhas em metros
    d_m = d_mil* 1610   #equação para converter milhas em metros
    return d_m          #comando para retornar o valor em metros

def d_m_mi(d_m):        #função para converter metros em milhas
    d_mil = d_m / 1610
    return d_mil

def t_h_s(h):            #função para converter horas em segundos
    t_s = t_h * 3600
    return t_s

def t_s_h(s):            #função que converte segundos em horas
    t_h = t_s/3600
    return t_h


#Exercício da aula 1

t = 43.5 * 60  #tempo dado em segundos
d = 10*1000    #distância dada em metros

d2_mil = d_m_mi(d)   #aplica a função na variável d
t_h2 = t_s_h(t)      #aplica a função na variável t

t_mil_h = (t_h2) / (d2_mil)   #equação para o tempo médio por milha em horas
v_mil_h = 1/t_mil_h           #equação para achar a velocidade média em milhas por hora

print('A velocidade média em milhas por hora é:', v_mil_h)
print('O tempo médio por milha em hora é:', t_mil_h)


#Exercício da aula 3

d3_mil = 4   #distância dada em milhas
t_h3 = 0.5   #tempo dado em horas

d2_m = d_mi_m(d3_mil)   #aplica a função na variável d3_mil
d_km = d2_m / 1000      #transforma d2_m em km

v_med = d_km / t_h3     #velocidade média em km/h
t_med = 1/ v_med        #tempo médio por km em horas

print('A velocidade média em km/h é:', v_med)
print('O tempo médio por km em horas é:', t_med)
