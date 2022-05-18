day3river:
    play music empty
    set_screen swamp5
    "The morning comes, and Hornet looks no more like a dog than she ever has."
    "The wagon hasn't collapsed either. You eat a quiet breakfast, creamed corn and cold flatbreads that both taste of conservants."
    $if this.data.dreamDogEat:
        talk hrn talk "..."
        talk em talk "..." 
    else:
        talk hrn talk "Sleep okay?"
        talk em talk "I guess."
        talk hrn talk "No bad dreams I hope!"
        "She wipes the last of the corn off her tin plate and gets up."
        talk hrn talk "Let's get going."
    "You set out."
    "It's not too long before you reach the end of the wooden walkway - and then, after some minutes on solid ground:"
    set_screen river1
    play music riverNice
    "the trees part, revealing a great river."
    "It's a dark, blueish grey in colour, and very silent. It's long been straightened - not by concrete but by chunks of rock, so it must be very old indeed."
    "A dusty path leads along the bank, some meters above it. It's asphalt, but old and run through with deep cracks. Thick white residue, not quite sand, has filled those, and it looks almost like grey marble, but for the tufts of beige weeds that sprout between the chunks of pavement."
    "Green would line the path, but for that dust - which has choked out most of the grass, it seems. Even the trees are a thick, chalky white, some all the way up to their crowns."
    "Whatever it is, it must come from the river - perhaps during floods." 
    "!! END OF CURRENT FINAL IMPLEMENTATION - PROCEED FOR OUTLINES AND ART ONLY !!"
    jump day3river_walk
    #why did you leave the city conversation
    #fruit conversation - option to really hurt hornet

day3river_walk:
    clear_dialog
    set_screen river2
    #MISSING
    "Hornet and emily walk along the river, wondering about where the dust might come from. It smells like:"
    $if this.data.tensionPoints > 4:
        "Styrohoam."
        "You have a bad score."
    else:
        $if this.data.score > 2:
            "Peach pits."
            "You have a very good score."
            "Hornet and Emily discuss why they REALLY left the city. With low tension and a high score, you unlock a 'to be with you' option that doesnt say LIE next to it."
            jump day3river_noargue
        "Burnt paper."
        "You have a middling score."
    "Hornet and Emily discuss why they REALLY left the city. With low tension and a high score, you unlock a 'to be with you' option that doesnt say LIE next to it."
    jump day3river_argue

day3river_argue:
    play music riverBad
    set_screen river3a
    #MISSING
    "Emily comments on the trees, hoping there are fruits."
    "This confuses Hornet, who doesn't know fruits come from trees. It spirals into an argument, unless the player has low enough tension to see the good options."
    $if this.data.tensionPoints > 5:
        set_screen river3b
        "Hornet is getting very angry."
    else:
        "Hornet is merely disappointed."
    jump day3bedtime


day3river_noargue:
    set_screen river3a
    #MISSING
    "Hornet says she's glad to be out of the swamp."
    "She hopes you're having an easier time with the suitcase on the asphalt."
    jump day3bedtime