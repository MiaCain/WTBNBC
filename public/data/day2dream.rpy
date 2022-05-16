day2dream:
    stop music
    $if this.data.tensionPoints > 5:
        jump day2dream_worse
    else:
        $if this.data.score < 1:
            jump day2dream_worse
        else:
            jump day2dream_bad

    
day2dream_bad:
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
            choice:
                talk pa talk "Yoou feel hot tears on your cheek"
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
    talk poet talk "They're on the walls and on your pillow and on the carved furniture and on the glasses in the drink cabinet and on the wallpaper and on the carpet there are a hundred million threads the colours of rotting apples and pears in the grass weaving to form dogs slinking away."
    talk poet talk "All of them are looking at you."
    "They won't hurt you. They'll keep their distance and watch until you die, and then they will eat you cold."
    "Wet noses will push their way into your ribcage."
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
            talk pa talk "The tea smells of rotting fruit. It gets drunken in here often."
            
    #WORSE DREAM

day2dream_wake:
    set_screen blank
    stop music
    #WAKE
    "-"
    "You're in the train cart."
    "Hornet is dozing by you."
    "Would she really..."
    $if this.data.dreamDogEat:
        "...eat you? Leave you until you turn into carrion?"
    else:
        "...leave you? Abandon you to these endless woods?"
    "You don't wake her this time... You can't. If she's plotting to abandon you or... or worse... she'll just lie to you."
    "It's so dark you can't even see her. You feel her, and you can hear her..."
    "Sleep comes again, eventually, but the bad taste remains..."
