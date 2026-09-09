let speler_afbeelding = img`
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
`
let auto_afbeelding = img`
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
`
let stop_afbeelding = img`
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
`
let fiets_afbeelding = img`
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
`
let speler = sprites.create(speler_afbeelding, SpriteKind.Player)
let auto = sprites.create(auto_afbeelding, SpriteKind.Enemy)
let bord_stop = sprites.create(stop_afbeelding, SpriteKind.Enemy)
let bord_fiets = sprites.create(fiets_afbeelding, SpriteKind.Enemy)
let scherm = "intro"
let vraag = 0
speler.setFlag(SpriteFlag.Invisible, true)
auto.setFlag(SpriteFlag.Invisible, true)
bord_stop.setFlag(SpriteFlag.Invisible, true)
bord_fiets.setFlag(SpriteFlag.Invisible, true)
function maak_stad() {
    scene.setBackgroundColor(7)
    let weg1 = sprites.create(img`
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    `, SpriteKind.Food)
    weg1.setPosition(80, 80)
    //  Tweede weg
    let weg2 = sprites.create(img`
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    `, SpriteKind.Food)
    weg2.setPosition(80, 120)
    //  Huizen
    let huis1 = sprites.create(img`
        . . 4 4 4 4 . .
        . 4 4 4 4 4 4 .
        4 4 4 4 4 4 4 4
        4 4 4 4 4 4 4 4
        4 4 . 4 4 . 4 4
        4 4 . 4 4 . 4 4
        4 4 . 4 4 . 4 4
        4 4 4 4 4 4 4 4
    `, SpriteKind.Food)
    huis1.setPosition(25, 25)
    let huis2 = sprites.create(img`
        . . 8 8 8 8 . .
        . 8 8 8 8 8 8 .
        8 8 8 8 8 8 8 8
        8 8 8 8 8 8 8 8
        8 8 . 8 8 . 8 8
        8 8 . 8 8 . 8 8
        8 8 . 8 8 . 8 8
        8 8 8 8 8 8 8 8
    `, SpriteKind.Food)
    huis2.setPosition(135, 25)
}

//  ==========================================
//  SPELER
//  ==========================================
function toon_speler() {
    speler.setFlag(SpriteFlag.Invisible, false)
    speler.setPosition(80, 105)
    controller.moveSprite(speler, 70, 70)
    speler.setFlag(SpriteFlag.StayInScreen, true)
}

//  ==========================================
//  AUTO
//  ==========================================
function toon_auto() {
    auto.setFlag(SpriteFlag.Invisible, false)
    auto.setPosition(145, 80)
    auto.vx = -35
}

//  ==========================================
//  STOPBORD
//  ==========================================
function toon_stopbord() {
    bord_stop.setFlag(SpriteFlag.Invisible, false)
    bord_stop.setPosition(25, 80)
}

//  ==========================================
//  FIETSPADBORD
//  ==========================================
function toon_fietspad() {
    bord_fiets.setFlag(SpriteFlag.Invisible, false)
    bord_fiets.setPosition(135, 110)
}

//  ==========================================
//  VERKEER VERBERGEN
//  ==========================================
function verberg_verkeer() {
    auto.setFlag(SpriteFlag.Invisible, true)
    bord_stop.setFlag(SpriteFlag.Invisible, true)
    bord_fiets.setFlag(SpriteFlag.Invisible, true)
}

//  ==========================================
//  INTRO
//  ==========================================
function intro() {
    
    scherm = "intro"
    game.splash("VERKEERSMEISTER", "Welkom bij VerkeersMeister!")
    game.splash("KLAAR?", "Druk op A")
    hoofdmenu()
}

//  ==========================================
//  HOOFDMENU
//  ==========================================
function hoofdmenu() {
    
    scherm = "menu"
    game.splash("HOOFDMENU", "A = PLAY")
    game.splash("SETTINGS", "B = SETTINGS")
}

//  ==========================================
//  INSTELLINGEN
//  ==========================================
function instellingen() {
    
    scherm = "settings"
    game.splash("SETTINGS", "VerkeersMeister")
    game.splash("BESTURING", "Pijltjes = fietsen")
    game.splash("TERUG", "Druk op B")
}

//  ==========================================
//  START SPEL
//  ==========================================
function start_spel() {
    
    
    scherm = "vraag"
    vraag = 1
    info.setScore(0)
    maak_stad()
    toon_speler()
    game.splash("START!", "Let goed op!")
    vraag_een()
}

//  ==========================================
//  VRAAG 1
//  ==========================================
function vraag_een() {
    
    
    scherm = "vraag"
    vraag = 1
    verberg_verkeer()
    toon_auto()
    game.splash("SITUATIE 1", "Auto komt van rechts!")
    game.splash("WAT DOE JE?", "A = auto laten gaan")
    game.splash("OF", "B = doorfietsen")
}

//  ==========================================
//  VRAAG 2
//  ==========================================
function vraag_twee() {
    
    
    scherm = "vraag"
    vraag = 2
    verberg_verkeer()
    toon_stopbord()
    game.splash("SITUATIE 2", "Je ziet een STOP-bord.")
    game.splash("WAT DOE JE?", "A = stoppen")
    game.splash("OF", "B = doorrijden")
}

//  ==========================================
//  VRAAG 3
//  ==========================================
function vraag_drie() {
    
    
    scherm = "vraag"
    vraag = 3
    verberg_verkeer()
    toon_fietspad()
    game.splash("SITUATIE 3", "Er is een fietspad.")
    game.splash("WAT DOE JE?", "A = fietspad")
    game.splash("OF", "B = stoep")
}

//  ==========================================
//  VRAAG 4
//  ==========================================
function vraag_vier() {
    
    
    scherm = "vraag"
    vraag = 4
    verberg_verkeer()
    game.splash("SITUATIE 4", "Je hebt voorrang.")
    game.splash("WAT DOE JE?", "A = doorfietsen")
    game.splash("OF", "B = stoppen")
}

//  ==========================================
//  VRAAG 5
//  ==========================================
function vraag_vijf() {
    
    
    scherm = "vraag"
    vraag = 5
    verberg_verkeer()
    game.splash("SITUATIE 5", "Iemand wil oversteken.")
    game.splash("WAT DOE JE?", "A = voorrang geven")
    game.splash("OF", "B = doorfietsen")
}

//  ==========================================
//  GOED ANTWOORD
//  ==========================================
function goed(tekst: string) {
    
    info.changeScoreBy(100)
    game.splash("GOED!", tekst)
    if (vraag == 1) {
        vraag_twee()
    } else if (vraag == 2) {
        vraag_drie()
    } else if (vraag == 3) {
        vraag_vier()
    } else if (vraag == 4) {
        vraag_vijf()
    } else if (vraag == 5) {
        einde()
    }
    
}

//  ==========================================
//  FOUT ANTWOORD
//  ==========================================
function fout(tekst: string) {
    
    info.setScore(0)
    game.splash("Helaas!", tekst)
    game.splash("OPNIEUW", "Je score is 0")
    if (vraag == 1) {
        vraag_een()
    } else if (vraag == 2) {
        vraag_twee()
    } else if (vraag == 3) {
        vraag_drie()
    } else if (vraag == 4) {
        vraag_vier()
    } else if (vraag == 5) {
        vraag_vijf()
    }
    
}

//  ==========================================
//  EINDE
//  ==========================================
function einde() {
    
    scherm = "einde"
    verberg_verkeer()
    speler.setFlag(SpriteFlag.Invisible, true)
    game.splash("GEFELICITEERD!", "Alle situaties klaar!")
    game.splash("JOUW SCORE", "" + info.score())
    hoofdmenu()
}

//  ==========================================
//  A-KNOP
//  ==========================================
//  ==========================================
//  B-KNOP
//  ==========================================
//  ==========================================
//  KNOPPEN INSTELLEN
//  ==========================================
controller.A.onEvent(ControllerButtonEvent.Pressed, function druk_op_a() {
    
    if (scherm == "intro") {
        hoofdmenu()
    } else if (scherm == "menu") {
        start_spel()
    } else if (scherm == "vraag") {
        if (vraag == 1) {
            goed("Auto van rechts heeft voorrang!")
        } else if (vraag == 2) {
            goed("Bij STOP moet je stoppen!")
        } else if (vraag == 3) {
            goed("Gebruik het fietspad!")
        } else if (vraag == 4) {
            goed("Je mag doorfietsen!")
        } else if (vraag == 5) {
            goed("Geef de voetganger voorrang!")
        }
        
    }
    
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function druk_op_b() {
    
    if (scherm == "menu") {
        instellingen()
    } else if (scherm == "settings") {
        hoofdmenu()
    } else if (scherm == "vraag") {
        if (vraag == 1) {
            fout("Verkeer van rechts heeft voorrang.")
        } else if (vraag == 2) {
            fout("Bij STOP moet je stoppen.")
        } else if (vraag == 3) {
            fout("Fiets op het fietspad.")
        } else if (vraag == 4) {
            fout("Je hebt hier voorrang.")
        } else if (vraag == 5) {
            fout("Laat de voetganger oversteken.")
        }
        
    }
    
})
//  ==========================================
//  START
//  ==========================================
intro()
