;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Original Code provided by Uri Wilensky;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Wilensky, U. (1997). NetLogo Turtles Circling Simple model. 
;; http://ccl.northwestern.edu/netlogo/models/TurtlesCirclingSimple. 
;; Center for Connected Learning and Computer-Based Modeling, Northwestern Institute on Complex Systems, Northwestern University, Evanston, IL.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;further modified and heavily commented by 深度碎片;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Chinese videos see https://www.bilibili.com/video/av31450231/ p01-03
turtles-own [speed]  ;; make a property for all turtles



to setup  ;; to setup the universe

  setup-circle  ;; setup a circle to begin with

  reset-ticks  ;; put clock back to 0

end

to setup-circle  ;; how to setup a cicle at the beginning

  clear-all  ;; wipe out the whole universe

  set-default-shape turtles "arrow"  ;; give each turtle a default shape of "arrow", even though no turtles created at this moment

  ;; all turtles are born at the same original spot
  create-ordered-turtles 40 [  ;; create 40 turtles, ordered: they are evenly spaced around the circle
;  create-turtles 40 [  ;; create 40 turtles, but not evenly spaced

    set size 2  ;; (easier to see) set the size of each turtle

    set speed .35  ;; (this is the size of each step the turtles take in a tick) set the speed of all turtles


    fd 20  ;; turtles move forward 20 to form the perimeter of circle

    rt 90  ;; turtles turn right for 90 degree to face tangent to the circle

  ]
end

to go  ;; how each turtle behave in iteration

  ;; all turtles indepedently behave in the same way forward the same amount and turn right the same 1 degree
  ask turtles [set speed velocity fd speed rt degree ]  ;; there is no interaction between turtles
;  set speed velocity

  ;; track a single turtle: enlarge it and make it pen-down
  if track-turtle? [ ask one-of turtles [set size 4 pen-down]

                     set track-turtle? false]  ;; make sure tracking turtle does not iterate

  tick  ;; count the number of iterations

end




;; build a button function: occur once when click it
to change-speed  ;; reset the speed of turtles by increasing 0.15, such function take place when user click a button (not included in iteration function 'go'

;  ask turtles [set speed speed + .15]   ;; increase the step-size to .5

end


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Thinking process ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


to problem

;  only design individual turtle's simple action (move forward or backward, turn right or left)
;
;  produce visually surprising emergence phenomena of all turtles as a whole

end

to initial-setting

;  put 40 turtles with even spaced onto a circle

;  each turtle locate at the point where tangent line through (move same distance, turn right the same degree)

;  we can see setup and go in slow motion

end


to behavior-design

;  each turtle move forward at certain but same speed and turn right at certain but same degree (very easy behavior)
;
;  do turtles interact with each other or act independently? (Independently, easy)

end

to emergence-from-iteration

;  are emergence phenonema surprising to us? (at initial setting )

;  any emergence phenonema if we change turtle's moving speed or direction?

;  see automation of experiment

end


; Copyright 1997 Uri Wilensky.
; See Info tab for full copyright and license.
