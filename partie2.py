class Etudiant:  #définir la clase Etudiant
    def _init_(self, nom, prenom, age, cne, moyenne):    #définir un constrecteur
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne

# list de type etudiant
Etudiant = [ {'nom': 'Taibi', 'prenom': 'Asmae', 'age': 23, 'cne': 'E13487553', 'moyenne':16},
    {'nom': 'Zaidi', 'prenom': 'Inssaf', 'age': 20, 'cne': 'P1326797', 'moyenne': 15},
    {'nom': 'Kadmiri', 'prenom': 'Malika', 'age': 22, 'cne': 'G156774', 'moyenne': 17},]

print(" la Liste triee par age est :")
Etudiant.sort(key=lambda x: x.get('age'))   # trie par age par la fonction sort
print(Etudiant)  #afficher la liste trie par age
print("\nla  Liste triee par moyenne est :")
Etudiant.sort(key=lambda x: x.get('moyenne'))  # trie par moyenne
print(Etudiant)  #afficher la liste trie par age

