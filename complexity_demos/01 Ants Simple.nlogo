;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Original Code provided by Uri Wilensky;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Wilensky, U. (1997). NetLogo Ants Simple model. http://ccl.northwestern.edu/netlogo/models/AntsSimple.
;; Center for Connected Learning and Computer-Based Modeling, Northwestern Institute on Complex Systems, Northwestern University, Evanston, IL.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;further modified and heavily commented by 深度碎片;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; links to Chinese and English videos can be found from https://github.com/EmbraceLife/shendusuipian/issues/50


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; problem ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  When an ant finds a piece of food, it carries the food back to the nest, dropping a chemical as it moves.
;  When other ants “sniff” the chemical, they follow the chemical toward the food.
;  As more ants carry food to the nest, they reinforce the chemical trail.


;; define patch properties  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
patches-own [  ;; patches as land, has 2 properties
  pheromone            ;; amount of pheromone
  food                 ;; amount of food

]

turtles-own [  ;; turle or ant has one property

  carrying-food?  ;; true or false

]

globals [ count-a-pile  ;; count the original number of food in one pile of food

          max-pheromone ;; maximum number of pheromone at any piece of land

          finish-time  ;; a constant to make model stop at a long time later

          ]



;; How to experiment on properties and globals
;; clear-all, create-turtles 1 [set size 5 set color green ]
;; ask one-of patches [ set psize 5 set pcolor blue ]


;;;;;;;;;;;;;;;;;;;;;;;;
;;; Setup procedures ;;;
;;;;;;;;;;;;;;;;;;;;;;;;

to setup  ;; setup the world

  clear-all  ;; wipe out the world first

  set-default-shape turtles "bug"  ;; make all turtles' shape to be "bug"

  setup-patches  ;; setup the world for ants

  set finish-time 1000000 ;; a constant to make model stop at a long time latera constant to make model stop at a long time later

  reset-ticks  ;; put clock back to 0

end


;;;;;;;;;;;;;;;;;;;;;
;;; Go procedures ;;;
;;;;;;;;;;;;;;;;;;;;;

to go  ;; make iterations

  if count turtles < population [ create-ant ]  ;; 1. create as much as ants as you want

  ask turtles [                                 ;; 2. ask each and every ant to

    move                                                ;; perform ant's simple actions

    recolor                                             ;; differentiate ants for carrying-food or not with color

  ]

  diffuse pheromone (diffusion-rate / 100)                    ;; 3. define how pheromone diffuse itself

  ask patches [                                               ;; 4. define how pheromone evaporate itself

    set pheromone pheromone * (100 - evaporation-rate) / 100        ;; decreasing by evaporation-rate
    if pheromone < 0.05 [ set pheromone 0 ]                         ;; if < 0.05, disappear
  ]

  recolor-patches                                             ;; 5. paint patches of pheromone with scale-color


  set max-pheromone max [ pheromone ] of patches ;; find out the max pheromone on any patch in the world  (stats)



  ;; if food is gone, if pherome is gone, and if stop-switch = true, then track the finish-time and put off stop-switch
  if sum [ food ] of patches = 0 and sum [ pheromone ] of patches = 0 and auto-stop?  [

      set finish-time ticks

      set auto-stop? false ]  ;; to make sure it only happen once

  if ticks > finish-time + 100  [ stop ]   ;; after both food and pheromone is gone, let model run 100 ticks, then stop the simulation

                                                                     ;; tick stop: stop model at specified ticks
  if stop-ticks? and ticks = user-ticks [ stop ]

  tick  ;; update the iteration clock or ticks, without it we can't see updating in graphics


end


;; for experiment ;;;;;;;;;;;;;;;;;;;
to setup-behavior  ;; setup the world for other experiment

  clear-all  ;; wipe out the world first

  set-default-shape turtles "bug"  ;; make all turtles' shape to be "bug"

  setup-patches  ;; setup the world for ants

  setup-large-food ;; overwrite to create large food area

  reset-ticks  ;; put clock back to 0

end

to setup-large-food  ;; paint 3 food areas

  ;; setup a food source on the right to the center
  ask patch (0.6 * max-pxcor) (0.6 * max-pycor) [  ;; find a patch of land at (0.6 x 35, 0.6 x 35) coordinates; make it same distance to second food pile

    make-food-source 20 cyan  ;; paint this patch surround area with cyan
  ]
  ;; setup a food source on the lower-left
  ask patch (-0.6 * max-pxcor) (-0.6 * max-pycor) [  ;; find a patch of land at (-0.6 x 35, -0.6 x 35), try observer: show max-pxcor

    make-food-source 20 sky  ;; paint this patch surrounding area with sky color
  ]
  ;; setup a food source on the upper-left
  ask patch (-0.8 * max-pxcor) (0.8 * max-pycor) [  ;; find a patch of land at (-0.8 x 35, 0.8 x 35), try observer: show max-pxcor

    make-food-source 20 blue  ;; paint this patch surround area with blue
  ]
  ;; setup a food source on the lower-left
  ask patch (0.8 * max-pxcor) (-0.8 * max-pycor) [  ;; find a patch of land at (-0.8 x 35, 0.8 x 35), try observer: show max-pxcor

    make-food-source 20 gray  ;; paint this patch surround area with blue
  ]



end
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


to setup-patches  ;; setup the world for ants

  setup-nest   ;; build nest for ants

  setup-food  ;; build food piles for ants

  recolor-patches  ;; paint non-food, non-nest area, paint the pheromone to form trail

end

to setup-nest  ;; paint nest with violet color

  ask patches with [ nest? ] [  ;; ask all patches whose nest? is true

    set pcolor violet  ;; set this patch of land to violet color
  ]
end

to setup-food  ;; paint 3 food areas

  ;; setup a food source on the right to the center
  ask patch (0.6 * max-pxcor) (0.6 * max-pycor) [  ;; find a patch of land at (0.6 x 35, 0.6 x 35) coordinates; make it same distance to second food pile

    make-food-source 5 cyan  ;; paint this patch surround area with cyan
  ]
  ;; setup a food source on the lower-left
  ask patch (-0.6 * max-pxcor) (-0.6 * max-pycor) [  ;; find a patch of land at (-0.6 x 35, -0.6 x 35), try observer: show max-pxcor

    make-food-source 5 sky  ;; paint this patch surrounding area with sky color
  ]
  ;; setup a food source on the upper-left
  ask patch (-0.8 * max-pxcor) (0.8 * max-pycor) [  ;; find a patch of land at (-0.8 x 35, 0.8 x 35), try observer: show max-pxcor

    make-food-source 5 blue  ;; paint this patch surround area with blue
  ]

end

to make-food-source [ food-area food-source-color ] ;; build a food pile based on the given patch and paint it with specified color
                                          ;; by the way, this is a function with a user input

  ask patches with [ distance myself < food-area ] [  ;; based on current patch, ask its surrounding neighbor patches within radius 5 unit distance

    set food 2  ;; set the patches' food property to be 2

    set pcolor food-source-color  ;; set the patches' color to be specified color
  ]

  set count-a-pile count patches with [ distance myself < food-area ]  ;; count the number of patches forming a pile of food

end

to recolor-patches  ;; paint pheromones or trails of the patches of land which have food nor nest

  ask patches with [ food = 0 and not nest? ] [  ;; ask all patches which have neither food nor nest

    set pcolor scale-color green pheromone 0.1 5  ;; paint patches with scale-color on green depend on pheromone level (low value 0.1 = dark-green, high value 5 = light-green)


  ]
end



to move  ;; 'move' contains all major ant behaviors


  if not carrying-food? [ look-for-food ]   ;; 1. look for food, if not carrying food


  if carrying-food? [ move-towards-nest ]   ;; 2. move towards nest, if carrying food

  wander                                    ;; 3. both actions require ant to wander


                                            ;; 4. make the pen-down ant to draw its trail and action state

                                                  ;; 4.1 paint for look-for-food and wander

  ask turtles with [pen-mode = "down"] [   ;; ask the turtle with pen down

                                          if not carrying-food? [ set label "look-for-food and wander"   ;; if the turtle does not carry food, label it with "look-for-food"
                                                                  set label-color blue        ;; and give blue as label color
                                                                  set color blue         ;; paint the ant blue with its pen
    ]
  ]


                                                  ;; 4.2 paint for move-towards-nest and wander

  ask turtles with [pen-mode = "down"] [   ;; ask the turtle with pen down

                                           if carrying-food? [set label "move-towards-nest and wander"   ;; if the ant carries food, label ant with "move-towards-nest"
                                                              set label-color yellow          ;; and give yellow as label color
                                                              set color yellow               ;; paint the ant yellow with its pen
    ]
  ]
                                                  ;; 4.3 paint for found food

  ask turtles with [pen-mode = "down"] [   ;; ask the turtle with pen down,

                                           if food > 0 [set label "Food, Food!"   ;; if the ant found food, label ant with "Food, Food !"
                                                        set label-color magenta          ;; and give yellow as label color
                                                        set color magenta               ;; paint the ant yellow with its pen
    ]
  ]

end

to create-ant  ;; create an ant

  create-turtles 1 [  ;; create a turtle

    set size 2  ;; make it big so easier to see

    set carrying-food? false  ;; set ant property as not carrying food mode

;    ;; testify this function
;    fd random 10  ;; fd a random number between 1 and 10
;    set label who  ;; Note the number of ants created

  ]
end

to move-towards-nest  ;; How ants move back to nest

  ifelse nest? [  ;; under ask turtles mode, check each ant's `nest?` true or false

    set carrying-food? false  ;; if at nest, drop food (set property 'carrying-food' to be false)

    rt 180  ;; and head out again is turn 180 degree

  ] [
    set pheromone pheromone + 60  ;; if not at nest yet, increase the current patch's pheromone by 60 in value, leaving pheromone for tracking

    facexy 0 0  ;; turn towards the nest, which is at the center
  ]
end

to look-for-food  ;; How ants look for food

  ifelse food > 0 [  ;; under ask turtles mode, we can access current turtle/ant's patch and its properties
                     ;; if current patch's food is more than 0, meaning we found food on this patch/location

    set carrying-food? true  ;; pick up food, set current turtle's carrying-food property to be true

    set food food - 1        ;; reduce current patch's food property by value 1

    rt 180                   ;; make the current ant turn around by 180 to the right


  ] [
    uphill-pheromone  ;; if no food at this patch, this ant go face towards the direction where the pheromone smell is strongest
  ]
end

to uphill-pheromone  ;; sniff left and right, and face towards where the strongest smell is

  if pheromone < pheromone-sensitivity [  ;; if current patch's pheromone is less than 2 (very weak);; what if uplift the upper limit from 2 too 200

    let scent-ahead pheromone-scent-at-angle   0  ;; assign the current heading direction-next patch's pheromone to local variable 'scent-ahead'

    let scent-right pheromone-scent-at-angle  45  ;; assign local variable 'scent-right' with the pheromone value of the patch
                                                  ;; which is 1 patch away with direction of current heading turn right 45 degree

    let scent-left  pheromone-scent-at-angle -45  ;; assign local variable 'scent-left' with the pheromone value of the patch
                                                  ;; which is 1 patch away with direction of current heading turn left 45 degree

    ;; ant only look for stronger pheromone in the area ahead of itself with 90 degree variation

    if (scent-right > scent-ahead) or (scent-left > scent-ahead) [  ;; if pheromone on the right is more than that ahead or that on the left is more than that ahead

      ifelse scent-right > scent-left  ;; and if pheromone on the right is more than that on the left

        [ rt 45 ]  ;; turn right 45 degree

        [ lt 45 ]  ;; otherwise, turn left 45 degree
    ]

;;    this is for test-look-for-food only
;    type "left " print precision scent-left 2
;    type "ahead " print precision scent-ahead 2
;    type "right " print precision scent-right 2


  ]
end


;; for experiment ;;;;;;;;;;;;;;;;;;;
to test-look-for-food  ;; This is for verify function look-for-food and uphill-pheromone

  ask patches with [ pxcor > 0 and pxcor < 30 and pycor < -10 and pycor > -30 ] [ set pheromone pxcor / 15 set pcolor scale-color green pheromone 0 2]
  create-turtles 1 [ set size 5 set color sky set xcor 0 set ycor -20 set heading 90]
  ask patches with [ pxcor = 5 and pycor = -20 ] [ set pheromone pheromone - 1 set pcolor blue]
  ask patches with [ pxcor = 6 and pycor = -19 ] [ set pheromone pheromone - 1 set pcolor red]


end

to go-test-look-for-food  ;; This is for verify function look-for-food and uphill-pheromone

  ask turtles [ look-for-food fd 1]


end
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


to wander  ;; make ant wander around

  rt random 40  ;; turn right randomly with maximum value at 40 degrees

  lt random 40  ;; turn left  randomly with maximum value at 40 degrees

  ;; given ant can sniff where the stronger pheromone is, wonder makes the ant direction vary from -40 to 40 degree (user defined variation)

  if not can-move? 1 [ rt 180 ]  ;; if ant can not move ahead by 1 unit distance, then turn right 180 degrees

  fd 1  ;; move forward by 1 unit distance

end

to recolor  ;; use color differentiate ants for carrying-food or not

  ifelse carrying-food?  ;; if the current ant has food on it

    [ set color orange + 1 ]  ;; set its color to be orange + 1

    [ set color red ]  ;; otherwise make it color red

end

to-report pheromone-scent-at-angle [ angle ]  ;; report the value of pheromone of a patch on certain direction and distance

  let p patch-right-and-ahead angle 1  ;; create a local variable p, assign a patch to it, such patch is about `angle` to the right and 1 patch distance away

  if p = nobody [ report 0 ]  ;; if this patch does not exist, report value 0

  report [ pheromone ] of p  ;; if this patch exist, report this patch's pheromone value

end

to-report nest?   ;; report a property like value for all patches or turtles
                  ;; if the distance between the turtle and (0,0) is smaller than 5, report true; otherwise false
                  ;; if the distance between the standing ant and (0,0) is smaller than 5, report true; otherwise false
  report distancexy 0 0 < 5
end



; Copyright 1997 Uri Wilensky.
; See Info tab for full copyright and license.
@#$#@#$#@
GRAPHICS-WINDOW
370
10
875
516
-1
-1
7.0
1
20
1
1
1
0
0
0
1
-35
35
-35
35
1
1
1
ticks
30.0

BUTTON
90
55
170
88
NIL
setup
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

SLIDER
85
90
275
123
diffusion-rate
diffusion-rate
0.0
99.0
74.0
1.0
1
NIL
HORIZONTAL

SLIDER
85
125
275
158
evaporation-rate
evaporation-rate
0.0
99.0
5.0
1.0
1
NIL
HORIZONTAL

BUTTON
190
55
265
88
NIL
go
T
1
T
OBSERVER
NIL
NIL
NIL
NIL
0

SLIDER
85
20
275
53
population
population
0.0
200.0
198.0
1.0
1
NIL
HORIZONTAL

PLOT
20
280
370
515
Remaining Food
Time
Food
0.0
1000.0
0.0
1.0
true
true
"" ""
PENS
"lower-left" 1.0 0 -5298144 true "" "plot sum [ food ] of patches with [ pcolor = sky ] "
"upper-left" 1.0 0 -13345367 true "" "plot sum [ food ] of patches with [ pcolor = blue ] "
"right" 1.0 0 -13840069 true "" "plot sum [ food ] of patches with [ pcolor = cyan ] "
"total" 1.0 0 -16777216 true "" "plot sum [ food ] of patches "

BUTTON
880
10
987
43
follow an ant
ask one-of turtles [ set shape \"arrow\" set size 5 pen-down ] 
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

TEXTBOX
885
55
1240
206
1. What does Ant model do? (code individual behavior, simulate complex pattern, complex: not easily foreseeable, extreme difficult or don't know how to program)\n2. In what way ABM model is similar to ML or DL? (build a model, let model learn to do complex tasks; ML learn from data, ABM learn from multi-agents simulations)\n3. complex patterns can validate our model \na. same distance food pile, still gather one by one (pop:130, diffuse:60, evapo:5, sniff pheromone < 12)\nb. whole is greater than sum of individuals (experiment to get statistics)
11
0.0
1

MONITOR
890
460
1027
505
food gathered so far
count-a-pile * 3 * 2 - sum [ food ] of patches
17
1
11

TEXTBOX
885
230
1195
381
A. single ant, by itself, 1000 ticks, 100 simulations, average food gathered = 3.71 = multiply with 100 = 371\nB. 100 ants together, 1000 ticks, 100 simulations, average food gathered = 393\n1. diffuse=88, evaporate=6 , A:371, B: 393, diff/A = 6% (statistically?)\n2. diffuse=88, evaporate=3, A: 333, B: 390, diff/A=17%\n3. diffuse=60, evaporate=3, A: 350, B: 401, diff/A=14.6%\n
11
0.0
1

MONITOR
1040
460
1157
505
NIL
max-pheromone
17
1
11

TEXTBOX
890
380
1225
455
Further Tasks\n1. program to count or even measure complex patterns \n2. statistical analysis with experiments\n3. more plotting skills on canvas
11
0.0
1

SWITCH
30
205
165
238
stop-ticks?
stop-ticks?
1
1
-1000

SLIDER
85
240
257
273
user-ticks
user-ticks
1000
2000
1330.0
10
1
NIL
HORIZONTAL

SLIDER
85
160
277
193
pheromone-sensitivity
pheromone-sensitivity
0
100
12.0
1
1
NIL
HORIZONTAL

SWITCH
180
205
302
238
auto-stop?
auto-stop?
1
1
-1000

@#$#@#$#@
## ACKNOWLEDGMENT

This model is originated from Chapter One of the book "Introduction to Agent-Based Modeling: Modeling Natural, Social and Engineered Complex Systems with NetLogo", by Uri Wilensky & William Rand.

* Wilensky, U. & Rand, W. (2015). Introduction to Agent-Based Modeling: Modeling Natural, Social and Engineered Complex Systems with NetLogo. Cambridge, MA. MIT Press.

I have **further modified and heavily commented** the model for learning NetLogo and Complexity concepts. I have made **both Chinese and English vdieo tutorials** on how to code up this model and analyse what this model generate. You are welcome to follow the tutorials while playing the model. https://github.com/EmbraceLife/shendusuipian/issues/50

## WHAT IS IT?

In this model, a colony of ants forages for food. Though each ant follows a set of simple rules, the colony as a whole acts in a sophisticated way.

## HOW IT WORKS

When an ant finds a piece of food, it carries the food back to the nest, dropping a chemical as it moves. When other ants "sniff" the chemical, they follow the chemical toward the food. As more ants carry food to the nest, they reinforce the chemical trail.

## HOW TO USE IT

Click the SETUP button to set up the ant nest (in violet, at center) and three piles of food. Click the GO button to start the simulation. The chemical is shown in a green-to-white gradient.

The EVAPORATION-RATE slider controls the evaporation rate of the chemical. The DIFFUSION-RATE slider controls the diffusion rate of the chemical.

If you want to change the number of ants, move the POPULATION slider before pressing SETUP.

## THINGS TO NOTICE

The ant colony generally exploits the food source in order, starting with the food closest to the nest, and finishing with the food most distant from the nest. It is more difficult for the ants to form a stable trail to the more distant food, since the chemical trail has more time to evaporate and diffuse before being reinforced.

Once the colony finishes collecting the closest food, the chemical trail to that food naturally disappears, freeing up ants to help collect the other food sources. The more distant food sources require a larger "critical number" of ants to form a stable trail.

The consumption of the food is shown in a plot.  The line colors in the plot match the colors of the food piles.

## EXTENDING THE MODEL

Try different placements for the food sources. What happens if two food sources are equidistant from the nest? When that happens in the real world, ant colonies typically exploit one source then the other (not at the same time).

In this model, the ants always "know" where the nest is: when they want to go back to the nest, they just turn towards the center of the world (using `facexy 0 0`). Real ants use a variety of different approaches to find their way back to the nest. Try to implement some alternative strategies.

The ants only respond to chemical levels between 0.05 and 2.  The lower limit is used so the ants aren't infinitely sensitive.  Try removing the upper limit.  What happens?  Why?

In the `uphill-chemical` procedure, the ant "follows the gradient" of the chemical. That is, it "sniffs" in three directions, then turns in the direction where the chemical is strongest. You might want to try variants of the `uphill-chemical` procedure, changing the number and placement of "ant sniffs."

## NETLOGO FEATURES

The built-in `diffuse` primitive lets us diffuse the chemical easily without complicated code.

The primitive `patch-right-and-ahead` is used to make the ants smell in different directions without actually turning.

## RELATED MODELS

This model is a slight modification of the Ants models in the Biology section of the NetLogo models library.

## CREDITS AND REFERENCES

This model is a simplified version of:

* Wilensky, U. (1997).  NetLogo Ants model.  http://ccl.northwestern.edu/netlogo/models/Ants.  Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

## HOW TO CITE

This model is part of the textbook, “Introduction to Agent-Based Modeling: Modeling Natural, Social and Engineered Complex Systems with NetLogo.”

If you mention this model or the NetLogo software in a publication, we ask that you include the citations below.

For the model itself:

* Wilensky, U. (1997).  NetLogo Ants Simple model.  http://ccl.northwestern.edu/netlogo/models/AntsSimple.  Center for Connected Learning and Computer-Based Modeling, Northwestern Institute on Complex Systems, Northwestern University, Evanston, IL.

Please cite the NetLogo software as:

* Wilensky, U. (1999). NetLogo. http://ccl.northwestern.edu/netlogo/. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

Please cite the textbook as:

* Wilensky, U. & Rand, W. (2015). Introduction to Agent-Based Modeling: Modeling Natural, Social and Engineered Complex Systems with NetLogo. Cambridge, MA. MIT Press.

## COPYRIGHT AND LICENSE

Copyright 1997 Uri Wilensky.

![CC BY-NC-SA 3.0](http://ccl.northwestern.edu/images/creativecommons/byncsa.png)

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License.  To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.

Commercial licenses are also available. To inquire about commercial licenses, please contact Uri Wilensky at uri@northwestern.edu.

This model was created as part of the projects: PARTICIPATORY SIMULATIONS: NETWORK-BASED DESIGN FOR SYSTEMS LEARNING IN CLASSROOMS and/or INTEGRATED SIMULATION AND MODELING ENVIRONMENT. The project gratefully acknowledges the support of the National Science Foundation (REPP & ROLE programs) -- grant numbers REC #9814682 and REC-0126227.

<!-- 1997 -->
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

airplane
true
0
Polygon -7500403 true true 150 0 135 15 120 60 120 105 15 165 15 195 120 180 135 240 105 270 120 285 150 270 180 285 210 270 165 240 180 180 285 195 285 165 180 105 180 60 165 15

arrow
true
0
Polygon -7500403 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

box
false
0
Polygon -7500403 true true 150 285 285 225 285 75 150 135
Polygon -7500403 true true 150 135 15 75 150 15 285 75
Polygon -7500403 true true 15 75 15 225 150 285 150 135
Line -16777216 false 150 285 150 135
Line -16777216 false 150 135 15 75
Line -16777216 false 150 135 285 75

bug
true
0
Circle -7500403 true true 96 182 108
Circle -7500403 true true 110 127 80
Circle -7500403 true true 110 75 80
Line -7500403 true 150 100 80 30
Line -7500403 true 150 100 220 30

butterfly
true
0
Polygon -7500403 true true 150 165 209 199 225 225 225 255 195 270 165 255 150 240
Polygon -7500403 true true 150 165 89 198 75 225 75 255 105 270 135 255 150 240
Polygon -7500403 true true 139 148 100 105 55 90 25 90 10 105 10 135 25 180 40 195 85 194 139 163
Polygon -7500403 true true 162 150 200 105 245 90 275 90 290 105 290 135 275 180 260 195 215 195 162 165
Polygon -16777216 true false 150 255 135 225 120 150 135 120 150 105 165 120 180 150 165 225
Circle -16777216 true false 135 90 30
Line -16777216 false 150 105 195 60
Line -16777216 false 150 105 105 60

car
false
0
Polygon -7500403 true true 300 180 279 164 261 144 240 135 226 132 213 106 203 84 185 63 159 50 135 50 75 60 0 150 0 165 0 225 300 225 300 180
Circle -16777216 true false 180 180 90
Circle -16777216 true false 30 180 90
Polygon -16777216 true false 162 80 132 78 134 135 209 135 194 105 189 96 180 89
Circle -7500403 true true 47 195 58
Circle -7500403 true true 195 195 58

circle
false
0
Circle -7500403 true true 0 0 300

circle 2
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240

cow
false
0
Polygon -7500403 true true 200 193 197 249 179 249 177 196 166 187 140 189 93 191 78 179 72 211 49 209 48 181 37 149 25 120 25 89 45 72 103 84 179 75 198 76 252 64 272 81 293 103 285 121 255 121 242 118 224 167
Polygon -7500403 true true 73 210 86 251 62 249 48 208
Polygon -7500403 true true 25 114 16 195 9 204 23 213 25 200 39 123

cylinder
false
0
Circle -7500403 true true 0 0 300

dot
false
0
Circle -7500403 true true 90 90 120

face happy
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 255 90 239 62 213 47 191 67 179 90 203 109 218 150 225 192 218 210 203 227 181 251 194 236 217 212 240

face neutral
false
0
Circle -7500403 true true 8 7 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Rectangle -16777216 true false 60 195 240 225

face sad
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 168 90 184 62 210 47 232 67 244 90 220 109 205 150 198 192 205 210 220 227 242 251 229 236 206 212 183

fish
false
0
Polygon -1 true false 44 131 21 87 15 86 0 120 15 150 0 180 13 214 20 212 45 166
Polygon -1 true false 135 195 119 235 95 218 76 210 46 204 60 165
Polygon -1 true false 75 45 83 77 71 103 86 114 166 78 135 60
Polygon -7500403 true true 30 136 151 77 226 81 280 119 292 146 292 160 287 170 270 195 195 210 151 212 30 166
Circle -16777216 true false 215 106 30

flag
false
0
Rectangle -7500403 true true 60 15 75 300
Polygon -7500403 true true 90 150 270 90 90 30
Line -7500403 true 75 135 90 135
Line -7500403 true 75 45 90 45

flower
false
0
Polygon -10899396 true false 135 120 165 165 180 210 180 240 150 300 165 300 195 240 195 195 165 135
Circle -7500403 true true 85 132 38
Circle -7500403 true true 130 147 38
Circle -7500403 true true 192 85 38
Circle -7500403 true true 85 40 38
Circle -7500403 true true 177 40 38
Circle -7500403 true true 177 132 38
Circle -7500403 true true 70 85 38
Circle -7500403 true true 130 25 38
Circle -7500403 true true 96 51 108
Circle -16777216 true false 113 68 74
Polygon -10899396 true false 189 233 219 188 249 173 279 188 234 218
Polygon -10899396 true false 180 255 150 210 105 210 75 240 135 240

house
false
0
Rectangle -7500403 true true 45 120 255 285
Rectangle -16777216 true false 120 210 180 285
Polygon -7500403 true true 15 120 150 15 285 120
Line -16777216 false 30 120 270 120

leaf
false
0
Polygon -7500403 true true 150 210 135 195 120 210 60 210 30 195 60 180 60 165 15 135 30 120 15 105 40 104 45 90 60 90 90 105 105 120 120 120 105 60 120 60 135 30 150 15 165 30 180 60 195 60 180 120 195 120 210 105 240 90 255 90 263 104 285 105 270 120 285 135 240 165 240 180 270 195 240 210 180 210 165 195
Polygon -7500403 true true 135 195 135 240 120 255 105 255 105 285 135 285 165 240 165 195

line
true
0
Line -7500403 true 150 0 150 300

line half
true
0
Line -7500403 true 150 0 150 150

pentagon
false
0
Polygon -7500403 true true 150 15 15 120 60 285 240 285 285 120

person
false
0
Circle -7500403 true true 110 5 80
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Rectangle -7500403 true true 127 79 172 94
Polygon -7500403 true true 195 90 240 150 225 180 165 105
Polygon -7500403 true true 105 90 60 150 75 180 135 105

plant
false
0
Rectangle -7500403 true true 135 90 165 300
Polygon -7500403 true true 135 255 90 210 45 195 75 255 135 285
Polygon -7500403 true true 165 255 210 210 255 195 225 255 165 285
Polygon -7500403 true true 135 180 90 135 45 120 75 180 135 210
Polygon -7500403 true true 165 180 165 210 225 180 255 120 210 135
Polygon -7500403 true true 135 105 90 60 45 45 75 105 135 135
Polygon -7500403 true true 165 105 165 135 225 105 255 45 210 60
Polygon -7500403 true true 135 90 120 45 150 15 180 45 165 90

square
false
0
Rectangle -7500403 true true 30 30 270 270

square 2
false
0
Rectangle -7500403 true true 30 30 270 270
Rectangle -16777216 true false 60 60 240 240

star
false
0
Polygon -7500403 true true 151 1 185 108 298 108 207 175 242 282 151 216 59 282 94 175 3 108 116 108

target
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240
Circle -7500403 true true 60 60 180
Circle -16777216 true false 90 90 120
Circle -7500403 true true 120 120 60

tree
false
0
Circle -7500403 true true 118 3 94
Rectangle -6459832 true false 120 195 180 300
Circle -7500403 true true 65 21 108
Circle -7500403 true true 116 41 127
Circle -7500403 true true 45 90 120
Circle -7500403 true true 104 74 152

triangle
false
0
Polygon -7500403 true true 150 30 15 255 285 255

triangle 2
false
0
Polygon -7500403 true true 150 30 15 255 285 255
Polygon -16777216 true false 151 99 225 223 75 224

truck
false
0
Rectangle -7500403 true true 4 45 195 187
Polygon -7500403 true true 296 193 296 150 259 134 244 104 208 104 207 194
Rectangle -1 true false 195 60 195 105
Polygon -16777216 true false 238 112 252 141 219 141 218 112
Circle -16777216 true false 234 174 42
Rectangle -7500403 true true 181 185 214 194
Circle -16777216 true false 144 174 42
Circle -16777216 true false 24 174 42
Circle -7500403 false true 24 174 42
Circle -7500403 false true 144 174 42
Circle -7500403 false true 234 174 42

turtle
true
0
Polygon -10899396 true false 215 204 240 233 246 254 228 266 215 252 193 210
Polygon -10899396 true false 195 90 225 75 245 75 260 89 269 108 261 124 240 105 225 105 210 105
Polygon -10899396 true false 105 90 75 75 55 75 40 89 31 108 39 124 60 105 75 105 90 105
Polygon -10899396 true false 132 85 134 64 107 51 108 17 150 2 192 18 192 52 169 65 172 87
Polygon -10899396 true false 85 204 60 233 54 254 72 266 85 252 107 210
Polygon -7500403 true true 119 75 179 75 209 101 224 135 220 225 175 261 128 261 81 224 74 135 88 99

wheel
false
0
Circle -7500403 true true 3 3 294
Circle -16777216 true false 30 30 240
Line -7500403 true 150 285 150 15
Line -7500403 true 15 150 285 150
Circle -7500403 true true 120 120 60
Line -7500403 true 216 40 79 269
Line -7500403 true 40 84 269 221
Line -7500403 true 40 216 269 79
Line -7500403 true 84 40 221 269

x
false
0
Polygon -7500403 true true 270 75 225 30 30 225 75 270
Polygon -7500403 true true 30 75 75 30 270 225 225 270
@#$#@#$#@
NetLogo 6.0.4
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
<experiments>
  <experiment name="single-ant-1000ticks" repetitions="100" runMetricsEveryStep="true">
    <setup>setup</setup>
    <go>go</go>
    <timeLimit steps="1000"/>
    <metric>count-a-pile * 3 * 2 - sum [ food ] of patches</metric>
    <enumeratedValueSet variable="evaporation-rate">
      <value value="3"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="population">
      <value value="1"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="diffusion-rate">
      <value value="60"/>
    </enumeratedValueSet>
  </experiment>
  <experiment name="ants100together" repetitions="100" runMetricsEveryStep="true">
    <setup>setup</setup>
    <go>go</go>
    <metric>sum [ food ] of patches with [ pcolor = cyan ] / sum [ food ] of patches</metric>
    <metric>sum [ food ] of patches with [ pcolor = blue ]/ sum [ food ] of patches</metric>
    <metric>sum [ food ] of patches with [ pcolor = sky ] / sum [ food ] of patches</metric>
    <enumeratedValueSet variable="evaporation-rate">
      <value value="3"/>
      <value value="5"/>
      <value value="8"/>
      <value value="12"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="population">
      <value value="30"/>
      <value value="100"/>
      <value value="200"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="diffusion-rate">
      <value value="30"/>
      <value value="50"/>
      <value value="60"/>
      <value value="80"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="pheromone-sensitivity">
      <value value="2"/>
      <value value="5"/>
      <value value="8"/>
      <value value="12"/>
      <value value="20"/>
      <value value="30"/>
    </enumeratedValueSet>
  </experiment>
</experiments>
@#$#@#$#@
@#$#@#$#@
default
0.0
-0.2 0 0.0 1.0
0.0 1 1.0 0.0
0.2 0 0.0 1.0
link direction
true
0
Line -7500403 true 150 150 90 180
Line -7500403 true 150 150 210 180
@#$#@#$#@
1
@#$#@#$#@
