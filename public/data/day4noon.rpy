day4noon:
    clear_dialog
    set_screen end4
    "By the time you settle Hornet down, you can see she's missing a leg too, even the boot it was in."
    "You seat her on her jacket, propped up against her backpack."
    $if this.data.tensionPoints > 5:
        talk hrn talk "Thanks, s-S..."
        "What now?"
        talk hrn talk "c-Cel..."
        play music empty
        "Not this again. You stand up, and look down at her."
        "Pathetic little broken creature. No one will even miss her."
        "You take a step back, then another. Suddenly, you're not even thinking about all the way you've come."
        "Nothing is further from your mind than the Section now."
        $if this.data.bagmention:
            "This creature and her fucking admonissions... Your nice dress and suitcase..."
        "Nothing but hate in her heart. For all the beautiful things in this world, in your City..."
        "You take another step back, then another."
        talk em talk "Try turning into a dog *now,* Hornet..."
        "you hiss. You take a final step back, then turn and duck out of the ruin, clutching your wounded hand."
        jump day4_endBad
    talk hrn talk "Thanks, Eh... e..."
    "She appears to slip into sleep. You check her throat, but she's breathing okay. She's burning hot to the touch."
    "You zip her bag open. Inside is an orderly set of necessities. A few changes of clothes, all dark. Food."
    $if this.data.hasSoda:
        "There..."
        "A smooth, cold aluminium can."
        set data.foundCan true
        choice:
            "It's heavy in your hand."
            "(Feed it to her)":
                add data.score 1
                "You pull out the soda you bought what seems like a lifetime ago. Your last time spending money."
                "The latch opens with a hiss. Soon you have her awake again. Her eyes are glassy."
                talk em talk "Drink this, dear."
                talk hrn talk "Thhn..."
                "Her lips part when she feels the aluminium, and she starts drinking eagerly."
                "Swallowing all of the cool liquid seems to cheer her up. Soon she's sleeping again, though she seems more content. She's less fevered, for sure."
            "(Cool her with it)":
                add data.score 1
                "You hold the can to her brow."
                "Pearls of sweat are clinging to her face. The can fogs up after a few moments where it touches her."
                "Her fever seems to gradually subside as you stay by her. You do your best not to look at her right arm, where those stains of dark grey ink are spreading."
                talk hrn talk "Thhan... ks. Emily.."
                "She falls asleep again."
    else:
        set data.foundCan false
        "You don't find what you were hoping for... Nothing to cool her with."
    "You reach back in."
    $if this.data.hasFirstaid:
        "There it is. A plastic box."
        set data.foundbox true
        add data.score 1
        "A stamped triangle design, within it, a lung."
        "You snap it open, feeling nervous. You pick out the length of gauze, rather softer than you were expecting."
        "You can't believe you ever wanted this for your own cut..."
        "Antiseptic, this tube says. You unscrew it, and squirt some onto your finger. Then you gingerly start massaging it onto Hornet's dark stump, trying not to look."
        "There's not enough for the leg, too. But the arm is closer to the heart, you think."
        "You do your best to wrap it up. The gauze seems to cling to her skin by itself."
        "Hornet doesn't stir from her sleep, but she looks a little tidier, at least."
    else:
        set data.foundbox false
        "No... Of course, the first aid kit was empty. You feel your chest constrict. Did you HAVE to commandeer it...?"
        "Too late now... You put your hand to her forehead."
    "There's nothing more you can do for her."
    "You step away. Outside."
    jump day4noon_outside

day4noon_outside:
    clear_dialog
    set_screen end1
    play music rainsong
    "Thoughts rush through your head. You look up at the roiling grey heavens."
    $if this.data.foundbox:
        $if this.data.foundCan:
            "At least you've managed to cool her. And bandage her up a little."
            "Maybe... Just maybe, that'll be enough..?"
        else:
            "At least you managed to bandage her up. That fever, though..?"
            talk em talk "Why'd you have to drink that soda... Stupid... Stupid rich girl..."
    else:
        $if this.data.foundCan:
            "At least you've managed to cool her."
            "But that wound..."
            talk em talk "Stupid, stupid rich girl... Needed that scratch treated so bad, did you..."
        else:
            "There was nothing you could do for her. You feel sick to your stomach."
            talk em talk "Why'd you have to drink that soda... Bandage that s-scratch... Stupid... Stupid rich girl..."
    "Tears come unbidden. They wash down your face with the rain."
    $if this.data.score >3:
        "It could be worse, you guess. Maybe there's a chance she'll be okay."
        "Better check back on her..."
        clear_dialog
        "You step back inside."
        play music hornet
        set_screen end5
        "The smell has gotten sweeter, but no less upsetting."
        "Hornet seems to be awake. You gingerly step to her side, and touch her cheek. She looks up at you."
        talk hrn talk "Emily... You came back..."
        "Her cheeks are wet. Is it sweat, or-?"
        talk hrn talk "You were gone so long, I thought..."
        talk em talk "Hush, darling. I was only out a moment. How are you feeling?"
        "She doesn't really answer. Her eyes look like marbles, set in dark, dark sockets."
        "Only then do you notice her other arm is gone, at the shoulder. You stifle a squeak of shock."
        talk hrn talk "Flowers..."
        "She looks up at you."
        talk hrn talk "Emily, there are so many of them... Are they, yours..."
        talk hrn talk "I dreamt of flowers..."
        "You realise pulmonarias have grown all around her, around her jacket and bag. A few have begun to bloom, even."
        "They smell sweet, nicer than her wounds."
        "Hornet is crying now."
        choice:
            talk hrn talk "It hurts, Emily. So much... You're so far away..."
            "'I'm right here, darling.'":
                talk em talk "I'm right here, darling."
                "You're at a loss. All you can think to do is gently caress her cheek."
                talk em talk "It'll be alright. You'll feel better soon, get some rest."
        "Hornet shakes her head, then her eyes widen."
        set_screen end6
        "Suddenly, a great stream of insects pours from her mouth. She seems startled. Black skin starts spreading along her neck."
        "The insects have a strange shine to them - they almost look like polycarbon, though they're pouring too fast to see, a great stream of them, glistening wings and carapaces, disappearing into cracks in the concrete and piping-"
        talk em talk "*Hornet!*"
        "You squeal in anguish, catching her as she falls forwards. Then you scream."
        set_screen end7b
        "In your hand is Hornet's head. It looks..."
        "Perfect."
        "It's the porcelain head of a doll, painted intricately, with delicate lips and round, shiny cheeks."
        "You stare at it."
        "Terror"
        "and misery."
        "This is your doing. Your dream. The pool."
        talk em talk "My, Hornet, what have I done to you..."
        "The hair are soft. There's no trace of marring on the neck."
        "Terrified, you don't know what to do with it. Your world is spinning."
        choice:
            talk em talk "Hornet... Hornet, what..."
            "Set it down.":
                "You place it gingerly at your side. It's... too light. To be her real head."
                talk emdrm talk "YOU KNOW WHAT COMES NEXT."
                "You make yourself look at the body."
        set_screen endGood
        "Hornet's body is split open, in a large triangular gash. There's no gore; it looks clean, and smells of flowers."
        "Flowers are in full bloom all around it. Even within it. What used to be her body is just a hollow, now, for colourful new life."
        choice:
            "You creep closer. Nestled inside is a tiny animal - a fawn, newborn. White spots dapple its back."
            "(Reach in)":
                "You reach in,"
                "and fasten a golden ribbon about its neck."
        stop music
        set_screen interl2
        clear_dialog
        " "
        "..."
        "GOOD END"
        jump outro1

    else:
        "You wonder if you could have done more for her."
        "Better check back on her..."
        clear_dialog
        "You step back inside."
        play music hornet
        set_screen end5
        "The smell has become no less upsetting."
        "Hornet seems to be awake. You gingerly step to her side, and touch her cheek. She looks up at you."
        talk hrn talk "Emily... You came back..."
        "Her cheeks are wet with sweat."
        talk hrn talk "You were gone so long, I thought..."
        talk em talk "I was only out a moment. How are you feeling?"
        "She doesn't really answer. Her eyes look like marbles, set in dark sockets."
        "Only then do you notice her other arm is gone, almost at the shoulder. Your stomach tightens."
        talk hrn talk "Flowers..."
        "She looks up at you."
        talk hrn talk "Emily, there are so many of them... Are they, yours..."
        talk hrn talk "I dreamt of flowers..."
        "You realise Pulmonarias have grown all around her, around her jacket and bag. A few have begun to bloom, even."
        "They help mask the stench of her decomposing wounds."
        "Hornet is crying now."
        choice:
            talk hrn talk "It hurts, Emily. So much... You're so far away..."
            "'I'm right here, Hornet.'":
                talk em talk "I'm right here, Hornet."
                "You're at a loss, but gingerly touch her cheek."
                talk em talk "It'll be alright. You'll feel better soon, get some rest."
        "Hornet shakes her head, then her eyes widen."
        set_screen end6
        "Suddenly, a great stream of insects pours from her mouth. She seems startled. Black patches spread along her neck."
        "The insects have a strange shine to them - they almost look like polycarbon, though they're pouring too fast to see, a great stream of them, glistening wings and carapaces, disappearing into cracks in the concrete and piping-"
        talk em talk "*Hornet!*"
        "You squeal in anguish, catching her as she falls forwards. Then you scream."
        set_screen end7a
        "In your hand is Hornet's head. It looks..."
        "Fake. It's the plastic head of a toy, painted poorly, with a great helmet of 'hair'."
        "You stare at it in disgust and horror. Your dream... The pool..."
        "Blank, flat eyes stare at nothing."
        talk em talk "Hornet, what happened to you..."
        "A seam runs up the side of the head."
        "Terrified, you don't know what to do with it. Your world is spinning."
        choice:
            talk em talk "Hornet... Hornet, what..."
            "Set it down.":
                "You place it gingerly at your side. It's... too light, somehow, to be her real head."
                talk emdrm talk "YOU KNOW WHAT COMES NEXT."
                "You make yourself look at her body."
        set_screen endMid
        "Hornet's body is split open, in a large triangular gash. There's no gore, really; it looks clean, and smells of flowers."
        "Flowers are in full bloom all around it. Even within it. What used to be her body is just a hollow, now, for new life."
        "You creep closer. There is nothing inside."
        "Only an array of purple and blue and magenta blossoms."
        "One of the flowers, a mutation, seems to glitter, golden."
        stop music
        set_screen interl2
        clear_dialog
        " "
        "..."
        "NEUTRAL END"
        jump outro1

day4_endBad:
    set_screen end1
    play music rainsong
    "You can't do this anymore."
    "You realise that as you stare outside into the rain."
    "You need to go back. You're Emily. You have a home. You don't need this rat or her grand ideas, or her constant holier-than-though proselityzing. Just because you're not from the machining district..."
    "She doesn't even know where FRUIT comes from. You feel churning in your stomach."
    "Then..."
    set_screen endBad
    talk emdrm talk "WHY ARE YOU STILL STANDING HERE?"
    choice:
        talk emdrm talk "RUN."
        "(Run)":
            "You run."
            "Hornet does not follow you."
            stop music
            set_screen interl2
            clear_dialog
            " "
            "BAD END"
            jump outro1
    