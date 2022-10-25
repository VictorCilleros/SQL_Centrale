import random
#Windows: Shift+Alt+A



def carres(n):
  res = []
  for i in range(n):
    print("foo")
    res.append(i*i)
  return res

def flux_carres_bis(n):
  for i in range(n):
    print("bar")
    yield i*i

""" for c in carres(10):
  print(c)

for c in flux_carres_bis(10):
  print(c) """


def table(descr, nb=10000):
    """Cette fonction génère une séquence de tuples décrits par le dictionnaire
    descr. Le dictionnaire associe à une clé une paire (k,l). La fonction
    génère nb dictionnaires de la manière suivante :
    - chaque clé de descr est une clé de ces dictionnaires
    - à chacune de ces clés x, ces dictionnaires associent un nombre tiré au hasard
      entre k et l lorsque la paire (k,l) est associée à x dans descr.
    NB : cette fonction requiert d'importer le module random.
    """
    for _ in range(nb):
        tuple_res = {}
        for a, (k,l) in descr.items():
            tuple_res[a] = random.randint(min(k, l), max(k, l))
        yield tuple_res


def somme_carres_quad(n):
    return sum(i*i for i in range(n))    # un générateur entre(). Mettre sum([]) demande de d'abord créer le tableau en mémoire.


def exemple_table():
    """Exemple d'utilisation de la fonction table. Génère une table de 10 éléments
comportant les attributs 'a' et 'b' et les affiche en flux."""
    schema = {'a': (0,10), 'b': (100,100000)}
    for tuple_tbl in table(schema,nb=10):
        print(tuple_tbl)

tab=[{"a": 1, "b": 2, "c": 3},
                 {"a": 1, "b": 3, "c": 4},
                 {"a": 5, "b": 2, "c": 3},
                 {"a": 1, "b": 8, "c": 4},
                 {"a": 5, "b": 2, "c": 3}
                 ]

print(key,val in tab[0])