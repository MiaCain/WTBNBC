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
    #BAD DREAM


day2dream_worse:
    #WORSE DREAM