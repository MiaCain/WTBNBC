day2bedtime_firstaid:
    play music sleeptime
    clear_dialog
    set_screen swamp6
    "The inside of the carriage smells bad, but it's not the worst thing ever. It's natural at least, not too unlike last night's hollow."
    "Faintly you can smell polycarbon, steel, aluminium, and ceramics rotting in the chassis. The covers on the seats are remarkably well preserved - some plastic fibre weave."
    talk hrn talk "Look!"
    "She gestures at a plastic case. A triangle is printed on the front,"
    "a lung design within it."
    talk hrn talk "A first aid kit!"
    if (>= $data.tensionPoints 5):
        "You haven't paid it any mind all day, but suddenly, the cut on the back of your hand throbs, hurting badly. You feel nauseous."
        choice:
            "You gasp in shock."
            "'Hornet, I *need* that!":
                talk em talk "Hornet, I *need* that!"
                if $data.FORlookedAtScratch:
                    "She looks startled."
                    talk hrn talk "What? What for?"
                    "Hornet has slipped the plastic case out of its slot, and is opening it."
                    talk em talk "My cut!"
                    "You thrust out your hand, wincing. The wound has stopped bleeding, becoming a thin brownish line. It feels terrible. You begin imagining yourself with only one hand, or even one arm..."
                    "Hornet looks suddenly very irritated, only glancing at the gash."
                    talk hrn talk "No. Suck on your scratch if you like, this is serious."
                    set data.ScratchFight true
                    "She moves away from you."
                    talk hrn talk "There's bandages in here."
                    "She rummages in the case and shows you an aluminium tube."
                    talk hrn talk "Antiseptic. Heat plasters. We're not wasting this on your fucking *scratch.*"
                    choice:
                        "You feel panic in your chest again."
                        "'It's a CUT, not a scratch!'":
                            talk em talk "It's a CUT, not a scratch!"
                            "Hornet doesn't answer. Instead, she snaps the plastic case shut again, and stuffs it into the bottom of her backpack. The click of the latches sounds devastating."
                            talk hrn talk "We're saving the medicine. Look, just get some sleep. I don't want to fight."
                            "She turns away, and starts taking off her scarf, to use it as a pillow."
                            add data.score -1
                            add data.tensionPoints 1
                            set data.hasFirstaid true
                            jump day2bedtime_opener2
                else:
                    "She looks startled."
                    talk hrn talk "What? What for?"
                    "Hornet has slipped the plastic case out of its slot, and is opening it."
                    talk em talk "My cut!"
                    set data.ScratchFight true
                    "You thrust out your hand, wincing. The wound has stopped bleeding, becoming a thin brownish line. It feels terrible. You begin imagining yourself with only one hand, or even one arm..."
                    "Hornet looks suddenly very irritated, only glancing at the gash."
                    talk hrn talk "What? There's nothing-"
                    "She seems to remember, and takes a second look at the scratch."
                    talk em talk "You're still going on about that?"
                    "She moves away from you."
                    talk hrn talk "There's bandages in here."
                    "She rummages in the case and shows you an aluminium tube."
                    talk hrn talk "Antiseptic. Heat plasters. We're not wasting this on your fucking *scratch.*"
                    choice:
                        "You feel panic in your chest again."
                        "'It's a CUT, not a scratch!'":
                            talk em talk "It's a CUT, not a scratch!"
                            "Hornet doesn't answer. Instead, she snaps the plastic case shut again, and stuffs it into the bottom of her backpack. The click of the latches sounds devastating."
                            talk hrn talk "We're saving the medicine. Look, just get some sleep. I don't want to fight."
                            "She turns away, and starts taking off her scarf, to use it as a pillow."
                            add data.score -1
                            add data.tensionPoints 1
                            set data.hasFirstaid true
                            jump day2bedtime_opener2

    else:
        "You haven't paid it any mind all day, but suddenly, the cut on the back of your hand throbs, hurting. You feel nauseous."
        choice:
            "You gasp in shock."
            "'Hornet, I *need* that!":
                talk em talk "Hornet, I *need* that!"
                if $data.FORlookedAtScratch:
                    "She looks over."
                    talk hrn talk "What, for your uh, cut?"
                    "Hornet has slipped the plastic case out of its slot, and is opening it. She holds out her hand."
                    talk hrn talk "Show me again?"
                    "You give her your hand, wincing. The wound has stopped bleeding, becoming a thin brownish line. It feels bad."
                    talk hrn talk "I don't know, Emily... How bad is it?"
                    choice:
                        "You can hear the doubt in her voice."
                        "'Terrible!'":
                            talk em talk "Terrible!"
                            talk em talk "I can barely move my fingers..."
                            "You give them a slight wriggle, for emphasis. You aren't lying, it really does feel bad. You haven't had pain like this since you got your molar pulled as a girl."
                            talk hrn talk "You're sure?"
                            "She rummages through the case, and pulls out a white strip of something."
                            choice:
                                talk hrn talk "There's enough antiseptic and gauze for one injury, I guess... Not much..."
                                "'I'm sure.'":
                                    talk em talk "I'm sure."
                                    set data.hasFirstaid false
                                "'On second thought...'":
                                    talk em talk "On second thought..."
                                    jump day2bedtime_noAid

                        "'On second thought...'":
                            talk em talk "On second thought..."
                            jump day2bedtime_noAid
                else:
                    "She looks over."
                    talk hrn talk "What for?"
                    "Hornet has slipped the plastic case out of its slot, and is opening it. She holds out her hand."
                    talk hrn talk "Show me?"
                    "You give her your hand, wincing. The wound has stopped bleeding, becoming a thin brownish line. It feels bad."
                    talk hrn talk "I don't know, Emily... How bad is it?"
                    choice:
                        "You can hear the doubt in her voice."
                        "'Terrible!'":
                            talk em talk "Terrible!"
                            talk em talk "I can barely move my fingers..."
                            "You give them a slight wriggle, for emphasis. You aren't lying, it really does feel bad. You haven't had pain like this since you got your molar pulled as a girl."
                            talk hrn talk "You're sure?"
                            "She rummages through the case, and pulls out a white strip of something."
                            choice:
                                talk hrn talk "There's enough antiseptic and gauze for one injury, I guess... Not much..."
                                "'I'm sure.'":
                                    talk em talk "I'm sure."
                                    set data.hasFirstaid false
                                "'On second thought...'":
                                    talk em talk "On second thought..."
                                    jump day2bedtime_noAid

                        "'On second thought...'":
                            talk em talk "On second thought..."
                            jump day2bedtime_noAid
        "She sighs."
        talk hrn talk "Very well. You know what's best."
        "She unscrews the cap of a tiny aluminium tube, and squirts out a thin, pale paste onto her finger. You offer your hand gingerly, and she begins spreading it."
        "Her hands are rough and calloused, but warm, and she's gentle. There's something almost soothing in her rhythm as she spreads it, in a circular motion, working the ointment into your skin."
        "Finally, she wraps the strip of gauze once around your hand, then seals it with adhesive tape."
        talk hrn talk "There you go."
        if (< $data.tensionPoints 2):
            "She looks beautiful in this light."
            "Before you know it, you've leaned down to kiss her on her freckled cheek."
            "She blinks at you, dark, mousy lashes encircling her big eyes. She seems startled, but not put off."
            talk em talk "My samaritan."
            "You smile. She smiles too."
            "Hornet snaps the case shut."
            add data.score 1
        choice:
            talk hrn talk "That should do it. Are you ready to sleep?"
            "'Yes. Thank you, Hornet.'":
                talk em talk "Yes. Thank you, Hornet."
                jump day2bedtime_opener2
        
    jump day2bedtime_opener2

day2bedtime_noAid:
    talk em talk "I think it'll be okay. It's only a scratch."
    "Hornet seems to like that. She takes your hand and plants a gentle kiss on the scratch. Suddenly, it feels better. Almost fine."
    talk hrn talk "I'm glad. We can save this in case something terrible happens, alright?"
    "That sounds... Frugal. You suppose she has a point. Maybe your hand will heal on its own. You watch her pack the medicine away."
    talk em talk "Alright. Let's go to bed, Hornet, I'm sleepy."
    set data.hasFirstaid true
    add data.tensionPoints -1
    jump day2bedtime_opener2

day2bedtime_opener2:
    clear_dialog
    set_screen blank    
    stop music
    " "
    "..."
    "..."
    "..."
    jump day2dream  