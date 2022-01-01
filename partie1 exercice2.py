class vecteur2D:  #definir une class vecteur2D
    def __init__(self, x=0, y=0):      #définir un constructeur sans parametre et avec parametre
        self.x = x
        self.y = y
    def affiche(self): #declarer une methode pour afficher pour qu'on peut afficher les vecteurs
        print("x: %d , y: %d" % (self.x, self.y))

    def __add__(self, other): # déclarer la méthode add pour faire l'additon
        x1 = self.x + other.x
        y1 = self.y + other.y
        v = vecteur2D(x1, y1)
        return v #retourner la valeur de v
    def somme(self): #déclarer une méthode pour afficher la somme
        return "la somme de deux vecteurs V3(" + str(self.x) + "," + str(self.y) + ")"
# affiche le vecteur par defaut
print("le vecteur par defaut est:")
Vd = vecteur2D()
Vd.affiche()
print("le vecteur V1")
V1 = vecteur2D(9, 3)
V1.affiche()
print("le vecteur V2")
V2 = vecteur2D(1, 6)
V2.affiche() #faire l'addition
V3 = V1 + V2
# afficher la somme
print(V3.somme())