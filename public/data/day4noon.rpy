day4noon:
    clear_dialog
    #MISSING
    "You return to the industrial building, desperate."
    "If you have the can: You can either feed the soda to Hornet, or press the cold metal to her burning cheek. either is +1 score"
    "If you have the first aid kit: You can try to bandage her wound. +1 score"
    "Her right leg soon falls off. She seems confused and distraught. She begins crying at one point."
    "With best stats you can stay inside with her for 1 score. With worst possible stats you leave and get an early bad ending."
    "With mid stats you go out to forage, trying to find anything that might help."
    "You return once to see Pulmonaria growing around her. She's watching them. Her left leg has fallen off at the hip, her right arm at the shoulder."
    "You can stay or leave again."
    "When you return, the Pulmonaria are in full bloom, crowning her. You walk up to her, and cradle her head in your hands."
    "It falls into them. It is made of:"
    $if this.data.score < 4:
        "plastic"
        "You stare at it in horror. When you look over at her torso, it has split open, filled with the purple and blue flowers, but empty."
        "Mid End"

    else:
        "porcelain"
        "You stare at it in terror and misery. When you look over at her torso..."
        "It has split open. Inside is a tiny newborn fawn, covered in white spots, a golden ribbon about its neck, resting in a bed of purple and blue flowers."
        "Best end"