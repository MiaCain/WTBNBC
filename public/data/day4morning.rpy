day4morning:
    #MISSING
    play music rainsong
    set_screen end1
    "The final day brings heavy rainfall."
    "Hornet has a slight fever, but says they should move on. She refuses to take the jacket back,"
    $if this.data.tensionPoints > 4:
        "with a hiss."
    else:
        "with a smile."
    "Emily and Hornet begin walking."
    set_screen end2
    play music hornet
    "Hornet soon gasps in pain. When you look back, her hand is turning dark, apparently decomposing. She says her fingers are stiff."
    "You can urge her to turn back, but she won't."
    "After more walking..."
    set_screen end3
    "Hornet stops. You turn back and see her standing in shock, having taken off her jacket and bag, in apparent shock. Her arm lies in a puddle."
    "She says she feels dizzy."
    set_screen blank
    #NO_ART
    jump day4noon