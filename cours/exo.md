Enoncé
Construis ta première classe Python : une mini-calculatrice orientée objet
Vous allez créer une classe Python appelée Calculator qui permet d’effectuer des opérations simples entre deux nombres.

Cette classe doit :

être initialisée avec deux nombres (entiers ou décimaux) ;

proposer une méthode add() qui retourne la somme des deux nombres ;

proposer une méthode multiply() qui retourne le produit des deux nombres.

Votre classe doit également vérifier que les deux valeurs fournies lors de l’instanciation sont bien des types numériques (int ou float). Si ce n’est pas le cas, une exception de type TypeError doit être levée.

Une fois votre classe définie, créez une instance de Calculator avec les valeurs 3 et 5, puis affichez le résultat des deux méthodes.
-----------------------------
Ma solution 
import except
class Calculator:
    __init__(self,a,b):
        self.a=a 
        self.b=b
        
def add(a,b):
    
  try:
        if ((type(self.a) or type(self.b))==int or type(type(self.a) or type(self.b)==float)
        result= self.a+self.b
        
    except TypeError as e:
        print(e.args)
        
    return print(result)


def multiply(a,b):
     try:
        if ((type(self.a) or type(self.b))==int or type(type(self.a) or type(self.b)==float)
        result=self.a * self.b 
        
    except TypeError as e:
        print(e.args)
    
    return  print(result)









correction :
class Calculator:
    def __init__(self, a, b):
        self.a = a 
        self.b = b
        
    def add(self):
        try:
            # Vérifier que a et b sont des nombres (int ou float)
            if isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)):
                # Exclure les booléens (qui sont techniquement des int)
                if not isinstance(self.a, bool) and not isinstance(self.b, bool):
                    result = self.a + self.b
                    return result
                else:
                    raise TypeError("Les booléens ne sont pas acceptés")
            else:
                raise TypeError("Les deux valeurs doivent être des nombres (int ou float)")
        except TypeError as e:
            print(f"Erreur: {e}")
            return None

    def multiply(self):
        try:
            # Vérifier que a et b sont des nombres (int ou float)
            if isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)):
                # Exclure les booléens
                if not isinstance(self.a, bool) and not isinstance(self.b, bool):
                    result = self.a * self.b
                    return result
                else:
                    raise TypeError("Les booléens ne sont pas acceptés")
            else:
                raise TypeError("Les deux valeurs doivent être des nombres (int ou float)")
        except TypeError as e:
            print(f"Erreur: {e}")
            return None


# Exemples d'utilisation
calc1 = Calculator(5, 3)
print(f"Addition: {calc1.add()}")        # 8
print(f"Multiplication: {calc1.multiply()}")  # 15

calc2 = Calculator(5.5, 2)
print(f"Addition: {calc2.add()}")        # 7.5
print(f"Multiplication: {calc2.multiply()}")  # 11.0

calc3 = Calculator("hello", 3)
print(f"Addition: {calc3.add()}")        # Erreur: Les deux valeurs doivent être des nombres