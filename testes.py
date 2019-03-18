import numpy as np
import tensorflow
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.python.keras.models import load_model

from cube import Cube

c = []
solutions = []
total = 1000000
for i in range(total):
    print(f"\r{i+1} of {total} - {(i+1)*100/total}%", end="")
    cube = Cube(2, 5)
    sequence = cube.sequence[::-1]
    if sequence[0][2] == '-1':
        sequence[0][2] = '1'
    elif sequence[0][2] == '1':
        sequence[0][2] = '-1'
    c.append([cube.get_numeric('R'),
              cube.get_numeric('L'),
              cube.get_numeric('U'),
              cube.get_numeric('D'),
              cube.get_numeric('F'),
              cube.get_numeric('B')])
    solutions.append(cube.numeric_sequence(sequence))
print()
df = [c, solutions]

split = int(len(df[0]) * 0.80)
cubes_training = np.array(df[0][:split])
solutions_training = np.array(df[1][:split])
cubes_test = np.array(df[0][split:])
solutions_test = np.array(df[1][split:])

model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=cubes_training[0].shape))
model.add(keras.layers.Dense(36, activation=tensorflow.nn.relu))
model.add(keras.layers.Dense(solutions_training.shape[1], activation=tensorflow.nn.softmax))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

historico = model.fit(cubes_training, solutions_training, epochs=5)

model.save('modelo.h5')
modelo_salvo = load_model('modelo.h5')

plt.plot(historico.history['acc'])
plt.title('Acurácia por épocas')
plt.xlabel('épocas')
plt.ylabel('acurácia')
plt.legend(['treino', 'validação'])
plt.show()

testes = model.predict(cubes_test)
print('resultado teste:', np.argmax(testes[1]))

testes_modelo_salvo = modelo_salvo.predict(cubes_test)
resultado = ''
print('resultado teste modelo salvo:', testes_modelo_salvo[1])
for x in testes_modelo_salvo[1]:
    resultado += str(int(round(x*10))) + ' '
print('resultado teste modelo salvo:', resultado)
# print('cubo', '\n', cubes_test[1])
print('sequencia de passos do teste:', solutions_test[1])

perda_teste, acuracia_teste = model.evaluate(cubes_test, solutions_test)
print('Perda do teste:', perda_teste)
print('Acurácia do teste:', acuracia_teste)
