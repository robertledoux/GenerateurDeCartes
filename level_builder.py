import numpy
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
import re
import csv

def maze(width=81, height=51, complexity=.75, density=.75):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1]))) # number of components
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2))) # size of components
    # Build actual maze
    Z = numpy.zeros(shape, dtype=bool)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2 # pick a random position
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    return Z


def plaine(width=81, height=51, density=.75):
    # Only odd shapes
    longueur = (height // 2) * 2 + 1
    largeur = (width // 2) * 2 + 1
    shape = (longueur, largeur)
    # Adjust complexity and density relative to maze size
    density    = rand(15,50) # size of components
    # Build actual maze
    Z = numpy.zeros(shape)

    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles

    #on ajoute sur la carte des pierres
    densite_or = rand(1, 5)
    for i in range(0, density):
        x, y = rand(0, shape[1] - 1), rand(0, shape[0] - 1) # pick a random position
        rect_l = rand(2, 6)
        rect_L = rand(2, 6)

        for u in range(1, rect_l):
            for v in range(1, rect_L):
                if u+x != 0 and v+y != 0 and u+x <longueur - 1 and v+y < largeur -1:
                    if rand(1, densite_or) == 1:
                        Z[u+x, v+y] =  216
                    else:
                        Z[u+x, v+y] =  1

    #on ajoute de l'eau
    volume_eau = rand(10,30)

    for i in range(1, volume_eau):
        x, y = rand(1, shape[1] - 2), rand(1, shape[0] - 2) # pick a random position
        Z[y, x] = 130
        larg = rand(2, 10)
        longe = rand(2, 6)

        for u in range(1, longe):
            for v in range(1, larg):
                if u+x != 0 and v+y != 0 and u+x <longueur - 2 and v+y < largeur -2:
                    Z[u + x, v +y] = 130

    #on ajoute des arbres
    foret = rand(15,50)

    for i in range(1, foret):
        x, y = rand(2, shape[1]/2 - 3)*2, rand(2, shape[0]/3 - 5)*3
        if y + 2 < largeur -2 and x+1 <longueur - 2:
            Z[y, x] = 13
            Z[y, x + 1] = 14
            Z[y + 1, x] = 15
            Z[y + 1, x + 1] = 16
            Z[y + 2, x] = 17
            Z[y + 2, x + 1] = 18

    return Z

nombre_de_cartes = 10
for i in range(1,nombre_de_cartes):
    if rand(0,10) > 7:
        pyplot.figure(figsize=(10, 5))
        #pyplot.imshow(maze(60, 40), cmap=pyplot.cm.binary, interpolation='nearest')
        #pyplot.xticks([]), pyplot.yticks([])
        #pyplot.show()

        a = maze(60, 39)
        carte = []
        collision = []
        evenement = []
        layer2 = []
        layer4 = []
        for el in a:
            carte_temp = []
            collision_temp = []
            event_temp = []
            layer2_temp = []
            layer4_temp = []
            j = 0
            for e in el:
                if e == True:
                    if j == 0 or j == 38:
                        carte_temp.append(5)
                        collision_temp.append(1)
                        layer2_temp.append(35)
                        layer4_temp.append(0)
                        event_temp.append(0)
                    elif rand(0,10)/10 < 0.95:
                        carte_temp.append(5)
                        collision_temp.append(1)
                        layer2_temp.append(35)
                        layer4_temp.append(0)
                        event_temp.append(0)
                    else:
                        carte_temp.append(5)
                        collision_temp.append(0)
                        layer2_temp.append(0)
                        layer4_temp.append(0)
                        event_temp.append(0)
                else:
                    carte_temp.append(5)
                    collision_temp.append(0)
                    layer2_temp.append(0)
                    layer4_temp.append(0)
                    event_temp.append(0)
            carte.append(carte_temp)
            collision.append(collision_temp)
            evenement.append(event_temp)
            layer2.append(layer2_temp)
            layer4.append(layer4_temp)
            j = j + 1

        carte[10].pop()
        carte[10].append(5)
        carte[9].pop()
        carte[9].append(5)
        carte[8].pop()
        carte[8].append(5)

        layer2[10].pop()
        layer2[10].append(5)
        layer2[9].pop()
        layer2[9].append(5)
        layer2[8].pop()
        layer2[8].append(5)

        collision[10].pop()
        collision[10].append(0)
        collision[9].pop()
        collision[9].append(0)
        collision[8].pop()
        collision[8].append(0)

        evenement[10].pop()
        evenement[10].pop(0)
        evenement[10].append(6)
        evenement[10].insert(0, 15)
        evenement[9].pop()
        evenement[9].pop(0)
        evenement[9].append(6)
        evenement[9].insert(0, 15)
        evenement[8].pop()
        evenement[8].pop(0)
        evenement[8].append(6)
        evenement[8].insert(0, 15)


        carte[10].pop(0)
        carte[10].insert(0,5)
        carte[9].pop(0)
        carte[9].insert(0,5)
        carte[8].pop(0)
        carte[8].insert(0,5)

        layer2[10].pop(0)
        layer2[10].insert(0,5)
        layer2[9].pop(0)
        layer2[9].insert(0,5)
        layer2[8].pop(0)
        layer2[8].insert(0,5)

        collision[10].pop(0)
        collision[10].insert(0,0)
        collision[9].pop(0)
        collision[9].insert(0,0)
        collision[8].pop(0)
        collision[8].insert(0,0)


        f = open('base' + str(i) +'.map.json','w+')
        a = '{"Level": { "charas": [["bunny", 50,  8],["bunny2", 55, 13],["bunny2", 50,  7],["rock", 12, 32],["rock", 12, 33],["bunny2", 37, 14], ["bunny2", 38, 13],["bunny_forest", 34, 26]], "collision": '
        f.write(a)
        f.write(str(collision))
        f.write(',')
        f.write('\n')
        f.write('"events": ')
        f.write(str(evenement))
        f.write(',')
        
        if i == 1:
            f.write('    "eventsActions":{"6": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","0;16;Villa"],["fadeIn","pixelizeFadeIn;doNotKeep"]], "15": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","59;10;base'+str(i+1)+'"],["fadeIn","pixelizeFadeIn;doNotKeep"]]},"eventsType": {"6":  [  0,  1,  0,  0,  0], "15":  [  0,  1,  0,  0,  0]},"layer1":')           
        elif i != nombre_de_cartes - 1:
            f.write('    "eventsActions":{"6": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","0;10;base'+str(i-1)+'"],["fadeIn","pixelizeFadeIn;doNotKeep"]], "15": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","59;10;base'+str(i+1)+'"],["fadeIn","pixelizeFadeIn;doNotKeep"]]},"eventsType": {"6":  [  0,  1,  0,  0,  0], "15":  [  0,  1,  0,  0,  0]},"layer1":')
        else:
            f.write('    "eventsActions":{"6": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","0;10;base'+str(i-1)+'"],["fadeIn","pixelizeFadeIn;doNotKeep"]], "15": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","28;11;Villa"],["fadeIn","pixelizeFadeIn;doNotKeep"]]},"eventsType": {"6":  [  0,  1,  0,  0,  0], "15":  [  0,  1,  0,  0,  0]},"layer1":')            
        f.write(str(carte))
        f.write(',')
        f.write('\n')
        f.write('"layer2":')
        f.write(str(layer2))
        f.write(',')
        f.write('\n')
        f.write('"layer4":')
        f.write(str(layer4))
        f.write(',')
        f.write('"levelName": "Base","tileImage": "img/tile.png","tiles": {"0":  [  0,  0],"1":  [  2, 11],"2":  [  1, 14],"3":  [  0, 16],"4":  [  1, 16],"5":  [  4, 14],"6":  [  0, 17],"7":  [  1, 17],"8":  [  2, 16],"9":  [  3, 13],"10":  [  5, 13],"11":  [  3, 15],"12":  [  5, 15],"13":  [  6, 17],"14":  [  7, 17],"15":  [  6, 18],"16":  [  7, 18],"17":  [  6, 19],"18":  [  7, 19],"19":  [  6, 14],"20":  [  7, 14],"21":  [  8, 14],"22":  [  6, 15],"23":  [  7, 15],"24":  [  8, 15],"25":  [  6, 16],"26":  [  7, 16],"27":  [  8, 16],"28":  [  9, 15],"29":  [  9, 16],"30":  [  8, 17],"31":  [  8, 18],"32":  [  8, 19],"33":  [  6, 20],"34":  [  7, 20],"35":  [ 8, 26],"130":  [ 9, 6],"131":  [ 10, 6]},"tilesAnimated": {}}}')

        f.close()

    else:
        pyplot.figure(figsize=(10, 5))
        #pyplot.imshow(maze(60, 40), cmap=pyplot.cm.binary, interpolation='nearest')
        #pyplot.xticks([]), pyplot.yticks([])
        #pyplot.show()

        a = plaine(60, 39, 0.4)
        carte = []
        collision = []
        evenement = []
        layer2 = []
        layer4 = []
        for el in a:
            carte_temp = []
            collision_temp = []
            event_temp = []
            layer2_temp = []
            layer4_temp = []
            j = 0
            for e in el:
                if e == 1:
                    if j == 0 or j == 38:
                        carte_temp.append(5)
                        collision_temp.append(1)
                        layer2_temp.append(35)
                        layer4_temp.append(0)
                        event_temp.append(0)
                    elif rand(0,10)/10 < 0.95:
                        carte_temp.append(5)
                        collision_temp.append(1)
                        layer2_temp.append(0)
                        layer4_temp.append(0)
                        event_temp.append(0)
                    else:
                        carte_temp.append(5)
                        collision_temp.append(1)
                        layer2_temp.append(35)
                        layer4_temp.append(0)
                        event_temp.append(0)
                elif e == 0:
                    if rand(0, 10) == 1:
                        carte_temp.append(8)
                    else:
                        carte_temp.append(5)
                    collision_temp.append(0)
                    layer2_temp.append(0)
                    layer4_temp.append(0)
                    event_temp.append(20)
                elif e == 130:
                    carte_temp.append(130)
                    collision_temp.append(0)
                    layer2_temp.append(0)
                    layer4_temp.append(0)
                    event_temp.append(0)
                elif e == 13:
                    carte_temp.append(5)
                    layer2_temp.append(0)
                    layer4_temp.append(13)
                    collision_temp.append(0) 
                    event_temp.append(0)
                elif e == 14:
                    carte_temp.append(5)
                    layer2_temp.append(0)
                    layer4_temp.append(14)
                    collision_temp.append(0) 
                    event_temp.append(0) 
                elif e == 15:
                    carte_temp.append(5)
                    layer2_temp.append(15)
                    layer4_temp.append(0)
                    collision_temp.append(1)
                    event_temp.append(0)
                elif e == 16:
                    carte_temp.append(5)
                    layer2_temp.append(16)
                    layer4_temp.append(0)
                    collision_temp.append(1)
                    event_temp.append(0)
                elif e == 17:
                    carte_temp.append(5)
                    layer2_temp.append(17)
                    layer4_temp.append(0)
                    collision_temp.append(1)
                    event_temp.append(0)
                elif e == 18:
                    carte_temp.append(5)
                    layer2_temp.append(18)
                    layer4_temp.append(0)
                    collision_temp.append(1)
                    event_temp.append(0)
                elif e == 216:
                    carte_temp.append(216)
                    layer2_temp.append(0)
                    layer4_temp.append(0)
                    collision_temp.append(1)
                    event_temp.append(13)

            carte.append(carte_temp)
            collision.append(collision_temp)
            evenement.append(event_temp)
            layer2.append(layer2_temp)
            layer4.append(layer4_temp)
            j = j + 1

        carte[10].pop()
        carte[10].append(5)
        carte[9].pop()
        carte[9].append(5)
        carte[8].pop()
        carte[8].append(5)

        
        layer2[10].pop()
        layer2[10].append(5)
        layer2[9].pop()
        layer2[9].append(5)
        layer2[8].pop()
        layer2[8].append(5)

        collision[10].pop()
        collision[10].append(0)
        collision[9].pop()
        collision[9].append(0)
        collision[8].pop()
        collision[8].append(0)

        evenement[10].pop()
        evenement[10].append(6)
        evenement[10].pop(0)
        evenement[10].insert(0, 15)
        evenement[9].pop()
        evenement[9].append(6)
        evenement[9].pop(0)
        evenement[9].insert(0, 15)
        evenement[8].pop()
        evenement[8].append(6)
        evenement[8].pop(0)
        evenement[8].insert(0, 15)


        carte[10].pop(0)
        carte[10].insert(0,5)
        carte[9].pop(0)
        carte[9].insert(0,5)
        carte[8].pop(0)
        carte[8].insert(0,5)

        layer2[10].pop(0)
        layer2[10].insert(0,5)
        layer2[9].pop(0)
        layer2[9].insert(0,5)
        layer2[8].pop(0)
        layer2[8].insert(0,5)

        collision[10].pop(0)
        collision[10].insert(0,0)
        collision[9].pop(0)
        collision[9].insert(0,0)
        collision[8].pop(0)
        collision[8].insert(0,0)


        f = open('base' + str(i) +'.map.json','w+')
        a = '{"Level": { "charas": [["bunny", 50,  8],["bunny2", 55, 13],["bunny2", 50,  7],["rock", 12, 32],["rock", 12, 33],["bunny2", 37, 14], ["bunny2", 38, 13],["bunny_forest", 34, 26]], "collision": '
        f.write(a)
        f.write(str(collision))
        f.write(',')
        f.write('\n')
        f.write('"events": ')
        f.write(str(evenement))
        f.write(',')
        
        if i == 1:
            f.write('    "eventsActions":{"6": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","0;16;Villa"],["fadeIn","pixelizeFadeIn;doNotKeep"]], "15": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","59;10;base'+str(i+1)+'"],["fadeIn","pixelizeFadeIn;doNotKeep"]], "13": [["playAnimationInMap","gold;0;current"],["changeTile","217;layer1;nocollision;20;current"], ["addItem","Or"]], "20": [["playAnimationInMap","gold;0;current"],["changeTile","216;layer1;collision;13;current"]]},"eventsType": {"6":  [  0,  1,  0,  0,  0], "15":  [  0,  1,  0,  0,  0], "13":  [  1,  0,  0,  0,  0], "20":  [  1,  0,  0,  0,  0]},"layer1":')           
        elif i != nombre_de_cartes - 1:
            f.write('    "eventsActions":{"6": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","0;10;base'+str(i-1)+'"],["fadeIn","pixelizeFadeIn;doNotKeep"]], "15": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","59;10;base'+str(i+1)+'"],["fadeIn","pixelizeFadeIn;doNotKeep"]], "13": [["playAnimationInMap","gold;0;current"],["changeTile","217;layer1;nocollision;20;current"], ["addItem","Or"]], "20": [["playAnimationInMap","gold;0;current"],["changeTile","216;layer1;collision;13;current"]]},"eventsType": {"6":  [  0,  1,  0,  0,  0], "15":  [  0,  1,  0,  0,  0], "13":  [  1,  0,  0,  0,  0], "20":  [  1,  0,  0,  0,  0]},"layer1":')
        else:
            f.write('    "eventsActions":{"6": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","0;10;base'+str(i-1)+'"],["fadeIn","pixelizeFadeIn;doNotKeep"]], "15": [["fadeOut","pixelizeFadeOut;keepEffect"],["playMusic","forest"],["teleport","28;11;Villa"],["fadeIn","pixelizeFadeIn;doNotKeep"]], "13": [["playAnimationInMap","gold;0;current"],["changeTile","217;layer1;nocollision;20;current"], ["addItem","Or"]], "20": [["playAnimationInMap","gold;0;current"],["changeTile","216;layer1;collision;13;current"]]},"eventsType": {"6":  [  0,  1,  0,  0,  0], "15":  [  0,  1,  0,  0,  0], "13":  [  1,  0,  0,  0,  0], "20":  [  1,  0,  0,  0,  0]},"layer1":')            
        f.write(str(carte))
        f.write(',')
        f.write('\n')
        f.write('"layer2":')
        f.write(str(layer2))
        f.write(',')
        f.write('\n')
        f.write('"layer4":')
        f.write(str(layer4))
        f.write(',')
        f.write('"levelName": "Base","tileImage": "img/tile.png","tiles": {"0":  [  0,  0],"1":  [  2, 11],"2":  [  1, 14],"3":  [  0, 16],"4":  [  1, 16],"5":  [  4, 14],"6":  [  0, 17],"7":  [  1, 17],"8":  [  2, 16],"9":  [  3, 13],"10":  [  5, 13],"11":  [  3, 15],"12":  [  5, 15],"13":  [  6, 17],"14":  [  7, 17],"15":  [  6, 18],"16":  [  7, 18],"17":  [  6, 19],"18":  [  7, 19],"19":  [  6, 14],"20":  [  7, 14],"21":  [  8, 14],"22":  [  6, 15],"23":  [  7, 15],"24":  [  8, 15],"25":  [  6, 16],"26":  [  7, 16],"27":  [  8, 16],"28":  [  9, 15],"29":  [  9, 16],"30":  [  8, 17],"31":  [  8, 18],"32":  [  8, 19],"33":  [  6, 20],"34":  [  7, 20],"35":  [ 8, 26], "130":  [ 9, 6],"131":  [ 10, 6], "132":  [ 0, 49], "216":  [ 1, 49], "217":  [ 2, 49]},"tilesAnimated": {}}}')

        f.close()