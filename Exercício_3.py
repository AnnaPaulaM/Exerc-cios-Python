import math

def ang_zen(alt, comp):
    ang_zen = math.atan(comp/alt)   #equação para achar o ângulo zenital
    print('O ângulo zenital é:', ang_zen)