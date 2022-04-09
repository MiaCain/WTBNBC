main:
    set_screen title
    clear_dialog
    "Two Women in Trouble"
    "A Game by Mia Cain"
    "Created for the Digital Arts Course at the FHOÖ in 2022. Uses the Narrat engine. Based on the story 'Brüderchen und Schwesterchen,' Brothers Grimm, 1812."
    choice:
        talk pa talk "Caution: this game includes surreal and graphic imagery, strong language, and discusses adult themes. Please proceed accordingly."
        "I understand.":
            jump intro1