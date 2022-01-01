class Point:#définir la classe point
    def __init__(self, x=0.0, y=0.0):
        self.x1 = float(x)   #Initialiser avec valeurs par defaut
        self.y1 = float(y)
class Segment:    #classe composite utilisant la classe Point.
    def __init__(self, a, b, c, d):    #L'initialisation utilise deux objets Point

        self.orig = Point(a, b)
        self.extrem = Point(c, d)
    def display(self):  #Representation d'un objet segment.
        print("[(",self.orig.x1,",", self.orig.y1,")", "(",self.extrem.x1,"," ,self.extrem.y1,")]")
Se = Segment(3, 9, 1, 4)
Se.display()