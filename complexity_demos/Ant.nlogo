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

patches-own [  ;; patches as land, we offer two new properties for each piece of land: pheromone (value) or food (amount)
  pheromone            ;; amount of pheromone on this patch of land
  food                 ;; amount of food on this patch of land (0, 1, or 2),

]

turtles-own [  ;; turtles as ants, we offer one new property for all ants : carry-food? (true or false)

  carrying-food?  ;; a boolean variable

]

globals [ count-a-pile  ;; count the original number of food in one pile of food

          max-pheromone ;; maximum number of pheromone

          stop-switch ;; switch off once finished

          finish-time  ;; when food and pheromone finished


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

  set finish-time 10000000  ;; set default time for auto stop

  set stop-switch true  ;; set switch true for user specified time to stop

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


                                                              ;; 6. how to make model stop automatically ( auto stop and tick stop )

                                                                     ;; auto stop: when both food and pheromone gone and another 100 ticks later

  ;; if food is gone, if pherome is gone, and if stop-switch = true, then track the finish-time and put off stop-switch
  if sum [ food ] of patches = 0 [ if sum [ pheromone ] of patches = 0 and stop-switch = true  [ set finish-time ticks set stop-switch false ] ]
  if ticks > finish-time + 100  [ stop ]   ;; after both food and pheromone is gone, let model run 100 ticks, then stop the simulation

                                                                     ;; tick stop: stop model at specified ticks
  if stop-by-ticks-switch = true and ticks = user-ticks [ stop ]

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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Thinking process ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

to Ant-model-ABM
;  How to understand ABM in terms of Ant colony model?
;
;  1. we code up single ant behavior rules into the ant model
;
;  2. the ant model can simulate ant colony dynamics

end

to simple-ant-behavior
;  What are the simple ant behavior rules we are trying to code up?
;
;  1. wander: how ants walk
;  2. look-for-food: use pheromone to sniff food direction, and if sniff pheromone then wander towards food direction
;  3. move-towards-nest: when found food, turn back, leaving pheromone, wander towards home
;  4. pheromone behaivor: it can evaporate and diffuse with some rate

;  Let's see the behavior in the simulation

end

to ant-colony-dynamics
;  What is ant colony dynamics? or the complex pattern in general (using ant colony dynamics as example to explain)?

;  how to understand complex patterns:
;  the effects of the whole is greater than the sum effect of individuals,
;  pattern are real world patterns that are not easily foreseeable,
;  and are too difficult to perceive in codes

;  Examples
;  Eg 1: food gathering ability of ant colony as a whole (100 ants) is greater than individual ant's ability multiplied 100 times
;  Eg 2: for food piles with equal distance and amount:
;  - we intuitively hypothesize ants will take them at the same time approximately, but it is not true in reality
;  - In reality, biologist observed that any colony will finish one pile after another even they have same amount and distance.


end

to design-detailed-ant-behavior
;  how to design or code up each behavior rule of ant
;  1. get as much detailed behavior descriptions from biologists as possible
;  2. make sensible and reasonable assumptions for the remaining and necessary details for coding
;  3. we will deal with the details of ant behaviors in the coding section/videos
;
end

to validate-model
;  How do we know our model is valid or practically useful in simulating the real ant colony dynamics?
;  it validates if -
;  1. our model should generate complex patterns
;  2. the patterns are similar to those in real world
;
;  examples:
;  1. the whole is greater than the sum of individuals in terms of food gathering efficiency
;  2. how ant colony (model) react to food piles of same distance and amount.
;  3. ants move in large trails when they found and transport food between food source and nest
;
;  when new complex patterns observed by biologist, our model's parameters need to update to reproduce the new
;  1. we can experiment the effects of different parameters
;  2. search for the more appropriate parameters values of the model to reproduce all complex patterns old and new
;  3. in the process we can code up measures to count the appearances of old and new complex patterns


end

to code-initial-states

;  build a nest,
;  build many ants at nest,
;  build 3 piles of food scatters located with different distance

end

to code-behavior-search-wonder-randomly

;  sniff around its 8 neighboring places for pheromone
;
;  if sniff no pheromone around [
;
;            randomly turn its directions and move forward at certain speed
;  ]

end


to code-behavior-follow-pheromone-towards-food

;  sniff around its 8 neighboring places for pheromone
;
;  if sniff pheromone around [
;
;            compare which neighbor has the highest pheromone
;
;            move to that neighbor's position
;
;  ]
;
;  sniff around its 8 neighboring places for food
;
;  if sniff food around [
;
;            take food (change its color)
;
;             code-behavior-foodhome-leave-pheromone
;  ]

end

to code-behavior-foodhome-leave-pheromone


;      going back to nest (but how? randomly wonder to home? follow pheromone? )
;
;      leaving pheromone at each step = change pheromone's value for the patch where the ant stand
;
;      make sure the value weaker and weaker at each step = pheromone's value is decreasing at each step

end

; Copyright 1997 Uri Wilensky.
; See Info tab for full copyright and license.
