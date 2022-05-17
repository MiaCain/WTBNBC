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
    #why did you leave the city conversation
    #fruit conversation - option to really hurt hornet