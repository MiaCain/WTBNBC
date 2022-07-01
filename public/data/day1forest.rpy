day1forest_offramp:
    clear_dialog
    play music empty
    set_screen blank
    "The night feels especially cold now that you're off the pathway."
    choice:
        "The rattling of Emily's trunk has been replaced by a dull thumping as it bounces over dusty ground and coarse wild rushes."
        "'I still can't believe you didn't just bring a backpack.'":
            talk hrn talk "I can't believe you didn't just bring a backpack. That thing is going to break once we find ourselves in rough terrain."
            talk hrn talk "Those heels too, actually..."
            "Emily gives you an irritated look."
            "Familiar. Copper in your mouth."
            if (< $data.tensionPoints 1):
                talk em talk "Can you not nag me?"
                talk em talk "I know what I'm doing."
                "Suddenly, the air between is tinged with bitterness. And just when you were having a nice time, too..."
                "You wonder if it was a good idea to bring Emily."
            else:
                talk em talk "Shut up, Hornet. I can deal with it myself."
                "The air between you becomes bitter."
                "A familiar feeling, at least."
                "You wonder if it was a good idea to bring Emily."
            set data.OR.bagmention true
            add data.tensionPoints 1
            jump day1forest_cityview
        "(Ignore it)":
            set data.OR.bagmention false
            "You decide to let her be, and keep walking for a little while longer."
            jump day1forest_cityview


day1forest_cityview:
    "You crest a rise, and are greeted with..."
    set_screen offramp3
    talk hrn talk "The City."
    talk em talk "It looks so tiny from here..."
    "You couldn't disagree more. It fills the entire horizon. It's dead night, but the City still glows. Angry neon. It screeches at the sky."
    "Traffic roaring, even all the way up here."
    "The railway heads to the station where you departed. Along the tracks, the inner city fades into crowded suburbs, which eventually dissolve altogether."
    "Not so in the other directions; hill upon hill reach out into the darkness, grids of electric light imposed upon them by the metropole."
    "It seems so vast. Will you ever leave it?"
    talk hrn talk "Do you know how big it is?"
    "She shrugs."
    talk em talk "On paper. Did you not learn in school?"
    talk hrn talk "..."
    "You watch the city for a minute."
    choice:
        talk em talk "What does it make you feel?"
        "'Nothing'":
            set data.OR.cityfeeling 0
            talk hrn talk "Nothing. We're getting out, that's what matters. It's just buildings and neon now."
            talk em talk "What about the people?"
            choice:
                "She seems put off."
                "(Shrug and move on)":
                    jump day1forest_trees
        "'Sadness'":
            set data.OR.cityfeeling 1
            talk hrn talk "Sad, I suppose. Lots of... bad stuff in there."
            talk hrn talk "All those empty buildings, all that bad air..."
            "Emily frowns at your answer."
            talk em talk "Ah, I see."
            "You decide to move on."
            jump day1forest_trees
        "'Nostalgia'":
            set data.OR.cityfeeling 2
            add data.tensionPoints -1
            talk hrn talk "I don't know. Despite all of it, we..."
            talk hrn talk "We had some nice times here, you know?"
            talk hrn talk "Even though I'm glad we're getting out."
            "She smiles warmly."
            talk em talk "I think so too. It'll always be our City."
            "The thought isn't that appealing to you, but you decide to move on."
            jump day1forest_trees
        "'Hate'":
            set data.OR.cityfeeling 3
            add data.tensionPoints 1
            talk hrn talk "Bad. Fuck this place. Fuck everything it's done to us."
            "She looks shocked."
            talk em talk "I-"
            talk hrn talk "Fuck everthing it's done to ME, at least. I hope I never see it again."
            "Emily can't think of anything to say, it seems. Her eyes shine with the sky's orange tint."
            talk hrn talk "Let's go."
            jump day1forest_trees

day1forest_trees:
    set_screen blank
    "The city is still reeling through your head. Thinking about it, you remember a slogan sprayed on a concrete wall by the canal off of Metternich Square. It said..."
    "'IT'S KILLED AL L OF IT/"
    "EVeN THE S TARS'"
    "Whoever wrote it wasn't wrong. There isn't a single star visible tonight. Even the moon, which you've seen on a good night now and then- (when getting kebabs with coworkers after a late shift)"
    "-is nowhere at all. Its dreadful to think about."
    "You suppose the City was never as bad for Emily in her family's polyceramic high-rise as it was for you. If it wasn't for the Section getting passed, she might never have-"
    set_screen forest1
    play music forestsong
    "You're startled to find yourself amidst the trees already. It's gotten darker, but the wind is almost gone now, beyond the quiet rustling of the pines far above."
    "The ground is littered with needles, most of them grey and brown. No grass or underbrush grows here."
    choice:
        "Emily shivers."
        "(Offer her your coat, quietly)":
            "You open your coat, showing Emily your warm sweater and scarf, raising your brow as a silent question."
            if $data.OR.bagmention:
                "She shoots you a reproachful look, then keeps moving. You feel a little bad."
                set data.FORhasCoat false
                jump day1forest_cont

            else:
                if (> $data.tensionPoints 3):
                    "She shoots you a reproachful look, then keeps moving. You feel a little bad."
                    set data.FORhasCoat false
                    jump day1forest_cont
                "She gives you a little smile, and accepts. You watch her put it on, then pull a few trapped strands of hair free with a flick."
                "The rough black corduroy goes quite well with her pale dress. You ignore the sudden chill at your back."
                set data.FORhasCoat true
                jump day1forest_cont

        "(Ask if she wants to borrow your coat)":
            talk hrn talk "Do you want to use this for a while? Me having a sweater and all."
            if $data.OR.bagmention:
                "She shoots you a reproachful look."
                talk em talk "No, I think I'll be fine, thank you."
                "Her pace quickens, and her trunk bounces on a stray root. You hurry to keep up."
                set data.FORhasCoat false
                jump day1forest_cont
            else:
                "She gives you a little smile."
                talk em talk "Thanks, Hornet."
                "You watch her put it on. She pulls a few trapped strands of hair free with a flick."
                "The rough black corduroy goes quite well with her pale dress. You ignore the sudden chill at your back."
                set data.FORhasCoat true
                jump day1forest_cont
        "(Ignore her)":
            set data.FORhasCoat false
            add data.tensionPoints 1
            "You don't pay her any mind. She should have listened to you in the first place."
            "Something inside you feels maliciously triumphant. Of COURSE it was going to be cold!"
            jump day1forest_cont

day1forest_cont:
    "You keep walking for a while."
    "Fatigue is starting to set in. The forest is repetitive, endless rows of slender tall pines. Real enough, but planted to feed industry, all the same."
    "There is little wildlife. You hear birdcalls now and then, and you can see insects flit through the air just in front of you."
    if (<= $data.tensionPoints 2):
        talk em talk "Hornet?"
        talk hrn talk "Hm?"
        talk em talk "I'm scared. I don't think I want to do this anymore."
        if $data.FORhasCoat:
            "She pulls your coat tighter around herself."
        choice:
            talk hrn talk "Hey now..."
            "'It could be worse'":
                talk hrn talk "It could be worse."
                "She sniffs."
                talk hrn talk "We could have gotten caught at any point so far. Even at Central Station. Even before then."
                "You rub her shoulder."
                talk hrn talk "We've made it this far, we'll find a way forward."
                talk em talk "You think so? We don't even know what's out there..."
                talk hrn talk "Yeah. Let's just find a place to rest, alright?"
                talk em talk "Okay. Thank you, Hornet."
            "'It'll be ok'":
                "You smile at her."
                talk hrn talk "It'll be okay, Emily. We'll get to somewhere new."
                talk hrn talk "With more room to breathe. You won't need to hear the electric droning in the walls ever again, okay?"
                "She seems comforted."
                talk em talk "Thank you, Hornet. I-"
                talk em talk "I don't know what I'd do without you. Let's move on."
                add data.score 1
            "(Embrace her)":
                "You pull her into a hug. She silently shivers, some tension going out of the lanky girl."
                "Emily's always liked physical attention more than you."
                "The moment passes. You think you see her smile as you move on."
                add data.score 1
        "Comforted, you keep trecking into the woods..."
    set_screen forest2    
    "Loud noise interrupts your wandering. Looking up, you see black shapes against the sky."
    talk em talk "Helicoptres-!"
    "You pull her towards you, next to one of the million identical tree-trunks, and the two of you watch the procession."
    "They look like tadpoles darting across a pond."
    "Floodlights hang from some of their bellies. It's impossible to say whether they're looking for fires,"
    "escapees,"
    "or Emily."
    talk em talk "They're so loud!"
    "Emily whines over the din. They are; it sounds like half a dozen trains passing over you, carbon rotors slicing through the heady air."
    choice:
        talk em talk "Do you think they're-"
        "'Looking for us? Probably.'":
            set data.FORHelicoptLooking true
            talk hrn talk "Looking for us? Probably. C'mon, keep your head down."
        "'No, they aren't.'":
            set data.FORHelicoptLooking false
            talk hrn talk "No, I don't think they're looking for us."
            talk hrn talk "But keep your head down anyway, okay?"
    "She looks irritated for a moment."
    if $data.FORHelicoptLooking:
        choice:
            talk em talk "That's not what I meant. I was asking if you think they're scary."
            "'That's the same thing!'":
                add data.tensionPoints 1
                talk hrn talk "That's the same thing!"
                "She looks very angry at that, and turns away."
                talk em talk"Look I just hope they're gone soon..."
                "she hisses."
            "'Oh. Yeah, they are.'":
                add data.tensionPoints 1
                talk hrn talk "Oh. Yeah, they are."
                if $data.FORhasCoat:
                    "She bundles herself up in your coat, like she's trying to hide."
                talk em talk "O-oh. I hope they'll move on soon..."
    else:
        choice:
            talk em talk "That's not what I meant. I was asking if you think they're scary."
            "'That's the same thing!'":
                add data.tensionPoints 1
                talk hrn talk "That's the same thing!"
                "She looks very angry at that, and turns away."
                talk em talk"Look I just hope they're gone soon..."
                "she hisses."
            "'Oh. Yeah, they are.'":
                add data.tensionPoints 1
                talk hrn talk "Oh. Yeah, they are."
                if $data.FORhasCoat:
                    "She bundles herself up in your coat, like she's trying to hide."
                talk em talk "O-oh. I hope they'll move on soon..."
            "'Like I said, they're not.'":
                talk hrn talk "Like I said, They're just doing their job. Probably surveying for fires."
                "She seems to like that."
                talk em talk "Still, I hope they'll move on soon."

    set_screen blank
    "It's not long before her wish is granted, and the tadpoles clear from their muddy grey pond."
    "You come out from your poor hiding spot and keep moving."
    jump day1forest_cut

day1forest_cut:
    set_screen blank
    "Emily suddenly gasps in the darkness. You whirl around to see what the matter is."
    talk hrn talk "Emily!?"
    choice:
        talk em talk "My hand! My hand!"
        "(Take a look)":
            set data.FORlookedAtScratch true
            "You lean in."
            set_screen forest2b
            "There's a small cut on her left hand. It's barely bleeding; You've seen people get much worse at the warehouse. A whole arm once."
            talk hrn talk "Emily... It's not so bad. It'll heal in no time, you'll see."
            talk em talk "What if I get blood poisoning!?"
            talk hrn talk "You won't. And even if, we can take care of it."
            "You're trying to keep exasperation out of your voice."
            talk hrn talk "Let's find somewhere to sleep, okay? It's getting very late."
            talk em talk "O-okay Hornet."
            jump day1bedtime
        "(Keep moving)"
            set data.FORlookedAtScratch false
            add data.tensionPoints 1
            talk hrn talk "Keep your voice down, Emily, we have to keep going."
            "You feel irritation well up inside you. Your chest feels tight."
            talk hrn talk "Unless you want those helicoptres back?"
            talk em talk "N-no, I guess not..."
            "She follows along again, meekly."
            jump day1bedtime
    