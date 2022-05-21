main:
    set data.OR.bagmention false
    set data.FORhasCoat false
    set data.tensionPoints 0
    set data.score 0
    set data.hasFirstaid false
    set data.OR.leaveReason 1
    set data.OR.cityfeeling 0
    set data.LOVE 0
    set_screen title
    clear_dialog
    play music maintheme
    "WILL THIS BITTER NIGHT BRING CHANGE?"
    "or"
    "TWO WOMEN IN TROUBLE"
    "A Game by MIA CAIN"
    "Created for the Digital Arts Course at the FHOÖ in 2022 using the Narrat engine. Based on the story 'Brüderchen und Schwesterchen,' Brothers Grimm, 1812."
    "Please be aware that the game currently cannot save or load fully - set aside about an hour to play. I apologise for any inconvenience this may cause."
    "Please report any bugs, typos, etc. to the author."
    choice:
        talk pa talk "Caution: this game includes surreal and graphic imagery, strong language, and discusses adult themes. Please proceed accordingly."
        "I understand.":
            jump opener1