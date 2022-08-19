day2dream:
    if (> $data.tensionPoints 5):
        jump day2dream_worse
    else:
        if (< $data.score 1):
            jump day2dream_worse
        else:
            jump day2dream_bad

day2dream_bad:
    play music teasong
    set_screen tea2a
    set data.dreamDogEat false
    "You're in a robe."
    talk poet talk "It's making you uncomfortably hot."
    talk poet talk "The air in here is humid and heavy, feeling far too cramped."
    talk poet talk "Every surface is covered in tchotchkes. Every wall is hung with rugs, and the floor has many of them, and cushions."
    talk poet talk "The room turns to fog a few yards away, thick and roiling fog, light grey oblivion swallowing the polished cabinet and its many glasses."
    choice:
        talk poet talk "That cabinet is behind you, to your right-"
        "Left.":
            talk poet talk "-of course. It's to your left."
            "Not that those terms means much here."
    talk poet talk "Across it is the window."
    talk pa talk "Don't look. Not now."
    talk poet talk "Try to ignore it."
    "There are dogs all around you. Many of them, in figures, carved onto furniture, woven into pillows, painted on plates."
    talk poet talk "Each and every one of them faces away from you, seeming all to have forgotten you."
    talk poet talk "They trod home,"
    talk pa talk "heeling,"
    choice:
        talk poet talk "to their masters."
        "Why am I in here?":
            "You're always in here."
            talk poet talk "No use pretending otherwise."
        "When can I leave?":
            "Whenever you want, I guess."
            talk poet talk "Difficult to, though. You'd need to work very hard on it."
            talk poet talk "You've not left it often. Running from the City was a good first step."
            "But there's so far left to go. The mask on the cabinet ignores you, and yet..."
            "it seems to look almost"
            "disdainful."
    "Something stirs in the mist."
    talk poet talk "Is it time?"
    talk poet talk "I believe it's time. And yes, there the knock comes,"
    talk poet talk "and there the slender arm. The figure is slender and androgynous, with short hair."
    "a curtain parts, and the figure passes down a fine china cup."
    set_screen tea2a
    "you take it,"
    if (> $data.score 1):
        "carefully."
    else:
        "spilling some droplets."
        "It's scalding hot, even the saucer, and you're shaking. You bite your lip as pain flares up along your forearm."
    "Your robe slips down to your wrist as you pull it closer."
    "Herd animals leap in frozen panic, woven in and out of the thread in many colours."
    "Something in you envies them their company... At least you have the robe."
    "The cup is small, and decorated with faceless dogs. All of them look the other way, none deigning to even glance at you."
    "You try to turn the cup, to force them into facing your way, but you only manage to spill some of the tea."
    talk poet talk "It smells of fruit."
    talk poet talk "Not in an appetizing way - in a dry, dusty way. Apples and peaches turning into vinegar."
    "The figure is gone, now, by the way. Thought I should mention."
    choice:
        talk poet talk "The saucer, now spattered with watery dark red droplets, depicts a dense forest. You try not to dwell on it."
        "Drink some":
            "You lean in- "
            set_screen tea3
            "-and freeze."
            "It's Hornet again."
            talk poet talk "No tigre now, oh no."
            "This is almost worse. She's a great dark dog, slinking away from you through the night,"
            "about to vanish into the mist."
            "You feel panic take hold of you. Where is she going?"
            "You try to call her name, but whether she hears you or not,"
            "she's not stopping."
            "She's running back to... to where?"
            talk poet talk "where else?"
            choice:
                talk pa talk "...that Celice woman. That was her name."
                "No!":
                    "You try to stop her, to call her back"
                    "But the dog vanishes, and the cup is filled only with ripples"
                    "Why?"
                    talk poet talk "And trembling so bad you almost spill it, you set it down on the floor, before"
    jump day2dream_wake
    
day2dream_badOld:
    play music teasong
    set_screen tea2a
    set data.dreamDogEat false
    talk pa talk "This one is different."
    talk poet talk "It is. You're not alone in this room but it is far smaller"
    talk poet talk "that you can"
    talk poet talk "tell."
    "It's so hot."
    talk poet talk "There is intricate decor on every surface. Much of it is old. An odd mix of styles."
    talk poet talk "The lacquered wood cabinet to your left ho"
    talk poet talk "to your left"
    talk poet talk "to your right holds many glasses patterned with leaves and scales and geometric patterns there are also bottles in many shapes and sizes crystal and glass and glazed ceramic and fine bone ."
    talk poet talk "mounted along the walls are carvings of dogs basset hounds whippets dalmatians doberman wolfhounds loyal dogs all and all facing away from you"
    talk poet talk "behind you is a great woven red rug with a hundred thousand threads running through and through like capillaries, like the bubbles in your lung"
    talk poet talk "and you are wearing a"
    talk poet talk "silk robe."
    talk poet talk "wild herd animals graze and leap on the cloth."
    "The room is misty. Dense, scalding hot fog seems to crowd the oxygen from it,  making it hard to breathe. There's incense, too. A war mask watches you from a pedestal."
    "You try not to look at the window set into the wall behind you."
    talk poet talk "You don't want to know what's on the other side. You know it's too deep down. You're on the precipice in here."
    choice:
        "This is the tea room."
        "Do I like the tea room?":
            "No."
        "Do I like being here?":
            "Yes."
    "You're sitting on a cushion. It is relatively comfortable."
    talk poet talk "There is laughter in the air, far away. But it doesn't penetrate in here, oh no, no it"
    choice:
        talk poet talk "doesn't."
        "Ring the bell":
            "In the mist beyond your sight a curtain parts and rustles in the hot air"
    "Dogs are here"
    "Or is it a servant?"
    "..."
    choice:
        "It passes you a cup."
        "Why can't I see them?":
            "You take the cup."
    
    set_screen tea2b
    "You take the cup."
    "The saucer is hot to the touch"
    "freshly fired."
    "Deep deep forests and circling the cup"
    "Dogs"
    "They have no faces. Are they looking away from you on purpose?"
    "You begin turning it frantically, trying to get them to acknowledge you, but they are always leaving, only faster now..."
    "You almost spill some on your sleeve and feel hot tears on your cheeks before you stop."
    "The tea is red and very dark"
    choice:
        "It smells foul and sweet, like dead fruit"
        "Drink":
            "..."
            set_screen tea3
            "You can see someone else in the room with you now,"
            talk poet talk "reflected inside the cup."
            "It's her again. You almost drop it reflexively, but you seem frozen."
            talk pa talk "Not a tigre this time, she's a huge black dog,"
            talk pa talk "slinking away,"
            talk pa talk "back to her master-"
            talk pa talk "she's loyal but not to you-"
            talk pa talk "she wouldn't care if you died now."
            "not in this reflection she wouldn't"
            talk poet talk "She only cares about her 'Cel' girl. The rat-fuck poor girl. The fucking,"
            talk poet talk "Homewrecker."
            talk poet talk "She'll be dancing on her leash in no time."
            talk poet talk "She'll forget about you."
            talk poet talk "You feel hot tears on your cheek"
            talk pa talk "You feel hot tears on your cheek"
            choice:
                talk pa talk "Yoou    feel hot tears on your cheek"
                "Why does she want to leave me?":
                    talk poet talk "You need to be better. If you drink now it'll happen, you just watch and see. you will wake up in one minute"
                    talk poet talk "alone"
                    "You set down the cup. The mist obscures the reflection, but your hand is shaking, and some tea scalds and burns you, soaking into your robe. It clings to your skin, burning it,"
                    "You feel a scream catching in your thr"
                    jump day2dream_wake

day2dream_worse:
    set data.dreamDogEat true
    play music teasong
    set_screen tea1a
    talk poet talk "You are naked."
    talk poet talk "It is very, very hot in here. The air is humind and smells sweetly of rotting fruit."
    talk poet talk "Apples turning to vinegar"
    talk poet talk "Dogs everywhere. Black dogs, all facing you, every where you look."
    talk poet talk "They're on the walls and on your pillow and on the carved furniture and on the glasses in the drink cabinet and on the wallpaper and on the carpet there are a hundred million threads the colours of rotting apples and peaches in the grass weaving to form dogs slinking away."
    talk poet talk "All of them are looking at you."
    "They won't hurt you. They'll keep their distance and watch until you die, and then they will eat you cold."
    talk poet talk "Distantly there's chattering, but you can't pay attention to it. Fear is choking you."
    choice:
        talk poet talk "Fear of the dogs, and..."
        "What's in the window behind me?":
            "I can't tell you that."
            "Please, please don't look through."
            "None of us want to see what's past it... Perhaps we can fashion new drapes soon, alright, Emily?"
            talk poet talk "You can't see very far. The fog is dense, and so hot besides it's making your eyes water."
            talk poet talk "Hot tears burn on your skin."
    "Someone's at the door."
    choice:
        talk poet talk "Are you going to let them in?"
        "I don't want to.":
            talk pa talk "She has the key. Not your lucky day."
            set_screen tea1b
            "She passes you a cup. Your hands are trembling so bad..."
            "Droplets of scalding hot tea burn you, sloughing the skin off your legs and your arms whenever you spill any. Even the saucer is hot."
            talk pa talk "The tea smells of rotting fruit. It's poured here often."
            "The cup has dogs on it too. They're watching you, leaping around in a circle, a great feral pack of them. You feel horror dawning even at the thought..."
            talk pa talk "Take a fucking sip, babe."
            "You raise the cup to your lips, when-"
            set_screen tea3
            choice:
                talk poet talk "It's her again. The fucking she-bitch."
                "No...":
                    "Yes, I'm afraid."
                    talk pa talk "Not a tigre this time."
                    talk pa talk "She's a black dog, in the darkest night, keeping her distance. But she'll eat you all the same, eventually."
                    "She'll just abandon you first."
            talk pa talk "That's right. Dogs are tools. They're objects, but they serve only one master, and..."
            talk pa talk "She's mentioned her. This Cel person. Celice? It was Celice. That's who holds the leash. Rat fuck poverty stricken fucking Celice."
            "Hornet would be nothing without you. But she's going to do this to you?"
            "You even paid her fucking rent when she had that cold."
            "Rage flares in your stomach."
            "Hatred,"
            "and bitter fear."
            set_screen blank
            stop music
            talk poet talk "Wet noses will push their way into your ribcage."
            "The thought comes unbidden, and the cup is gone."
    jump day2dream_wake

day2dream_wake:
    set_screen blank
    play music empty
    "-"
    "You're in the train cart."
    "Hornet is dozing by you."
    "Would she really..."
    if $data.dreamDogEat:
        "...eat you? Leave you until you turn into carrion?"
    else:
        "...leave you? Abandon you to these endless woods?"
    "You don't wake her this time... You can't. If she's plotting to abandon you or... or worse... she'll just lie to you."
    "It's so dark you can't even see her. You feel her, and you can hear her..."
    talk em talk "Don't... leave me, Hornet..."
    "Sleep comes again, eventually, but the bad taste remains..."
    jump day3river