# Intro to ABM Textbook Examples 

[model repository](https://github.com/EmbraceLife/shendusuipian/tree/master/complexity_demos) 

## Turtles Circling Simple 

> [00 Turtles Circling Simple.nlogo](models/MMM/00 Turtles Circling Simple.nlogo)  
>
> **Learning objectives** 
>
> - `patches-own [ speed ]`
> - `clear-all` and `reset-ticks`  for `setup`  function 
> - `tick` for `go` function 
> - `set-default-shape turtles "arrow"` 
> - `create-ordered-turtles 40 [ set size 2 fd 5 rt 90 ]`  : evenly spaced 
> - `ask turtles [ ... ]` 
> - globals by interface widgets
>   - switch on or off : `trakc-turtle?`  
>   - slider to change values : `degree` and `velocity`

## Simple Ant model 

> [01 Ants Simple.nlogo](../MMM/01 Ants Simple.nlogo) 
>
> video [CN](https://www.youtube.com/playlist?list=PLx08F1efFq_Xvg8EXr4aqqZW5U9xuhoFX) and [EN](https://www.youtube.com/playlist?list=PLx08F1efFq_VqfiaXI_Eiifq04f5C4afe)
>
> Learning Objectives 
>
> - `to-report nest?`
> - `distancexy 0 0 < 5` 
> - `let p patch-right-and-ahead angle 1`
> - `ifelse carrying-food?[][]`
> - `if not can-move? 1 [ rt 180 ]`  
> - `lt random 40`  
> - `create-turtles 1 [ ]`
> - `ask turtles with [pen-mode = "down"]`  
> - `ask one-of turtles [ set shape "arrow" set size 5 pen-down ] `
> - `set label "yeah" set label-color "yellow" `
> - `ask patches with [ food = 0 and not nest? ] [set pcolor scale-color green pheromone 0.1 5] `
> - `set count-a-pile count patches with [ distance myself < food-area ] `
> - `ask patch (-0.8 * max-pxcor) (0.8 * max-pycor)`
> - `if sum [ food ] of patches = 0 and sum [ pheromone ] of patches = 0 and auto-stop?  [ set finish-time ticks set auto-stop? false ] `
> - `diffuse pheromone (diffusion-rate / 100) `  

## Simple Economy Model 
