import random

class Lotteri:
    
    def __init__(self):
        self.list_vinster = [
        "Ljusgul fluffig kula",
        "Grek-stek",
        "Ak-fempan",
        "Gunnarssons trä-skor",
        "10 liter nomnom",
        "Maglies naturgodis",
        "Walters Kristaller",
        "Viggos Morot"
        "PJ's popcorn"
        "en burk cornichons",
        "rättigheterna till pewdiepies första låt",
        "En magisk svamp",
        "Dag Hellby's Kanon",
        "Gustav Kanon",
        "en påskö-staty",
        "en gaminghjälm",
        "en daddel",
        "VIP-biljett till Lekdags 2",
        "Grisphilips bacon",
        "en magisk svamp",
        "ett gåthorn"
        ]

    def get_vinst(self):
        slumptal = random.randint(0, 19)
        return self.list_vinster[slumptal]
        