class Quest:
    """class for manage quest"""

    def __init__(self, targs):
        self._lAvatar = targs["lAvatar"]
        self._lvl = targs["lvl"]
        self._itemGift = targs["gift"]

    def run(self, hero):
        round = 1
        output = ""
        if len(self._lAvatar) == 1:
            output += "### PVP MODE ####"
            print("### PVP MODE ####")
            player = self._lAvatar[0]
            output += "\n" + player._nom + " VS " + hero._nom
            print(player._nom + " VS " + hero._nom)
            while (player._life > 0) and (hero._life > 0):
                output += "\n" + "Round " + str(round)
                print("# Round " + str(round) + " # ")
                print("# PV de " + hero._nom + " " + str(hero._life))
                output += "\n" + "# PV de " + hero._nom + " " + str(hero._life)
                print("# PV de " + player._nom + " " + str(player._life))
                output += "\n" + "# PV de " + player._nom + " " + str(player._life)
                if player.initiative() > hero.initiative:
                    output += "\n" + player._nom + " begin"
                    print(player._nom + " begin")
                    hero.defense(player.damages())
                    if hero._life <= 0:
                        output += "\n" + player._nom + " win"
                        print(player._nom + " win")
                    else:
                        player.defense(hero.damages())
                else:
                    output += "\n" + hero._nom + " begin"
                    print(hero._nom + " begin")
                    player.defense(hero.damages())
                    if player._life <= 0:
                        output += "\n" + hero._nom + " win"
                        print(hero._nom + " win")
                    else:
                        hero.defense(player.damages())
                round += 1
            if hero._life <= 0:
                output += "\n" + player._nom + " win"
                print(player._nom + " win")
                player.setXP(10 * self._lvl)
                player._bag.addItem(self._itemGift)
            else:
                output += "\n" + hero._nom + " win"
                print(hero._nom + " win")
                hero.setXP(10 * self._lvl)
                hero._bag.addItem(self._itemGift)
        else:
            output += "\n" + "### Quest MODE ####"
            print("### Quest MODE ####")
            for player in self._lAvatar:
                output += "\n" + player._nom + " VS " + hero._nom
                print(player._nom + " VS " + hero._nom)
                while (player._life > 0) and (hero._life > 0):
                    output += "\n" + "Round " + str(round)
                    print(f"Round  {str(round)}")
                    print(f"# Round {str(round)} # ")
                    print(f"# PV de  {hero._nom}: {str(hero._life)}")
                    output += "\n" + "# PV de " + hero._nom + " " + str(hero._life)
                    print("# PV de " + player._nom + " " + str(player._life))
                    output += "\n" + "# PV de " + player._nom + " " + str(player._life)
                    if player.initiative() > hero.initiative():
                        output += "\n" + player._nom + " begin"
                        print(player._nom + " begin")
                        tmpDegats = player.damages()
                        hero.defense(tmpDegats)
                        output += "\n" + player._nom + " degats " + str(tmpDegats)
                        print(player._nom + " degats " + str(tmpDegats))
                        if hero._life <= 0:
                            output += "\n" + player._nom + " win"
                            print(player._nom + " win")
                        else:
                            tmpDegats = hero.damages()
                            player.defense(tmpDegats)
                            output += "\n" + hero._nom + " degats " + str(tmpDegats)
                            print(hero._nom + " degats " + str(tmpDegats))
                    else:
                        output += "\n" + hero._nom + " begin"
                        print(hero._nom + " begin")
                        tmpDegats = hero.damages()
                        player.defense(tmpDegats)
                        output += "\n" + hero._nom + " degats " + str(tmpDegats)
                        print(hero._nom + " degats " + str(tmpDegats))
                        if player._life <= 0:
                            output += "\n" + hero._nom + " win"
                            print(hero._nom + " win")
                        else:
                            tmpDegats = player.damages()
                            hero.defense(tmpDegats)
                            output += "\n" + player._nom + " degats " + str(tmpDegats)
                            print(player._nom + " degats " + str(tmpDegats))
                    round += 1
            if hero._life <= 0:
                output += "\n" + "You loose"
                print("You loose")
            else:
                output += "\n" + hero._nom + " win"
                print(hero._nom + " win")
                hero.setXP(10 * len(self._lAvatar) * self._lvl)
                hero._bag.addItem(self._itemGift)
            return output

    def __str__(self):
        return self._itemGift
