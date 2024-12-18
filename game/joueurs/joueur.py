from personnages.avatar import Avatar


class joueur:
    _code = 0
    _nb_joueur = 0

    def __init__(self, **kwargs):
        self._nom = kwargs["nom"]
        self._code += 1
        self._nb_joueur += 1
        self._nb_point = 0
        self._list_perso = kwargs["listperso"]

    @property
    def list_perso(self):
        return self._list_perso

    def ajouter_personnage(self, personnage: Avatar):
        self._list_perso.append(self.personnage)

    def modifier_point(self, nb: int):
        self._nb_point += nb

    def peut_jouer(self):
        return len(self._list_perso) > 0

    def __str__(self):
        return f"{self._code} {self._nom} ({self._nb_point}) points avec {len(self._list_perso)} joueurs "
