class Vecteur2D:      #définir une classe vecteur2D
    def __init__(self, a=0, b=0): #déclraer un constructeur par défaut
        self.x = a  # initialisation de a et b
        self.y = b
    def __str__(self):
        return "x = %d, y = %d" % (self.x, self.y) #retorner la valeur de x et y
print(" le vecteur2D sans parametre est: ")
print(Vecteur2D()) #afiche le constrecteur sans parametre
print(" le vecteur2D avec parametre est: ")
print(Vecteur2D(1, 6))  #afiche le constrecteur avec parametre
