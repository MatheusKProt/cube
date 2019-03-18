import numpy as np
from tensorflow.python.keras.models import load_model

from cube import Cube

modelo_salvo = load_model('modelo2.h5')

cube = Cube(2, 5)
print(cube.sequence)
cube.print_cube()

testes_modelo_salvo = modelo_salvo.predict([[[cube.get_numeric('R'),
                                              cube.get_numeric('L'),
                                              cube.get_numeric('U'),
                                              cube.get_numeric('D'),
                                              cube.get_numeric('F'),
                                              cube.get_numeric('B')]]])

resultado = ''
print('resultado teste modelo salvo:', testes_modelo_salvo[0])
for x in testes_modelo_salvo[0]:
    resultado += str(int(round(x*10))) + ' '
print('resultado teste modelo salvo:', resultado)

