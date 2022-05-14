day2swamp:
    set_screen swamp1
    play music swampsong
    "The day is heady and foggy, only a little less cold than the night. You feel ambient moisture seeping into your dress, and are all the more glad for Hornet's coat."
    "The two of you eat some conserved sheep sausage and tin bread for breakfast."
    "You don't bring up having woken Hornet up, and she doesn't either - hopefully she's forgotten. It makes you a little ashamed to remember."
    talk hrn talk "It's a good thing we didn't go any further last night."
    "She gestures at the wilder woods ahead of you."
    talk hrn talk "Looks like a... what's the word. The, uh..."
    choice:
        "A small freckled hand waves about in irritation."
        "('A peat bog?')"
            talk hrn talk "A peat bog?"
    talk hrn talk "That's the one."
    $if this.DATA.tensionPoints < 4:
        talk hrn talk "Thanks."
        talk em talk "Speaking of..."
    