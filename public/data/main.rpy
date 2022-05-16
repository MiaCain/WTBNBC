main:
    set data.OR.bagmention false
    set data.hasFirstaid false
    set_screen title
    clear_dialog
    "WILL THIS BITTER NIGHT BRING CHANGE?"
    "or"
    "TWO WOMEN IN TROUBLE"
    "A Game by MIA CAIN"
    "Created for the Digital Arts Course at the FHOÖ in 2022 using the Narrat engine. Based on the story 'Brüderchen und Schwesterchen,' Brothers Grimm, 1812."
    choice:
        talk pa talk "Caution: this game includes surreal and graphic imagery, strong language, and discusses adult themes. Please proceed accordingly."
        "I understand.":
            jump opener1