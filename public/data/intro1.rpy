intro1:
    set_screen intro1
    clear_dialog
    play music stationblues
    "The two of you have come a long way. All the way to Peele Station, the final stop on the west line."
    "The night is cool and Emily shakes a little. You wonder again why she didn't bring a coat."
    choice:
        talk em talk "Is this it?"
        "('I suppose so.')":
            talk hrn talk "I suppose so. Look, the train's stopped."
            "The lights are slowly flickering out inside the carriages. There's a quiet whine as the engines shut down. It'll hum to life in a few hours, to pick up factory workers."
            talk em talk "I don't want it to be. We have to keep going! Look!"
            "She points at a videocamera. It's trained at the tracks. Her arm is pale."
            talk em talk "They'll know we're here by the morning, Hornet!"
            choice:
                talk hrn talk "We have to keep going then."
                "('Why didn't you bring a jacket?')":
                    talk hrn talk "Why didn't you bring a jacket?"
                    talk hrn talk "In fact, why didn't you bring ANYTHING warm?"
                    "Emily scowls."
                    talk em talk "You told me to dress warm. This is a warm dress."
                    talk hrn talk "It doesn't have sleeves!"
                    talk em talk "Besides, I like the colour."
                    "Her knuckles whiten on the grip of her suitcase and she starts dragging it towards the offramp."
                    talk em talk "Come on. We have to get going."
                    talk hrn talk "Let's."
                    "You follow along, a bitter taste in your mouth. Your bag swings at your side."
                    jump intro1_hesitate
                "('Should we find a road?')":
                    talk hrn talk "Should we find a road?"
                    "Emily rubs her shoulder, and reaches down for her suitcase."
                    talk em talk "Good idea. Let's."
                    jump intro1_hesitate
        "('It can't be!')":
            talk hrn talk "It can't be!"
            "Emily thinks for a moment."
            talk em talk "Yes. You're right. We need to keep going. Let's get out of dodge."
            "She points at a videocamera. It's trained at the tracks. Her arm is pale."
            talk hrn talk "You think it's on?"
            talk em talk "Why bother finding out? In the morning this place will be full of people anyway. Let's get moving."
            choice:
                "She begins dragging her suitcase across the ground. It makes a low rumbling sound."
                "(Follow along.)":
                    jump intro1_hesitate

intro1_hesitate:
    set_screen intro2
    "Emily stops suddenly. She stares at a whirring automaton. Within its clear plastic casing, cans and cellophane packages beckon."
    talk em talk "H-hang on, Hornet..."
    "She reaches into her purse and pulls out a coin, leaning closer, staring into the machine's innards."
    choice:
        "Insects buzz through the air. They like the light."
        "('What are you doing!?')":
            talk hrn talk "What are you doing!? We don't have time for this!"
            talk em talk "Look, I just..."
            "She appears to be having trouble deciding what to pick."
            talk em talk "I want to... We might not see one of these for a while..."
            choice:
                "She's right. You have no idea where you're going."
                "(Let her continue.)":
                    "She considers for a moment, then presses in two worn little metal buttons. She slots the coin into the automaton."
                    "After an agonizing while the mechanism picks an aluminium can out of the array, and drops it with a heavy clank into the retrieval slot."
                    "Emily bends over and her long fingers slip past the plastic flap."
                    talk em talk "Ack! Cold!"
                    talk hrn talk "What were you expecting? You bought a soda!"
                    "She trembles again, ever so slightly, as a breeze blows through the station. Metal creeks somewhere."
                    choice:
                        talk em talk "You want some?"
                        "('Yes')":
                            talk hrn talk "Sure."
                            "She eagerly pops it open, and even lets you sip it first. It's achingly sweet and very cold indeed."
                            jump intro1_leave
                        "('No')":
                            talk hrn talk "Save it, you'll be happy to have it later. Come on."
                            jump intro1_leave
                "(Put a stop to this.)":
                    "Glancing nervously at the camera, you pull her away by the wrist."
                    talk hrn talk "Come on. Let's go. I brough some sweets anyway."
                    "She tries to worm free of your grip for a moment, then relents. Her suitcase begins rattling along again."
                    talk em talk "Fucking... Fine..."
                    jump intro1_leave
        "(Watch her.)":
            "test"

intro1_leave:
    clear_dialog
    "blank"