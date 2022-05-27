intro1:
    set_screen intro1
    clear_dialog
    set data.tensionPoints 0
    set data.score 0

    play music stationblues

    "The two of you have come a long way. All the way to Peele Station, the final stop on the west line."
    "The night is cool and Emily shakes a little. You wonder again why she didn't bring a coat."
    choice:
        talk em talk "Is this it?"
        "'I suppose so.'":
            talk hrn talk "I suppose so. Look, the train's stopped."
            "The lights slowly flicker inside the carriages. There's a quiet whine as the engines shut down. It'll hum to life in a few hours, to pick up factory workers."
            talk em talk "I don't want it to be. We have to keep going! Look!"
            "She points at a videocamera. It's trained at the tracks. Her arm is pale."
            talk em talk "They'll know we're here by the morning, Hornet!"
            choice:
                talk hrn talk "We have to keep going then."
                "'Why didn't you bring a jacket?'":
                    add data.tensionPoints 1
                    set data.askedAbJacket true
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
                "'Should we find a road?'":
                    talk hrn talk "Should we find a road?"
                    "Emily rubs her shoulder, and reaches down for her suitcase."
                    talk em talk "Good idea. Let's."
                    jump intro1_hesitate
        "'It can't be!'":
            talk hrn talk "It can't be!"
            "Emily thinks for a moment."
            talk em talk "Yes. You're right. We need to keep going. Let's get out of dodge."
            "She points at a videocamera. It's trained at the tracks. Her arm is pale."
            talk hrn talk "You think it's on?"
            talk em talk "Why bother finding out? In the morning this place will be full of people anyway. Let's get moving."
            choice:
                "She begins dragging her suitcase across the ground. It makes a low rumbling sound."
                "(Follow along)":
                    jump intro1_hesitate

intro1_hesitate:
    set_screen intro2
    "Emily stops suddenly. She stares at a whirring automaton. Within its clear plastic casing, cans and cellophane packages beckon."
    talk em talk "H-hang on, Hornet..."
    "She reaches into her purse and pulls out a coin, leaning closer, staring into the machine's innards."
    "Insects buzz through the air. They like the light."
    "They make you think of the people back at the City... They like light, too. You shiver a little."
    choice:
        "Emily's pale fingers tap on the clear plastic."
        "'What are you doing!?'":
            add data.tensionPoints 1
            talk hrn talk "What are you doing!? We don't have time for this!"
            talk em talk "Look, I just..."
            "She appears to be having trouble deciding what to pick."
            talk em talk "I want to... We might not see one of these for a while..."
            choice:
                "She's right. You have no idea where you're going."
                "(Let her continue)":
                    set data.letGetSoda true
                    "She considers for a moment, then presses in two worn little metal buttons. She slots the coin into the automaton."
                    "After an agonizing while the mechanism picks an aluminium can out of the array, and drops it with a heavy clank into the retrieval slot."
                    "Emily bends over and her long fingers slip past the plastic flap."
                    talk em talk "Ack! Cold!"
                    talk hrn talk "What were you expecting? You bought a soda!"
                    "She trembles again, ever so slightly, as a breeze blows through the station. Metal creeks somewhere."
                    choice:
                        talk em talk "You want some?"
                        "(Yes)":
                            set data.hasSoda false
                            add data.tensionPoints -1
                            talk hrn talk "Sure."
                            "She eagerly pops it open, and even lets you sip it first. It's achingly sweet and very cold indeed."
                            "The two of you take turns quietly sipping the drink. After a while, the can is empty."
                            talk hrn talk "Thank you."
                            talk em talk "That was... that was nice. Pa never let me have these, you know?"
                            jump intro1_leave
                        "(No, save it)":
                            set data.hasSoda true
                            talk hrn talk "Save it, you'll be happy to have it later. Come on."
                            "She eyes the can longingly."
                            talk em talk "If you say so..."
                            "She drops the slender cylinder into her case."
                            jump intro1_leave
                "(Put a stop to this)":
                    set data.hasSoda false
                    set data.letGetSoda false
                    add data.tensionPoints 1
                    "Glancing nervously at the camera, you pull her away by the wrist."
                    talk hrn talk "Come on. Let's go. I brought some sweets anyway."
                    "She tries to worm free of your grip for a moment, then relents. Her suitcase begins rattling along again."
                    talk em talk "Fucking... Fine..."
                    jump intro1_leave
        "(Watch her)":
            set data.letGetSoda false
            "After some consideration, she pushes in two worn little metal buttons, and slots the coin into the automaton."
            "After an agonizing wait, the mechanism picks an aluminium can out of the array and drops it with a clank into the retrieval slot."
            "Emily worms her slender fingers under the plastic flap."
            talk em talk "Ack! Cold!"
            talk hrn talk "What did you get?"
            talk em talk "F-fizzy pop... Pa never let me have these..."
            choice:
                "She's about to open the latch on the drink."
                "'Wait. Don't you want to save that?'":
                    set data.hasSoda true
                    talk hrn talk "Wait. Don't you want to save that?"
                    talk em talk "Hrmm..."
                    "She considers the colourful aluminium cylinder longingly."
                    talk hrn talk "You'll be happy for it later. C'mon."
                    talk em talk "S-sure, I guess..."
                    "She drops the can into her case."
                    talk em talk "Let's get going, Hornet."
                    jump intro1_leave
                "'Can I have some?'":
                    set data.hasSoda false
                    add data.tensionPoints -1
                    talk em talk "Yes, of course, Hornet!"
                    "She eagerly pops it open, and even lets you sip it first. It's achingly sweet and very cold indeed."
                    "The two of you take turns quietly sipping the drink. After a while, the can is empty."
                    talk hrn talk "Thanks."
                    "Emily discards the can and wipes her lips with the back of a wrist."
                    talk em talk "Let's get going, Hornet."
                    jump intro1_leave

intro1_leave:
    clear_dialog
    set_screen offramp1
    "The two of you walk along the station. There's an offramp that leads onto a beaten concrete track, flanked on either side by railway tracks. A roadsign points towards PEELE CO. POLYCARBON PLANT WEST."
    "Clumps of moss cling to the sign, to the makeshift fence meant to keep animals off the trail."
    "Even at night, the factory is alive. Flames sputter atop tall towers, casting odd shadows into the clouds."
    "The sky to the east is bright orange. The City."
    $if this.data.tensionPoints <= 0:
        "Emily looks forlorn."
        choice:
            "Maybe you should..."
            "(Try to hold her hand)":
                add data.score 1
                "You quietly let your hand slip out of your coat, and slip it into her own palm. She's cold, but a little smile plays across her face as you do."
                "She turns back again and watches the factory."
            "(Keep going)":
                "Now's not the time. You turn back to face the factory."
    talk em talk "We aren't going *there*, are we?"
    "That feeling in your chest."
    talk hrn talk "I don't know... I don't know..."
    "Running away was supposed to be liberatory and exciting. Have you already hit a dead end?"
    choice:
        "The feeling grows stronger. Tightness, panic rising."
        "'We have to head away from the City!'":
            talk hrn talk "We have to head away from the City!"
            talk em talk "Yes, we do..."
            "She glances over her shoulder. A gust of wind picks up some of her hair."
            talk hrn talk "I don't know. I don't know. This factory is just another part of the city, Emily."
            talk em talk "We definitely won't find anyone sympathetic here..."
            set_screen offramp2
            "Both of you turn to face the forest. It reaches for the night sky like a million tentative fingers, interlocking dark in dark, until it's hard to tell where the clouds begin. It seems to pulsate. The night is dark."
            talk em talk "Should we...?"
            talk em talk "Maybe this was a mistake..."
            talk hrn talk "Let's go. Whatever's there is going to be better than *that* place."
            jump intro1_exit
intro1_exit:
    "The two of you head towards the looming forest..."
    jump day1forest_offramp