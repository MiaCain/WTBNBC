day1dream:
    clear_dialog
    set_screen blank
    play music empty
    "..."
    "..."
    "..."
    "Your legs"
    "Hurt."
    "You try shifting one of them, when suddenly,"
    set_screen banq1
    play music banquetsong
    talk pa talk "You've got seat reserved at a great banquet, Emily."
    talk pa talk "You can see a hundred guests - two hundred more in the great wall-to-wall mirrors lining the hall, and each glazen hall with its own reflection, driving attendance levels into infinity."
    talk pa talk "All of them are eating. They're dressed in finery and livery, the ruches of high society, fibreglass cufflinks and satin pocket linings on everyone."
    talk pa talk "The colours are gaudy - all of them. The clothes, yes, but also the tablecloth, the plates, all of it gleams in coral and amber and gilded wood."
    talk pa talk "Next to them all you look nearly plain - made up in a simple red shift, your hair combed over one shoulder. When you feel for them, you aren't even wearing jewels. You feel ashamed - you must stick out sorely."
    talk pa talk "You attempt to make out what the conversation is about, or who is in attendance - but the faces before you keep averting their gaze, and your eyes slip off them."
    talk pa talk "In the end, it's simply too difficult to focus on them or their lazy chattering."
    talk pa talk "Instead you turn your attention to the spread before you. None of it looks particularly inviting; stuffed tigre paws offer lavender and lungwort salads in their rictus, claws extended as though still wishing to strike their captors. Tiny red beads - berries, perhaps, though they smell of iron - fill plates."
    talk pa talk "Someone at your table is gorging on tiny songbirds, and you hear a roar of jolly laughter go up from their neighbours."
    set_screen banq2
    talk pa talk "A waiter passes by and places a glass cup before you."
    talk pa talk "It is intricately tooled, splitting and reflecting the strange light and the mirror-wall, filling the liquid inside with an unnerving glow."
    choice:
        talk pa talk "The waiter bustles off."
        "(Gaze into the cup)":
            "You pick it up and stare inside."
    set_screen banq3
    "You are met with another reflection, but-"
    talk pa talk "It's Hornet. Your darling Hornet. That poor young girl who, even though she's from the machining district, turned out to be so sweet and exciting."
    talk pa talk "Yes, it's her."
    "But..."
    talk pa talk "But she's warped. There's something wrong with her."
    talk pa talk "You can see her hulking in the underbrush. You know deep inside she's been stalking you here, in this image, waiting for you to see her."
    "To see her and know it's already over."
    choice:
        talk pa talk "She's a predator here. You know it. You can see it in her eyes. She's going to draw closer and closer and then"
        "She's going to drink the hot blood out of my throat, and eat my heart and my stomach":
            "You drop the cup in horror, the contents splashing to the ground, one reflection dissipating into a million shards, each too small to hurt you now."
    set_screen blank
    play music sleeptime
    "The guests are gone too, and suddenly, you're back in the forest."
    jump day1dream_wake

day1dream_wake:
    set_screen banq4
    "You can hear Hornet snoring softly below you. You reach down, to touch her shoulder, touch her hair."
    talk em talk "hornet..."
    "you whisper, then hiss-"
    talk em talk "Hornet!"
    "You give her a slight squeeze and she breathes in. Her eyes open a smidge."
    talk hrn talk "...Emily? What is..."
    choice:
        "She freezes and her eyes open a little wider when she sees the look in yours."   
        "'Promise me you won't ever hurt me.'":
            talk em talk "Promise me you won't ever hurt me."
            talk em talk "Promise it. Swear it. You don't want to... You won't do me any, you... you fucking..."
    "A gentle touch on your arm distracts you."
    talk hrn talk "Did you have a bad dream?"
    if (<= $data.tensionPoints 1):
        "Hornet plants a gentle kiss on your forehead."
        add this.data.score 1
        talk hrn talk "It was only a bad dream, Emily. Try to get some more rest, it'll be morning soon."
    talk hrn talk "I promise I won't ever hurt you, Emily. Or why would I have run away with you?"
    if (< $data.tensionPoints 3):
        "You can make out a little smile."
    talk hrn talk "Good night."
    set_screen blank
    "Feeling a little less panicked, you drift off again."
    "This time, your rest is untroubled..."
    jump opener2
