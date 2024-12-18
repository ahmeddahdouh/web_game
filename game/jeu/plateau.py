import random
from jeu.case import Case
from joueurs import joueur
from obstacle import Obstacle


class Plateau:
    NB_JOUEUR_MAX = 6
    NB_CASE = 50

    def __init__(self, titre: str, nb_etape: int, nb_obstacle: int):
        self._titre = titre
        self._list_joueurs = []
        self._cases = self._cases = [
            Case(gain=i, perso=None, obs=None) for i in range(self.NB_CASE)
        ]
        self._nb_etapes = nb_etape
        self._nb_obstacles = nb_obstacle
        self._score_max = 0

    def ajouter_joueur(self, joueur: joueur):
        self._list_joueurs.append(joueur)

    def tous_les_persos(self):
        liste_perso = []
        for joueur in self._list_joueurs:
            for element in joueur.list_perso:
                liste_perso.append(element)
        return liste_perso

    def initialiser_cases(self):
        for i in range(self.NB_CASE):
            self._cases[i]._gain = random.randint(1, self.NB_CASE)
            if (
                self._cases[i]._gain % 5 == 0
                and Obstacle.nbObstacle < self._nb_obstacles
            ):
                self._cases[i].placer_obstacle(Obstacle(self._cases[i]._gain * 2))

    def afficher_plateau(self):
        print(f"Plateau : {self._titre}")
        for case in self._cases:
            print(str(case))

    def lancer_jeu(self):
        list_perso = self.tous_les_persos()
        free_cases = [i for i, case in enumerate(self._cases) if case.sans_obstacle()]

        if len(free_cases) < len(list_perso):
            print("Il n'y a pas assez de cases libres pour tous les personnages.")
            return

        for element in list_perso:
            if free_cases:
                index = free_cases.pop(0)
                self._cases[index].placer_personnage(element)
            else:
                print("Aucune place libre pour placer un personnage")
                break
