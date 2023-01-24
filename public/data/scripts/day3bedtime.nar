day3bedtime:
    clear_dialog
    set_screen river4
    "A structure swims out of the distance."
    "You approach it bit by bit, and it grows, grows larger and larger, the first building you've seen since Peele Station."
    "A queer feeling."
    "It's cheap concrete, eaten away at the base by the river, covered in the everpresent dust and lichen."
    "There are great winches and the remains of steel cranes. Cables and chains trail off into the river."
    "As you get closer, a dark spot coalesces into a large gash at one side, surrounded by rubble... It must be as old as this road. Perhaps the path used to be a service trail."
    "Though this place hasn't been serviced - or even visited - in a long time, you guess."
    talk hrn talk "That looks like it'll do..."
    "She looks up at the sky."
    talk hrn talk "It's gonna be light for a bit longer, but I don't think we'll find anything like this again. Let's check it out."
    "You nod, and the two of you clamber closer."
    "There are videocameras, but they've been gutted, shreds of magnetic tape hanging from their insides, the fronts looking dark and hollow without the lenses. In a way, they look like ancient carrion."
    "There was livery painted on this building a long time ago, but that time has scratched it off again, bleached it and painted over it a dozen times over, and only traces of letters remain visible, straighter than the other stains."
    "The hole is too dark to see clearly. You crouch down carefully, and step inside..."
    set_screen river5
    "Inside the building you're greeted with slightly damp air. It's not as dusty as outside, and green moss plays on the ground and walls. Rebar and piping fill the space, but its impossible to tell what this used to be... A garage, perhaps?"
    "Much of it is rusted to pieces. A crack in the wall happens to let in a deal of light, seeming much brighter in the gloom than it does outside."
    "There's graffiti on the wall, old too, but still legible. Two indistinct people crouch looking at each other. Above them, an inscription reads-"
    "'AL L THIS LOVE/"
    "ON DUST CHOKED'"
    "You glance at Hornet, but she doesn't say anything. She's busy inspecting the room."
    talk hrn talk "Doesn't look too bad. Should shelter us from the weather at least..."
    "Her boot taps the ground."
    talk hrn talk "This is asphalt, so it shouldn't collapse on us."
    "She takes a few tentative steps inside."
    talk hrn talk "Let's make dinner. We can spend the evening here."
    "You do."
    "Neither of you are very hungry, so you eat more of the bread. It's running low... Hopefully you'll find something to eat soon, you think."
    if (> $data.tensionPoints 4):
        "There's food back in the City..."
        "You try to forget the thought."
    "You make your makeshift bed and open the book you brought."
    if (> $data.tensionPoints 1):
        "Not a single word stays in your head, however. You're keyed up, distracted."
        "You start thinking about throwing the book in the river."
    else:
        "It's a modern romance novel, about a rat who falls in love with a white fox in a church."
        "It's calming."
    "Hornet heads outside to climb the building."
    if (< $data.tensionPoints 3):
        talk em talk "Be careful!"
        talk hrn talk "Of course I will!"
        "She gives you a wry smile as she ducks out."
    else:
        "You acknowledge her with a little grunt."
    "She returns when it starts getting darker and the wind picks up."
    talk hrn talk "Well, the road keeps going on a while. I think there's a bridge in the distance, though I can't be sure."
    "She opens her bag to get a drink of water."
    talk hrn talk "Ruined tower to the north-east, over the treetops. I don't think it's anything to be worried about."
    "Nor something to head for, by her tone."
    talk hrn talk "Dark clouds coming our way. Let's hope this place is as good a shelter as it seemed."
    if (> $data.score 2):
        set_screen river6a
        set data.sleepstatus 1
        "Hornet lies down by your side, and you stroke her palm for a while. The light fades."
        "You don't need words now."
        if (== $data.LOVE 0):
            "You realise you love her. Does she love you too? She's right next to you, you can feel her chest rise and fall..."
            set this.data.LOVE 2
            "The question chases itself around your mind."
        "It's nice, having her there. There's a comfortable stillness that falls over you, and her soft breathing makes you sleepy..."
        jump opener3
    else:
        if (> $data.tensionPoints 4):
            set_screen river6c
            set datasleepstatus 3
            talk em talk "Hmh."
            "Hornet doesn't say another word. Neither do you."
            "You hear a gentle thump, and glance over; she's dropped her bag and is lying down."
            "You lean back too, staring up at the stained ceiling for a long time, even as the light fades."
            "Hornet seems to fall asleep eventually. You don't really know how long it is until you do."
            jump opener3
        else:
            set_screen river6b
            set data.sleepstatus 2
            "Hornet drops her bag on the floor near you, and lies down."
            "You make some idle conversation about the tower she saw, then say goodnight to each other."
            "Hornet seems to fall asleep before long, but you lie awake for a while, gazing at the ceiling."
            "Sleep comes."
            jump opener3