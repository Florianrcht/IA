from keras import *
import numpy as np

model = Sequential()

model.add(layers.Dense(units=50, input_shape=[1])) #ENTREE Premiere couche dense (neuronnes interconnectés) avec 3 neuronnes et un tableau de 1

model.add(layers.Dense(units=8)) #CACHEE 
model.add(layers.Dense(units=8)) #CACHEE 
model.add(layers.Dense(units=8)) #CACHEE 
model.add(layers.Dense(units=8)) #CACHEE 
model.add(layers.Dense(units=8)) #CACHEE 
model.add(layers.Dense(units=8)) #CACHEE 
model.add(layers.Dense(units=8)) #CACHEE 
model.add(layers.Dense(units=8)) #CACHEE 


#1 Couche de 64 neuronnes : loss 6.4400e-05
#4 Couche de 16 neuronnes : loss: 4.9005e-10
#8 Couche de 8 neuronnes : loss: 7.3896e-13 => Méthode gardée
#16 Couche de 4 neuronnes : loss: 6.9349e-13
#32 Couche de 2 neuronnes : loss: 1.2460e-11

model.add(layers.Dense(units=1)) #SORTIE donne le resultat

entree = np.array([1, 2, 3, 4, 5])  #Input
sortie = np.array([2, 4, 6, 8, 10])  #Target

#L'IA va essayer de trouver la corelation entre l'entree et la sortie (ici la multiplication par deux)

model.compile(loss='mean_squared_error', optimizer='adam')
##Régression
#loss mean_squared_error : une valeur est bonne quand le carré de l'écart à la moyenne devient minimal (MSE)
#On calcule l'écart entre la valeur cible (sortie) et la valeur prédite par le modèle, on élève cet écart au carré (pour éviter que les erreurs positives et négatives se compensent mutuellement), puis on fait la moyenne de ces carrés d'erreurs sur un nombre d'échantillons.
#Plus le MSE est bas, plus on se rapproche de la valeur cible (sortie)

##Optimizer
#Adam : Calcule mathématique pour optimiser 

model.fit(x=entree, y=sortie, epochs=1000)
#epochs : nombre de tours que fera l'ia pour s'améliorer et baisser son loss

while True:
    x = int(input('Nombre :'))
    print('Prédiction : ' + str(model.predict(np.array([x]))[0][0])) 