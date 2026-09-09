import game
import sprites
import controller
import scene
import info



speler_afbeelding = img("""
    . . . . . . . . . . . . . . . .
    . . . . . 1 1 1 1 1 1 . . . . .
    . . . . 1 1 1 1 1 1 1 1 . . . .
    . . . . 1 1 1 1 1 1 1 1 . . . .
    . . . . . 1 1 1 1 1 1 . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . . 1 1 1 1 . . . . . .
    . . . . . 1 1 1 1 1 1 . . . . .
    . . . . 1 1 1 1 1 1 1 1 . . . .
    . . . . 1 1 1 1 1 1 1 1 . . . .
    . . . . 1 1 . . . . 1 1 . . . .
    . . . . 1 1 . . . . 1 1 . . . .
    . . . . 1 1 . . . . 1 1 . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
""")

auto_afbeelding = img("""
    . . . . . . . . . . . . . . . .
    . . . . 2 2 2 2 2 2 2 2 . . . .
    . . . 2 2 2 2 2 2 2 2 2 2 . . .
    . . . 2 2 2 2 2 2 2 2 2 2 . . .
    . . . 2 2 2 2 2 2 2 2 2 2 . . .
    . . . 2 2 2 2 2 2 2 2 2 2 . . .
    . . . 2 2 2 2 2 2 2 2 2 2 . . .
    . . . 2 2 2 2 2 2 2 2 2 2 . . .
    . . . 2 2 2 2 2 2 2 2 2 2 . . .
    . . . 2 2 2 2 2 2 2 2 2 2 . . .
    . . . 2 2 . . . . 2 2 . . . . .
    . . . 2 2 . . . . 2 2 . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
""")

stop_afbeelding = img("""
    . . . . . 2 2 2 2 . . . . . .
    . . . . 2 2 2 2 2 2 . . . . .
    . . . . 2 2 2 2 2 2 . . . . .
    . . . 2 2 2 2 2 2 2 2 . . . .
    . . . 2 2 2 2 2 2 2 2 . . . .
    . . . . 2 2 2 2 2 2 . . . . .
    . . . . 2 2 2 2 2 2 . . . . .
    . . . . . 2 2 2 2 . . . . . .
    . . . . . . . 2 . . . . . . .
    . . . . . . . 2 . . . . . . .
    . . . . . . . 2 . . . . . . .
    . . . . . . . 2 . . . . . . .
    . . . . . . . 2 . . . . . . .
    . . . . . . . 2 . . . . . . .
    . . . . . . . 2 . . . . . . .
    . . . . . . . 2 . . . . . . .
""")

fiets_afbeelding = img("""
    . . . . . . . . . . . . . . .
    . . . . . . 7 7 . . . . . . .
    . . . . . 7 7 7 7 . . . . . .
    . . . . 7 7 7 7 7 7 . . . . .
    . . . . 7 7 7 7 7 7 . . . . .
    . . . . . 7 7 7 7 . . . . . .
    . . . . . 7 7 7 7 . . . . . .
    . . . . . 7 7 7 7 . . . . . .
    . . . . . 7 7 7 7 . . . . . .
    . . . . . 7 7 7 7 . . . . . .
    . . . . . . 7 7 . . . . . . .
    . . . . . . 7 7 . . . . . . .
    . . . . . . 7 7 . . . . . . .
    . . . . . . 7 7 . . . . . . .
    . . . . . . 7 7 . . . . . . .
    . . . . . . 7 7 . . . . . . .
""")




speler = sprites.create(speler_afbeelding, SpriteKind.player)
auto = sprites.create(auto_afbeelding, SpriteKind.enemy)
bord_stop = sprites.create(stop_afbeelding, SpriteKind.enemy)
bord_fiets = sprites.create(fiets_afbeelding, SpriteKind.enemy)



scherm = "intro"
vraag = 0



speler.set_flag(SpriteFlag.INVISIBLE, True)
auto.set_flag(SpriteFlag.INVISIBLE, True)
bord_stop.set_flag(SpriteFlag.INVISIBLE, True)
bord_fiets.set_flag(SpriteFlag.INVISIBLE, True)



def maak_stad():
    scene.set_background_color(7)


    weg1 = sprites.create(img("""
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    """), SpriteKind.food)

    weg1.set_position(80, 80)

    # Tweede weg
    weg2 = sprites.create(img("""
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    """), SpriteKind.food)

    weg2.set_position(80, 120)

    # Huizen
    huis1 = sprites.create(img("""
        . . 4 4 4 4 . .
        . 4 4 4 4 4 4 .
        4 4 4 4 4 4 4 4
        4 4 4 4 4 4 4 4
        4 4 . 4 4 . 4 4
        4 4 . 4 4 . 4 4
        4 4 . 4 4 . 4 4
        4 4 4 4 4 4 4 4
    """), SpriteKind.food)

    huis1.set_position(25, 25)

    huis2 = sprites.create(img("""
        . . 8 8 8 8 . .
        . 8 8 8 8 8 8 .
        8 8 8 8 8 8 8 8
        8 8 8 8 8 8 8 8
        8 8 . 8 8 . 8 8
        8 8 . 8 8 . 8 8
        8 8 . 8 8 . 8 8
        8 8 8 8 8 8 8 8
    """), SpriteKind.food)

    huis2.set_position(135, 25)

# ==========================================
# SPELER
# ==========================================

def toon_speler():
    speler.set_flag(SpriteFlag.INVISIBLE, False)
    speler.set_position(80, 105)
    controller.move_sprite(speler, 70, 70)
    speler.set_flag(SpriteFlag.STAY_IN_SCREEN, True)

# ==========================================
# AUTO
# ==========================================

def toon_auto():
    auto.set_flag(SpriteFlag.INVISIBLE, False)
    auto.set_position(145, 80)
    auto.vx = -35

# ==========================================
# STOPBORD
# ==========================================

def toon_stopbord():
    bord_stop.set_flag(SpriteFlag.INVISIBLE, False)
    bord_stop.set_position(25, 80)

# ==========================================
# FIETSPADBORD
# ==========================================

def toon_fietspad():
    bord_fiets.set_flag(SpriteFlag.INVISIBLE, False)
    bord_fiets.set_position(135, 110)

# ==========================================
# VERKEER VERBERGEN
# ==========================================

def verberg_verkeer():
    auto.set_flag(SpriteFlag.INVISIBLE, True)
    bord_stop.set_flag(SpriteFlag.INVISIBLE, True)
    bord_fiets.set_flag(SpriteFlag.INVISIBLE, True)

# ==========================================
# INTRO
# ==========================================

def intro():
    global scherm

    scherm = "intro"

    game.splash(
        "VERKEERSMEISTER",
        "Welkom bij VerkeersMeister!"
    )

    game.splash(
        "KLAAR?",
        "Druk op A"
    )

    hoofdmenu()

# ==========================================
# HOOFDMENU
# ==========================================

def hoofdmenu():
    global scherm

    scherm = "menu"

    game.splash(
        "HOOFDMENU",
        "A = PLAY"
    )

    game.splash(
        "SETTINGS",
        "B = SETTINGS"
    )

# ==========================================
# INSTELLINGEN
# ==========================================

def instellingen():
    global scherm

    scherm = "settings"

    game.splash(
        "SETTINGS",
        "VerkeersMeister"
    )

    game.splash(
        "BESTURING",
        "Pijltjes = fietsen"
    )

    game.splash(
        "TERUG",
        "Druk op B"
    )

# ==========================================
# START SPEL
# ==========================================

def start_spel():
    global scherm
    global vraag

    scherm = "vraag"
    vraag = 1

    info.set_score(0)

    maak_stad()
    toon_speler()

    game.splash(
        "START!",
        "Let goed op!"
    )

    vraag_een()

# ==========================================
# VRAAG 1
# ==========================================

def vraag_een():
    global scherm
    global vraag

    scherm = "vraag"
    vraag = 1

    verberg_verkeer()
    toon_auto()

    game.splash(
        "SITUATIE 1",
        "Auto komt van rechts!"
    )

    game.splash(
        "WAT DOE JE?",
        "A = auto laten gaan"
    )

    game.splash(
        "OF",
        "B = doorfietsen"
    )

# ==========================================
# VRAAG 2
# ==========================================

def vraag_twee():
    global scherm
    global vraag

    scherm = "vraag"
    vraag = 2

    verberg_verkeer()
    toon_stopbord()

    game.splash(
        "SITUATIE 2",
        "Je ziet een STOP-bord."
    )

    game.splash(
        "WAT DOE JE?",
        "A = stoppen"
    )

    game.splash(
        "OF",
        "B = doorrijden"
    )

# ==========================================
# VRAAG 3
# ==========================================

def vraag_drie():
    global scherm
    global vraag

    scherm = "vraag"
    vraag = 3

    verberg_verkeer()
    toon_fietspad()

    game.splash(
        "SITUATIE 3",
        "Er is een fietspad."
    )

    game.splash(
        "WAT DOE JE?",
        "A = fietspad"
    )

    game.splash(
        "OF",
        "B = stoep"
    )

# ==========================================
# VRAAG 4
# ==========================================

def vraag_vier():
    global scherm
    global vraag

    scherm = "vraag"
    vraag = 4

    verberg_verkeer()

    game.splash(
        "SITUATIE 4",
        "Je hebt voorrang."
    )

    game.splash(
        "WAT DOE JE?",
        "A = doorfietsen"
    )

    game.splash(
        "OF",
        "B = stoppen"
    )

# ==========================================
# VRAAG 5
# ==========================================

def vraag_vijf():
    global scherm
    global vraag

    scherm = "vraag"
    vraag = 5

    verberg_verkeer()

    game.splash(
        "SITUATIE 5",
        "Iemand wil oversteken."
    )

    game.splash(
        "WAT DOE JE?",
        "A = voorrang geven"
    )

    game.splash(
        "OF",
        "B = doorfietsen"
    )

# ==========================================
# GOED ANTWOORD
# ==========================================

def goed(tekst):
    global vraag

    info.change_score_by(100)

    game.splash(
        "GOED!",
        tekst
    )

    if vraag == 1:
        vraag_twee()
    elif vraag == 2:
        vraag_drie()
    elif vraag == 3:
        vraag_vier()
    elif vraag == 4:
        vraag_vijf()
    elif vraag == 5:
        einde()

# ==========================================
# FOUT ANTWOORD
# ==========================================

def fout(tekst):
    global vraag

    info.set_score(0)

    game.splash(
        "Helaas!",
        tekst
    )

    game.splash(
        "OPNIEUW",
        "Je score is 0"
    )

    if vraag == 1:
        vraag_een()
    elif vraag == 2:
        vraag_twee()
    elif vraag == 3:
        vraag_drie()
    elif vraag == 4:
        vraag_vier()
    elif vraag == 5:
        vraag_vijf()

# ==========================================
# EINDE
# ==========================================

def einde():
    global scherm

    scherm = "einde"

    verberg_verkeer()

    speler.set_flag(SpriteFlag.INVISIBLE, True)

    game.splash(
        "GEFELICITEERD!",
        "Alle situaties klaar!"
    )

    game.splash(
        "JOUW SCORE",
        str(info.score())
    )

    hoofdmenu()

# ==========================================
# A-KNOP
# ==========================================

def druk_op_a():
    global scherm

    if scherm == "intro":
        hoofdmenu()

    elif scherm == "menu":
        start_spel()

    elif scherm == "vraag":

        if vraag == 1:
            goed("Auto van rechts heeft voorrang!")

        elif vraag == 2:
            goed("Bij STOP moet je stoppen!")

        elif vraag == 3:
            goed("Gebruik het fietspad!")

        elif vraag == 4:
            goed("Je mag doorfietsen!")

        elif vraag == 5:
            goed("Geef de voetganger voorrang!")

# ==========================================
# B-KNOP
# ==========================================

def druk_op_b():
    global scherm

    if scherm == "menu":
        instellingen()

    elif scherm == "settings":
        hoofdmenu()

    elif scherm == "vraag":

        if vraag == 1:
            fout("Verkeer van rechts heeft voorrang.")

        elif vraag == 2:
            fout("Bij STOP moet je stoppen.")

        elif vraag == 3:
            fout("Fiets op het fietspad.")

        elif vraag == 4:
            fout("Je hebt hier voorrang.")

        elif vraag == 5:
            fout("Laat de voetganger oversteken.")

# ==========================================
# KNOPPEN INSTELLEN
# ==========================================

controller.A.on_event(
    ControllerButtonEvent.PRESSED,
    druk_op_a
)

controller.B.on_event(
    ControllerButtonEvent.PRESSED,
    druk_op_b
)

# ==========================================
# START
# ==========================================

intro()