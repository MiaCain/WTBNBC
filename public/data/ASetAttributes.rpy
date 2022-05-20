ASetAt_Tension_High:
    set_screen error
    set data.tensionPoints 10
    set data.OR.cityfeeling 3
    talk pa talk "Tension set to 10"

ASetAt_Tension_Low:
    set_screen error
    set data.tensionPoints 0
    set data.OR.cityfeeling 1
    talk pa talk "Tension set to 0"

ASetAt_Score_High:
    set_screen error
    set data.score 10
    talk pa talk "score set to 10 : ) winner winner chicken dinner!"

ASetAt_Score_Low:
    set_screen error
    set data.score 0
    talk pa talk "score set to 0. go fuck yourself loser"
 