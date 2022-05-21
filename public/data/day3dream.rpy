day3dream:
    clear_dialog
    set_screen blank
    play music empty
    "..."
    "..."
    "..."
    "It's not your legs that hurt now."
    "Your back is cramped from the hard floor, your neck from the pillow."
    $if this.data.sleepstatus == 1:
        "There's a warm creature clinging to you, breathing softly."
    else:
        "It's cold. So cold. You feel abandoned."
    "All feeling dissolves"
    "and then"
    stop music
    set_screen hollow1
    play music treedream
    "You're back."
    "It's spring. The hollow is bathed in bright, colourful light... Coming from all around, somehow, but most of all from within."
    talk pa talk "This is what angels look like. The sun is always shining on them, like they swallowed a piece of it, and all light loves them for it."
    "The colours play along the hollow. Flow over the bark, through it even."
    "Flowers all around... Pulmonaria, in twin magenta and blue. You've never seen so much colour."
    "Hornet is here too, somewhere. In some way."
    "If you were to linger here... Even only a minute or two... You'd hear her. You'd hear her voice crying out for you."
    "Crying your name."
    $if this.data.LOVE == 0:
        "The thought makes you so scared."
    $if this.data.LOVE == 1:
        "The thought makes you desperate. Hornet..."
    $if this.data.LOVE == 2:
        "The thought fills you with longing. Why is she so far away?"
        $if this.data.sleepstatus == 1:
            "But wasn't she right there? Her hand was on your tummy..."
    "The trees all around are creaking. There must be wind in the crowns, but dawn hasn't come yet. It won't for a long while. So the wind won't reach you down here."
    talk pa talk "It's safe at night."
    choice:
        talk pa talk "Safe to climb inside the deepest burrows."
        "Do I want to be in this one?":
            talk pa talk "Of course you do. Try it."
            talk poet talk"No sour wine for you this time. And better fare than that tea parlour serves, for sure."
            choice:
                talk poet talk "Hornet is waiting for you inside."
                "(Climb into the hollow)":
                    "You seem to glide into it-"

    set_screen hollow2
    "It is so bright."
    "You can barely see."
    choice:
        "You can feel yourself becoming blind. Feel your face turning into light. Feel your soul becoming"
        "a bonfire.":
            "Yes. A bonfire."
        "smaller.":
            "Yes. smaller."
        "a hammer.":
            "Yes. A tool."
        "a nest.":
            "Yes. A nest."
        "a river.":
            "Yes. A river."
    "As your eyes adjust, you see many pools of clear water, feeding each other. They sparkle in the light."
    "You see your own face in some of them. Bright white and gold, a shooting star. Your hair looks good short."
    "You look good with freckles, even if they are only specks of dust."
    "You look at your hands. The nail polish is blue."
    "The cut on your hand is gone now. So is hornet's coat. You still feel you might hear her if you linger, but it doesn't seem as important now. Not now that you've become someone else."
    "You feel yourself becoming a new person. You're inside the old Emily now. A cocoon. Emily didn't know half of what you do."
    talk poet talk "Emily is dead. Long live Emily."
    "A great terror takes hold, then subsides, like a wave."
    choice:
        "Say it with me, both of you. This is it."
        "'This is it.'":
            talk emdrm talk "THIS IS IT."
            choice:
                "The Power and the Glory."
                "'The Power and the Glory.'":
                    talk emdrm talk "THE POWER AND THE GLORY."
                    "She's very close now."
                    "Have you already heard her?"
    choice:
        talk poet talk "There she is."
        "Reach out for her":
            "You reach into the largest pool"
    set_screen hollow3
    "Your hand slips into the water. It is pleasantly cool."
    "Ripples run through. Your fingers find nothing at first, but then the light shifts. Inside, you see hornet's face - not reflection but refraction, a crystal structure."
    "She's beautiful. You've never seen her so happy."
    "About her neck is a golden ribbon, pure light, clearly a gift."
    "She's so *happy,* Emily. Yours forever."
    "She won't ever hurt you. Won't ever turn her face from you, leave your side..."
    "No biting teeth... A gentle creature, feeding from your hand..."
    $if this.data.LOVE == 0:
        "It's all you need to make this pain right again. One handful. Your throat feels dry enough..."
    $if this.data.LOVE == 1:
        "Her kiss was so lovely... There will be a thousand more, and she will never feel pain..."
    $if this.data.LOVE == 2:
        "You didn't tell her you loved her earlier. This, however, will speak louder than a thousand words."
    choice:
        "Do it."
        "Raise the water...":
            "Emily leans in"
    stop music
    set_screen blank
    "and drinks from the pool."
    "The water is so cold."
    "The dream fades, and deep sleep takes its place."
    jump day4morning