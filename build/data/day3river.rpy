day3river:
    play music empty
    set_screen swamp5
    "The morning comes, and Hornet looks no more like a dog than she ever has."
    "The wagon hasn't collapsed either. You eat a quiet breakfast, creamed corn and cold flatbreads that both taste of conservants."
    if $data.dreamDogEat:
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
    if (> $data.tensionPoints 2):
        "Hornet looks tired."
        choice:
            talk hrn talk "Looks like we're in for more walking."
            "'Not up to it?'":
                talk em talk "Not up to it?"
                "You taunt her. She ignores you."
                add data.tensionPoints 1
            "'It'll be alright.'":
                talk em talk "It'll be alright."
                talk em talk "We'll find something soon, I'm sure."
                "Hornet smiles."
                add data.tensionPoints -1
            "'What, are you getting tired? We can go back to your train car if you want. Sleep in, you've earned it, getting us all the way here to sewer central. *And* ruining my dress while you're at it! You're a real star, Hornet.'":
                talk em talk "What, are you getting tired? We can go back to your train car if you want. Sleep in, you've earned it, getting us all the way here to sewer central. *And* ruining my dress while you're at it! You're a real star, Hornet."
                talk em talk "Wow, Hornet,"
                "your voice is mocking now,"
                talk em talk "I wonder why you're so fucking poor! I wonder why you never even got a grade school education. With go-getter spirit like that? What are you tired? Do you not want to walk anymore? Do you not want to see the next fucking biome in store for us?"
                "You spit venom at her. You almost don't mean to, but the words are out now."
                "Hornet looks taken aback, hurt."
                talk hrn talk "...f-fuck yourself, Emily..."
                "she says, in a small voice, before hurrying off ahead. What just happened..?"
                add data.score -2
                add data.tensionPoints 2
                jump day3river_walk
    talk hrn talk "What is this place?"
    talk em talk "I don't know. I've never been this far out."
    "Hornet takes a moment to consider."
    choice:
        talk hrn talk "We twisted and wound around a lot in the fog. I'm not sure what direction this is, but..."
        "'We need to head that way.' (Point west)":
            "You gesture at the sun, still hanging low in the eastern sky, broken into several shards by the polluted sky. It'll mostly reassemble by noon."
            talk em talk "We need to head away from the sun. That'll be where the City is."
            if (> $data.tensionPoints 3):
                "You think you detect Hornet's nose wrinkling slightly."
                talk hrn talk "Well aren't you clever. Alright."
                if $data.OR.bagmention:
                    "Let's go then. I was already missing the sound of your suitcase rattling."
                    "You ignore her, but start walking."
                "You start walking, and Hornet follows."
            else:
                "Hornet's eyes widen a sliver."
                talk hrn talk "Oh, smart. I guess we can do that."
                "You start walking together."
    jump day3river_walk

day3river_walk:
    clear_dialog
    set_screen river2
    "The shore is quiet."
    "The river, straightened as it is, makes very little noise; there's a rhythmic growl where it laps at the boulders, but that's all."
    "To your right is a dense wall of tall trees, seemingly culled from the path long ago. It is mirrored across the river, though the air is too hazy to tell whether there's another path there."
    "You can't see much of anything in the distance- no bridges or boats, though there is a curve near the horizon that might obscure something."
    if (> $data.tensionPoints 2):
        "Your feet hurt badly. Your wrist too; like it or not, Hornet was right when she told you to bring a backpack. You can feel a cramp deep inside your arm, far more painful than that cut."
    "There's a gentle wind, and occasional birdsong."
    "What rushes have survived the thick dust don't sway, however; they're coarse and woody, sounding like dead leaves when you step on them."
    "Everything at ground level is smeared in that dust. An off-white colour already clings to your dress and Hornet's jacket."
    "It smells of"
    if (> $data.tensionPoints 4):
        "styrofoam."
        "It's a toxic smell. It digs deep into your nostrils, seeming to fill your every breath with that fine powder. You hope it isn't bad for you..."
        "Hornet seems to think about something. But when she glances at you, she seems to think better than to tell you."
        talk em talk "What is it?"
        talk hrn talk "Nothing. Save your breath."
        if (== $data.OR.cityfeeling 0):
            "There's a disinterested air about her."
        if (== $data.OR.cityfeeling 1):
            "There's a slight sadness to her."
            "You sort of wish things were different..."
            if $data.bagmention:
                "Then you remember her constant nettling."
                if $data.ScratchFight:
                    "Not to mention that deal with your cut. Your hand throbs. Is it already infected?"
                "Yeah, screw you, Hornet."
            else:
                "Then you remember that attitude she's so ready with..."
                if $data.ScratchFight:
                    "Not to mention that deal with your cut. Your hand throbs. Is it already infected?"
                "Yeah, screw you, Hornet."
        "She keeps walking, and you follow, a pace or two behind her."
        jump day3river_argue
    else:
        if (> $data.score 3):
            "peach pits."
            "It's a neutral smell. Not great, but sort of... homely."
            "After some time walking, Hornet slows down, and looks at you."
            talk hrn talk "I suppose I never told you why I wanted to leave the City, huh?"
            talk em talk "No..."
            if (== $data.OR.leaveReason 1):
                talk hrn talk "Well, you left because of your family..."
                "You nod, thinking back to the admonissions. The night of sobbing you endured when your sister told Mother, about Hornet and..."
                "You shake the memory aside."
            if (== $data.OR.leaveReason 2):
                talk hrn talk "Well, you left because of... You had your reasons."
                "Something plays across Hornet's face as she recalls your answer."
            if (== $data.OR.leaveReason 3):
                talk hrn talk "Well, you left because of the... The feeling, you said."
                "So many sleepless nights. So much time looking down at all the winding suprastructures. The great concrete circuit... Hornet lost somewhere within, crushing her life to powder in a warehouse..."
            talk hrn talk"But I just feel like..."
            if (== $data.OR.cityfeeling 1):
                talk hrn talk "Well. I know I said I *said* I felt sad about it. When we were looking down at it."
            if (== $data.OR.cityfeeling 2):
                talk hrn talk "I said earlier I felt nostalgic about it... When we were looking down at it, I mean."
            if (== $data.OR.cityfeeling 3):
                talk hrn talk "I... I know I said I hated it."
                "That wasn't nice of her, no. Though you can see why she felt that way. To a degree."
                talk hrn talk "When we were looking down at it there, I did feel that way, but..."
            if (== $data.OR.cityfeeling 0):
                talk hrn talk "I couldn't really think of something to say earlier. When we were looking down at it. I just wanted to get out of dodge, you know?"
            talk hrn talk "Only now, thinking about it that isn't quite right. I..."
            "She smiles."
            talk hrn talk "I guess I left for you, Emily. And for myself."
            talk hrn talk "Leaving for you *was* selfish, in a way. I... I know the road's been hard, but... we're walking it together, right?"
            "You feel a dampness on your cheek. You lean in to embrace her."
            "...a long moment passes."
            talk hrn talk "Are you okay?"
            talk em talk "Y-yeah. Sorry."
            "You remember your dreams... They almost feel foolish now. Say it."
            choice:
                talk pa talk "Don't say it. It'll hurt more if you do."
                "'I love you, Hornet.'":
                    talk em talk "I love you, Hornet."
                    set data.LOVE 1
                    "It seems to take her a moment, before she says,"
                    talk hrn talk "Love you too, Emily."
                    "Your heart is pounding."
                    "Hornet pulls your face down and kisses you."
                    "You haven't kissed since the fight, since before you agreed to come to the train."
                    "She lingers for a long moment, and you feel yourself turning into a nervous animal in her hands."
                    "When she pulls away, your hands are shaking."
                    talk hrn talk "Let's keep walking, okay?"
                    "You glance at the distance. It doesn't seem so far, now... And is that a flash of light, some pale structure...?"
                    talk em talk "O-okay, Hornet."
                    "Your heart is still thumping away at your chest. Did you do the right thing?"
                "'Thank you, Hornet.'":
                    talk em talk "Thank you, Hornet."
                    set data.LOVE 2
                    "She smiles again, and kisses your cheek."
                    talk hrn talk "Thank you, too. For coming with me."
                    talk hrn talk "Speaking of..."
                    "She looks over her shoulder, at the long road ahead. You think you see the light catch something, a brief white flash in the distance."
                    talk hrn talk "We should keep going. We need to find a shelter."
                    talk em talk "Yes. Let's..."
                    "Your heart is pounding. Did you do the right thing?"
            jump day3river_noargue
        "burnt paper."
        "Not a good smell, but you suppose it could be worse."
        "After some time walking, Hornet slows down, and looks at you."
        talk hrn talk "I suppose I never told you why I wanted to leave the City, huh?"
        talk em talk "No..."
        if (== $data.OR.leaveReason 1):
            talk hrn talk "Well, you left because of your family..."
            "You shiver, thinking back to the admonissions. The night of sobbing you endured when your sister told Mother."
        if (== $data.OR.leaveReason 2):
            talk hrn talk "Well, you left because of... You had your reasons."
            "Her mouth becomes a thin line remembering your answer."
        if (== $data.OR.leaveReason 3):
            talk hrn talk "Well, you left because of the... The feeling, you said."
            "So many sleepless nights. So much time looking down at all the winding suprastructures. The great concrete circuit..."
        "But I just feel like..."
        if (== $data.OR.cityfeeling 1):
            talk hrn talk "That place was killing me. There were places to hide, but, we was always..."
            "she casts around for the right words."
            talk hrn talk "I was always in the belly of the beast, I guess. Does that make sense?"
            "She seems distraught now."
            talk hrn talk "I... I felt like, after the section got signed into law, that was almost an excuse to finally get out. I couldn't even talk to anyone for the longest time..."
            talk hrn talk "So... I know this has been hard, and it might get harder, but..."
            choice:
                "She trails off."
                "(Embrace her)":
                    "You pull her into a hug."
                    "You can't tell, but you think she might appreciate it..?"
                    "She wipes a sleeve across her face after."
                    talk hrn talk "Thanks, Emily."
                    "She turns her face quickly."
                    "Did you do the right thing...?"
                "'It could be worse'":
                    talk em talk "It could be worse."
                    "You smile at her."
                    talk em talk "We haven't gotten caught yet, and..."
                    talk em talk "we still have each other."
                    "That seems to cheer her."
                    talk hrn talk "Th-thanks, Emily..."
                    add data.tensionPoints -1
                    add data.score 1
        if (== $data.OR.cityfeeling 2):
            talk hrn talk "I..."
            "She has trouble composing her next sentence."
            talk hrn talk "I really... miss some of my friends, from there, you know."
            talk hrn talk "And my little brother. You never met him, he..."
            talk hrn talk "well, anyway."
            "She shakes something off."
            talk hrn talk "I just couldn't be there anymore. It was doing such terrible things to everyone around me, to me, to..."
            if (> $data.score 1):
                talk hrn talk "to us..."
            "another shake. She's not looking you in the eye."
            talk hrn talk "Well... If that makes sense, there's why."
            "She looks sad."
            choice:
                "(Embrace her)":
                    "You pull her into a hug."
                    "You can't tell, but you think she might appreciate it..?"
                    "She wipes a sleeve across her face after."
                    talk hrn talk "Thanks, Emily."
                    "She turns her face quickly."
                    "Did you do the right thing...?"
                "'You did the right thing.'":
                    talk em talk "You did the right thing."
                    "You smile at her."
                    talk hrn talk "But..."
                    talk em talk "There's no way you staying there would have helped any of them."
                    talk em talk "Plus we haven't gotten caught yet, and..."
                    talk em talk "we still have each other."
                    "That seems to cheer her."
                    talk hrn talk "Th-thanks, Emily..."
                    add data.tensionPoints -1
                    add data.score 1
        if (== $data.OR.cityfeeling 3):
            talk hrn talk "I just... REALLY hated it."
            "You feel your gut tighten. Not this again..."
            talk hrn talk "The streets. Endless rows of them. The blocks so high you couldn't see the sky sometimes. The stink of sewage on the morning commute..."
            talk hrn talk "After my brother died,"
            "What..? You didn't know she had a brother..."
            talk hrn talk "well... there's no way to change it now. But I'm not going to go like that."
            talk hrn talk "I've seen rats... in traps. They try to gnaw their way out. That's I'm doing, you get it?"
            "She's opening and closing her fist."
            choice:
                talk hrn talk "With a fucking... fervor... I'll bring it back home someday. Maybe. But until then I want to put a thousand fucking miles between myself and that... that..."
                "'Enough!'":
                    talk em talk "Enough!"
                    talk hrn talk "That *scab.*"
                    "She looks up at you. The look in her eyes is a little scary."
                    "After a moment..."
                    "It passes. She opens her fist."
                    talk em talk "Are you done?"
                    talk hrn talk "Yeah. Sorry, I..."
                    choice:
                        talk hrn talk "I know you don't like hearing about it."
                        "'Good.'":
                            talk em talk "Good."
                            talk em talk "It's..."
                            talk em talk "it's not like I don't get you at all. Just... Lots of my family live there, okay? No matter what their... positions."
                            "In more ways than one. Hornet doesn't even know you have a cousin who signed the Section..."
                            "For a moment, you feel guilt. It passes."
                            talk hrn talk "Let's keep walking."
                            talk em talk "Yeah."
                        "'Don't bring it up again'":
                            talk em talk "Good. Then don't bring it up again."
                            "Her mouth becomes a thin line."
                            talk hrn talk "Hmmh."
                            talk em talk "..."
                            "A moment passes."
                            talk hrn talk "Well..."
                            talk em talk "Let's... Keep moving."
                            add data.tensionPoints 1
                            jump day3river_argue
        if (== $data.OR.cityfeeling 0):
            talk hrn talk "I..."
            "she thinks about her answer for some time."
            talk hrn talk "I couldn't stand it in there. I mean..."
            talk hrn talk "neither could you, I guess. But it was almost... boring. So tedious. Days and days and days of work. No future."
            "You're about to respond, but she cuts in,"
            talk hrn talk "And I mean *no* future. I know you were raised on your... *diet* of aspirations and all that. That anyone can hope to have what you had."
            talk hrn talk "But that's just more... crystal screens. Just another graphic slogan on a magazine. Does that make sense?"
            choice:
                "You can see her desperately wanting to make you understand now."
                "'Things could have gotten better...'":
                    talk em talk "Things could have gotten better..."
                    "she laughs."
                    talk hrn talk "Ha. I guess? I was always hearing that, but... I had a brother. He's..."
                    talk hrn talk "he's not around anymore. The City took him, you know? And now, that..."
                    talk em talk "the Section."
                    talk hrn talk "That obscenity, yeah. Now that it's in place... There really is no future. Not for me, I don't think."
                    "Maybe not even for you."
                    "Hornet is shaking a little."
                    choice:
                        "(Embrace her)":
                            "You pull her into a hug."
                            "You can't tell, but you think she might appreciate it..?"
                            "She wipes a sleeve across her face after."
                            talk hrn talk "Thanks, Emily."
                            "She turns her face quickly."
                            "Did you do the right thing...?"
                        "'You did the right thing.'":
                            talk em talk "You did the right thing."
                            "You smile at her."
                            talk hrn talk "But..."
                            talk em talk "There's no way you staying there would have made anything better"
                            talk em talk "Plus we haven't gotten caught yet, and..."
                            talk em talk "we still have each other."
                            "That seems to cheer her."
                            talk hrn talk "Th-thanks, Emily..."
                            add data.tensionPoints -1
                            add data.score 1
        set_screen river3a
    jump day3river_argue

day3river_argue:
    if (> $data.tensionPoints 2):
        "You walk on."
        "The trees to your right rustle and sway in the wind, and a cloud of dust drifts from the lowest branches."
        choice:
            "It gives you a thought..."
            "'I wonder if we'll find any fruit.'":
                talk em talk "I wonder if we'll find any fruit."
                "Hornet scowls."
                "Her face is already sort of splotchy and red. She's very irritated."
                set_screen river3b
                play music riverBad
                talk hrn talk "What?"
                talk em talk "Fruit."
                "You point up at the trees. Hornet looks like you've gone insane."
                talk hrn talk "You think we'll find a supermarket up there?"
                choice:
                    "Oh. Is it possible..."
                    "'Hornet, do you not know where fruit comes from?'":
                        talk em talk "Hornet, do you not know where fruit comes from?"
                        "She goes bright red."
                        talk hrn talk "Is it..."
                        "She knows she doesn't."
                        if (> $data.tensionPoints 4):
                            talk em talk "Wow Hornet, you should have paid more attention in school."
                            add data.tensionPoints 2
                            "She freezes. There's something jovial in your voice. You can't stop yourself."
                            talk em talk "Didn't your parents teach you anything, Hornet? Fruit comes from *trees,* you fucking *child.*"
                            "The look on her face is very satisfying."
                            if $data.OR.bagmention:
                                "Especially after that shit she pulled with your bag. Who's laughing now?"
                            "Your cut is hurting less already."
                            set_screen blank
                            "Hornet turns her face away, and hurries ahead several paces. You don't rush to keep up, quietly enjoying your victory. You think you hear her gasping."
                            jump day3bedtime
                        choice:
                            talk hrn talk "I thought they made it."
                            "Taunt her":                            
                                talk em talk "Wow Hornet, you should have paid more attention in school."
                                add data.tensionPoints 3
                                add data.score -1
                                "She freezes. There's something jovial in your voice. You can't stop yourself."
                                talk em talk "Didn't your parents teach you anything, Hornet? Fruit comes from *trees,* you fucking *child.*"
                                "The look on her face is very satisfying."
                                if $data.OR.bagmention:
                                    "Especially after that shit she pulled with your bag. Who's laughing now?"
                                "Your cut is hurting less already."
                                set_screen blank
                                "Hornet turns her face away, and hurries ahead several paces. You don't rush to keep up, quietly enjoying your victory. You think you hear her gasping."
                            "Be nice":
                                "In the least condescending voice you can muster, you explain to her how fruit is grown."
                                "She seems very embarrassed, but at least you're not taunting her."
                                talk hrn talk "So you think there could be some... Wild fruit, here?"
                                talk em talk "I hope so, at least."
                                "It isn't likely. But anything's possible out here."
                                add data.tensionPoints -1
                        jump day3bedtime
        jump day3bedtime
    else:
        "You walk on."
        "The trees to your right rustle and sway in breeze, and a fine cloud of dust drifts from the lowest branches."
        choice:
            "It gives you a thought..."
            "'I wonder if we'll find any fruit.'":
                talk em talk "I wonder if we'll find any fruit."
                "Hornet slows, looks over at you."
                set_screen river3a
                talk hrn talk "What, sorry?"
                talk em talk "Fruit."
                "You point up at the trees. Hornet looks blank."
                talk hrn talk "You think we'll find a supermarket up there?"
                choice:
                    "Oh. Is it possible..."
                    "'Hornet, do you not know where fruit comes from?'":
                        talk em talk "Hornet, do you not know where fruit comes from?"
                        "She goes bright red."
                        talk hrn talk "Is it..."
                        "She knows she doesn't."
                        choice:
                            talk hrn talk "I thought they made it."
                            "Taunt her a little":                            
                                talk em talk "Wow Hornet, you should have paid more attention in school."
                                add data.tensionPoints 1
                                "She looks hurt."
                                talk hrn talk "Emily, you know that isn't funny."
                                "Immediately you feel bad"
                                talk em talk "Oh. I'm sorry Hornet."
                                "Shit. How do you get out of this one?"
                                "Your cut hurts, suddenly."
                                talk em talk "I was..."
                                talk em talk "Uh. Fruit. It. It's grown, in trees. Like leaves."
                                "It takes her a moment, then she raises her eyebrows, beckoning you on."
                                talk em talk "I was... trying to make a joke. I'm sorry Hornet."
                                "She takes a deep breath."
                                talk hrn talk "I see."
                                talk hrn talk "Don't... Joke about that again. And... yeah, food would be nice."
                                "She starts moving again. You hurry along, feeling yourself go red."
                            "Be nice":
                                "You explain to her how fruit is grown."
                                "She seems very embarrassed, but listens."
                                talk hrn talk "So you think there could be some... Wild fruit, here?"
                                talk em talk "I hope so, at least."
                                "It isn't likely. But anything's possible out here."
                                add data.tensionPoints -1
                        jump day3bedtime
    jump day3bedtime


day3river_noargue:
    set_screen river3c
    "The walk continues in mostly amicable silence."
    "You can't stop glancing at Hornet now. A lazy smile plays across her lips occasionally... She's never smiled much, and it's nice to see."
    "The wind picks up some of her hair and plays with it. She brushes strands of it from her face absent-mindedly."

    talk hrn talk "I'm glad to be out of the swamp. This is... Nice."
    talk em talk "Almost like a hike!"
    "That makes her laugh, though you don't quite get the joke."
    "She says she hopes the asphalt is easier on your suitcase, and your stomach tightens up. But then you realise she really means it."
    "In time..."
    jump day3bedtime