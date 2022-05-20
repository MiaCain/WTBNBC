day2swamp:
    clear_dialog
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
        "'A peat bog?'":
            talk em talk "A peat bog?"
    talk hrn talk "That's the one."
    $if this.data.tensionPoints < 4:
        talk hrn talk "Thanks."
        choice:
            talk em talk "Speaking of..."
            "'Thank you for the coat. I slept very well.'":
                talk em talk "Thank you for the coat. I slept very well."
                "Hornet smiles, gazing up at you."
                talk hrn talk "Oh, my pleasure. I have my scarf and sweater, anyway."
            "'Thank you for sticking with me. I wouldn't have made it this far alone.'":
                talk em talk "Thank you for sticking with me. I wouldn't have made it this far alone."
                talk hrn talk "No problem."
                "She nods, seeming preoccupied with the way ahead."
    "You walk to the edge of the bog. The trees keep growing, but in full disarray now, and further apart. They seem slimmer, their crowns yellow, horizontal gashes and eyes in black burned into their bark."
    "You know these - birches, from an old school book, but think better than to bring it up now."
    "There are birdcalls from within the bog, but it's mostly quiet."
    "You see a pale, opalescent sort of shimmer in the air high above. The way it plays with the light reminds you of petrol on asphalt."
    "Hornet points at a wooden structure some distance off."
    talk hrn talk "Look, a catwalk."
    "It's just a walkway, but you nod. It looks rickety. As you draw closer, you can see the wood is pale, almost like driftwood, though none of the boards are damaged or missing."
    "It leads off into the fog."
    talk hrn talk "Well..."
    "She casts her gaze around."
    choice:
        talk hrn talk "I suppose there's nothing for it?"
        "'Let's go.'":
            talk em talk "Let's go."
    jump day2swamp_cont


day2swamp_cont:
    set_screen swamp2
    "Hornet steps up first, taking one tentative step, then another, then beckoning for you to follow."
    "You begin pulling your suitcase along the walkway, slowly at first, until you settle into a pace."
    "It's only about a foot above the surface of the bog, but seems sturdy enough. Rushes and reeds occasionally reach up to toy with your dress, but it's better than wading through a swamp."
    "Far overhead, the oily sheen in the air is stirring with the mist. Now and then the heavily diffuse sunlight is shattered into odd colours, but mostly the effect is content just to stir between the leaves and leave you interlopers in peace."
    choice:
        "Your case is thumping on the boards rhythmically. You envy Hornet her backpack."
        "'Damn suitcase...'":
            add data.tensionPoints 1
            $if this.data.bagmention:
                "Hornet freezes for a moment, and you almost bump into her."
                talk hrn talk "Yeah,"
                "she snarls,"
                talk hrn talk "You should have brough a backpack, Emily."
                "There's something very bitter in her voice. it makes you uneasy."
                add data.score -1
            talk hrn talk "I did *tell* you."
            "She moves a little faster, neglecting to even look back at you."
            "Something about this feels like an open wound; it makes you very uncomfortable."
        "Say nothing":
            "You stay quiet."
    "You keep walking in silence for some time."
    "Thump, thump, thump, thump, thump. Your feet feel tired, squeezed into these boots, and you have to switch hands every now and then, the suitcase tugging at your wrist."
    "Eventually, Hornet slows her pace a little, and gazes into the mist."
    talk hrn talk "I'm glad you agreed to meet me at the Station, Emily, but..."
    "She struggles for a moment."
    talk hrn talk "What was it that made you finally agree? Why did you run away?"
    choice:
        "Her eyes meet yours, and you look away after a moment. Sudden fear wells inside you. What *was* it?"
        "'I couldn't stand them, my sister...'":
            set data.OR.leaveReason 1
            talk em talk "I couldn't stand them, my sister..."
            "Your mother, too. And Pa. If she only knew half of what they..."
            "Before you can say more, Hornet nods."
            talk hrn talk "Ah. I understand."
            "There's a sort of pensive look about her now. You wonder if you should reach out and touch her, but the moment passes."
        "'I wanted to see something new.'":
            set data.OR.leaveReason 2
            talk em talk "I wanted to see something new."
            add data.tensionPoints 1
            $if this.data.tensionPoints >= 4:
                "A nasty look passes over her face for a brief second, then it's gone."
                talk hrn talk "Like a tourist, huh?"
                "You feel yourself flush. Just because you're not a factory worker doesn't mean she gets to..."
            talk hrn talk "Right. Well... Lots of trees, at least."
            talk hrn talk "Not that those are unheard of in *your* part of the city."
            talk em talk "Hornet..."
            "She walks a little faster. Conversation over."
        "'I wanted to get rid of this god-awful feeling.'":
            talk em talk "I wanted to get rid of this god-awful feeling."
            set data.OR.leaveReason 3
            "Hornet smiles."
            add data.tensionPoints -1
            talk hrn talk "Reference is vulgar, you know."
            talk em talk "You know the line? Well it's still true. That place is so..."
            "You cast around for a word, finding none."
            talk hrn talk "I know what you mean. Well..."
            "She gazes around, at the tall pale trees, the colours burning through the air overhead."
            talk hrn talk "Whatever feeling is here is something different, at least. I don't think I mind it."
            talk em talk "Y-yeah. Me either."
            "You keep walking in pleasant silence."
    jump day2swamp_fire


day2swamp_fire:
    clear_dialog
    set_screen swamp3
    "It must be early afternoon by the time you speak again, to share lunch. You wish there was coffee, but you don't even have a gas cooker."
    "After the meal, you gaze up at the sky. That everpresent sheen has caught alight in the sun, it seems; fire burns in the sky, lazily eating the air as though it were paper, the flames shredding themselves on invisible gusts like clouds."
    "Their silent and alien dance is oddly mesmerizing, though you're glad it's far away from you."
    talk em talk "Hornet, what do you think the flames are?"
    "She mulls it over a moment, watching them. Her dark eyes reflect the light, now turquoise, now silver, now orange."
    choice:
        talk hrn talk "I need to consider that. What do you think?"
        "'Doesn't matter.'":
            talk em talk "I don't think it matters. Any more than the trees."
            set data.BOGFireChoice 0
            "Hornet looks annoyed."
            talk hrn talk "Why ask then? Come on, let's pack up."
        "'Souls.'":
            talk em talk "I think it's souls. It seems a little sad."
            set data.BOGFireChoice 1
            "Hornet seems to consider this."
            choice:
                talk hrn talk "You think it's dead people?"
                "'Yes!'":
                    talk em talk "Yes! Though it might not remember being alive. Or even individual people. Just what people felt like."
                    talk hrn talk "Let's hope it doesn't get too close to us, anyhow. Come on, let's clean up here."
                "'Not exactly...'":
                    talk em talk "No, not exactly... It's hard to explain. Forget it, it's just a feeling."
                    talk hrn talk "I see. I think I know what you mean."
                    "She gazes up at the flames."
                    add data.tensionPoints -1
                    talk hrn talk "Well, in any case, let's get moving. We need to find a place that isn't this catwalk before it gets dark."
        "'Ghosts.'":
            talk em talk "I think it's ghosts. It seems a little scary."
            set data.BOGFireChoice 2
            choice:
                talk hrn talk "You think it's dead people?"
                "'Yes.'":
                    talk em talk "Yes. I want it to go away."
                    talk hrn talk "I agree with that at least. Come on, let's clean up here."
                "'Not exactly...'":
                    talk em talk "No, not exactly... It's hard to explain. Forget it, it's just a feeling."
                    talk hrn talk "Hmm."
                    "She gazes up at the flames."
                    add data.tensionPoints 1
                    talk hrn talk "I don't get you, Emily. Let's clean up here."
        "'Industrial waste.'":
            talk em talk "Industrial waste. Maybe they used to make petrol here."
            set data.BOGFireChoice 3
            "Hornet lets out a brief laugh."
            talk hrn talk "Ha! Yeah, you're right, stupid question."
            "The two of you look up at the methane and ozone stirring lazily."
            talk hrn talk "I suppose we're all industrial waste, come to think."
            "Maybe."
            talk hrn talk "Oh well."
            "She gets on her knees."
            talk hrn talk "Let's clean up."
        "'Friends.'":
            talk em talk "I think it's friends. It likes our company, and wants to play."
            set data.BOGFireChoice 4
            add data.tensionPoints 1
            "Her face falls a little."
            talk hrn talk "Emily, I was being serious..."
            "You feel a pang of guilt. Even though you were, too!"
            talk hrn talk "Look, let's just clean up."
            "She rises."
    "You help her clean, though you feel terribly clumsy next to her. She's like an automaton in one of Pa's factories."
    jump day2swamp_train

day2swamp_train:
    clear_dialog
    set_screen swamp5
    "At dusk you finally reach something new. A train carriage, half embedded in the swamp, older even than the one that brought you to the forest."
    "It juts out of the peat almost comically, a dusty turquoise in the evening fog. The fires have burned out now, and the sheen is invisible without light from overhead."
    "One of the windows is fully gone, broken from the inside. It seems dangerous, but might offer shelther..."
    talk hrn talk "Finally."
    "This time it's Hornet who has to stifle a yawn."
    talk hrn talk "I've no idea how far we've come, but that swamp must be miles long. Maybe we'll get to leave it come the morning."
    "She looks up at the sky. It's only slightly darker than the fog all around you."
    talk hrn talk "And no helicoptres that I can see."
    $if this.data.FORHelicoptLooking:
        talk em talk "You were wrong, looks like."
        "She scared you over nothing."
        talk hrn talk "Well..."
        "Hornet gives you a slightly sheepish look."
        talk hrn talk "I don't know. I'm only human."
    talk em talk "Do you think this place is any good?"
    "She takes in the carriage. It's lopsided, but close to the path... You could just step through the window..."
    talk hrn talk "Better than being out here. Let's get the baggage inside."
    "She begins taking off her backpack."
    "This seems like a bad idea, suddenly. The cart could crush you both, or come to life with humming neon..."
    choice:
        "Hornet is stepping through the window, her backpack in hand, kneeling down on a padded bench."
        "'I'd much rather sleep outside.'":
            "You muster up all your dignity and straighten up a bit."
            talk em talk "Hornet. I'd much rather we sleep outside. This is a bad idea."
            "She looks back at you."
            talk hrn talk "On the walkway? Are you crazy?"
            "Hot blood rushes to your head."
            talk em talk "Don't give me that! It looks unsafe!"
            $if this.data.tensionPoints > 5:
                "Who does this rat think she is!?"
            "Hornet turns back to look around the inside of the carriage, then pulls her feet in, and jumps on the seat."
            "You screech in shock. Birds startle, somewhere."
            "She kicks the inside of the carriage for good measure. The metal creaks, but the structure doesn't so much as tremble."
            "Her round face appears in the window again."
            choice:
                talk hrn talk "Seems sturdy enough to me. Come on in."
                "'Don't *do* that!'":
                    talk em talk "Don't *do* that!"
                    "Your heart is pounding in your ears."
                    choice:
                        talk hrn talk "Are you coming?"
                        "(Climb in)":
                            "You climb inside, fuming."
                            jump day2bedtime_firstaid
                        "'No!'":
                            talk em talk "No!"
                            talk hrn talk "Suit yourself. Sleep well out there."
                            $if this.data.tensionPoints > 5:
                                talk hrn talk "If you roll into the bog and die, do me a favour and take off my coat first."
                            add data.tensionPoints 1
                            "Horror wells up inside you for a moment, and you choke on a breath."
                            talk em talk "W-wait, Hornet, I didn't mean it-!"
                            "Before you know it, you're scrambling inside after her, heart pounding. Your dress catches on some stray bit of glass, and rips, but you barely notice."
                            "You embrace Hornet, trembling. She seems uncomfortable all of a sudden."
                            "You pull away, and turn your face to the side so she can't see how distraught you feel. Would she really have left you?"
                            jump day2bedtime_firstaid