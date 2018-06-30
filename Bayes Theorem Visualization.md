[book cover](http://m.qpic.cn/psb?/V119hAgO3eS46m/yaBrqVIRjnGGN4xNzctrt5iQDPoe.DoeSfxrEh*UKD4!/b/dEABAAAAAAAA&bo=1ANuBNQDbgQDCSw!&rf=viewer_4)  

# Bayes Everyday 

## Book intro

> what is Bayes' theorem and how does it work
>
> is simple and built on elementary math
>
> different names: Bayes' rule, Bayes' theorem, Bayes' formula

## used everywhere

> help display google search result 
>
> same true to Netflix recommendations
>
> Hedge funds, self-driving cars, search and rescue 

## Nature 

> a simple math formula revolutionalized how understand and deal with uncertainty
>
> if life is black and white, Bayes' Theorem help to think about the gray areas
>
> how much should we change our confidence in a belief when given new evidence

## Examples

> a test for cancer came back positive, what is the probability of having cancer if the test is positive?
>
> what is the probability that the dog likes you given it licks you?
>
> what is the probability the stock prices will fall given interest rate rises?
>
> what is the probability you are truly drunk given the breathalyzer test is positive?

## why visual?

> applying the theorem is not intuitive for most people

## Visual Aids

> [Venn Diagrams](http://m.qpic.cn/psb?/V119hAgO3eS46m/8fFCYtIzwuPC8M8uy3FujsUxrxtIOQFsNVQ2EDqRhKk!/b/dC8BAAAAAAAA&bo=1gNOAtYDTgIDCSw!&rf=viewer_4) 
>
> [Decision Trees](http://m.qpic.cn/psb?/V119hAgO3eS46m/dapBaWT3sbEAfWPZyQWxoBLSN2kTFYXdRTJMq1zeUZA!/b/dIMAAAAAAAAA&bo=0ANIAtADSAIDGTw!&rf=viewer_4)
>
> Letters (T, H for tail and head)
>
> Physical objects (real coins)

# A Visual Intro Part 1

## Bayes' theorem without formula 

### Problem setting

> [a box with 2 outcomes](http://m.qpic.cn/psb?/V119hAgO3eS46m/lCusU*hqR6kX*EBi2jjqo5eeJ*Gas4.J6DgKB94JPvE!/b/dDMBAAAAAAAA&bo=1ANGAtQDRgIDCSw!&rf=viewer_4), both are equally likely to happen
>
> - p(A) = 1/2, p(B) = 1/2
>
> a box with 3 outcomes, all of them are equally likely to happen
>
> - p(A) = 1/3, p(B) = 1/3, p(C) = 1/3
>
> focus on [first case](http://m.qpic.cn/psb?/V119hAgO3eS46m/OtU9mzDSZniy.*NtZCgh72QCkCd4U7bi5eTL7ccDX2E!/b/dDABAAAAAAAA&bo=zgM6As4DOgIDGTw!&rf=viewer_4), two types of cookies, [chocolate and peanut](http://m.qpic.cn/psb?/V119hAgO3eS46m/50SPuxzJw8*gmF7yxpQT1Hh42qD4*8GYv4Fr1HakoT4!/b/dEABAAAAAAAA&bo=0gNMAtIDTAIDCSw!&rf=viewer_4) 
>
> - p(A) = 1/2, p(B) = 1/2
> - P(chocolate) = 3/4, P(peanut butter) = 1/4

### Problem proposed

> prob(boxA | chocolate cookie) ?>? prob(boxB | chocolate cookie) 
>
> **intuitive:** box A has double the amount of chocolate than box B

### Explanation

> New Evidence change the universe 
>
> - Evidence: given a chocolate cookie
> - Ignorance: peanut butter cookie ([sample space changed](http://m.qpic.cn/psb?/V119hAgO3eS46m/MdQ4JfO7ucjhPmi5JIKaHIOGg9R57aLUzkdpG4a5ANc!/b/dGEBAAAAAAAA&bo=1ANOAtQDTgIDCSw!&rf=viewer_4))
> - [new universe](http://m.qpic.cn/psb?/V119hAgO3eS46m/gs1Duxkk1NZIgKZPVK11i01qykJ0JniE2YwkRtDNHzo!/b/dC4BAAAAAAAA&bo=zgNEAgAAAAADB6k!&rf=viewer_4) has only 15 chocolate cookies,  A has 10, B has 5
>
> prob(boxA | chocolate cookie) = 2/3 
>
> prob(boxB | chocolate cookie) =1/3

## The Bayes' theorem Fomula

### [3 ingredients](http://m.qpic.cn/psb?/V119hAgO3eS46m/b2K9Zk3P28YW91Xh7J0.VxfxiMF4co8szRynpClT2vA!/b/dC0BAAAAAAAA&bo=0ANOAtADTgIDCSw!&rf=viewer_4) of the formula

> [meaning of each component](http://m.qpic.cn/psb?/V119hAgO3eS46m/2bhK.Z.EpZhQctZyrw.naJNnLbOvS71M8NPW9P4knRc!/b/dDEBAAAAAAAA&bo=1gNQAtYDUAIDORw!&rf=viewer_4) of the formula
>
> posterior probability = normalized weighted average

### solution with formula

> [apply formula](http://m.qpic.cn/psb?/V119hAgO3eS46m/a2ahu91Z0Rua3G9fvxYBafRrLh6Q0cucWJCDwS6rwVQ!/b/dDABAAAAAAAA&bo=0gPiANID4gADCSw!&rf=viewer_4) to the problem above 
>
> P(B | A) = P(chocolate cookie | box A) = 100% sure = 1
>
> P(A) = P(box A) = 50% of universe = 0.5
>
> P(B) = P(get a cholocate cookie) = # chocolate / # universe = 15/20 = 0.75
>
> [simple calculation process](http://m.qpic.cn/psb?/V119hAgO3eS46m/WWRM33d65HUuI9A1z.KoZ.8P0tVp5IQFtcpXnmf0UOA!/b/dPMAAAAAAAAA&bo=zgNOAs4DTgIDCSw!&rf=viewer_4)

# Solving for one possible outcome with all data provided

## Senario 1: The Flu

### Problem Setting

> “You have a headache and sore throat, and you know that people with the flu have the same symptoms roughly 90% of the time. In other words, 90% of people with the flu have the same symptoms you currently have. Does this mean you have the flu?”
>
> Excerpt From: Dan Morris. “Bayes Theorem: A Visual Introduction For Beginners.” iBooks. 

### Posterior Probability

> what is probability you have a flu, given you find out you have a headache, sore throat?
>
> - P(Flu | headache and sore throat) **Posterior probability**

### Prior Knowlege

> search in google to find more **prior knowledge** about the flu
>
> - P(Flu | all population in general) = 5%
>
> search in google to find **prior knowledge** about headache and sore throat
>
> - P(headache and sore throat | all population in general) = 20%

### Likelihood

> personal belief about relationship between Flu and [headache with sore throat]
>
> - P(headache and sore throat | Flu) = 90% **current belief or likelihood** 

### Base Rate Fallacy

> **Don't fall into common error trap** to assume
>
> - P(A | B) = P(B | A) 
> - P(headache and sore throat | Flu) = P(Flu | headache and sore throat) 
> - so P(Flu | headache and sore throat) = 90% (**wrong**)

### Visualizing the problem and solution

> use Venn Diagram to [show what we know](http://m.qpic.cn/psb?/V119hAgO3eS46m/K0xehlamTJtsFhQjo3Xm.5EZpyiuLqah5Rf5F5aVYJA!/b/dDIBAAAAAAAA&bo=1ANKAtQDSgIDCSw!&rf=viewer_4)
>
> $P(A \bigcap B)$ is **not known or given**, but formula does not need it
>
> [apply to Bayes' theorem](http://m.qpic.cn/psb?/V119hAgO3eS46m/89xI9AgrjEupJlkcIscGEmoBo4zSnFlW.aRdcy1EDe0!/b/dIMAAAAAAAAA&bo=0gNcAdIDXAEDCSw!&rf=viewer_4) and [calculate the answer](http://m.qpic.cn/psb?/V119hAgO3eS46m/VWWN6nmfruK6Tbll2V16SI7vPmV.vxjYTpPYT.7Chqs!/b/dFYAAAAAAAAA&bo=zANGAswDRgIDGTw!&rf=viewer_4) 
>
> [many highly educated people](http://m.qpic.cn/psb?/V119hAgO3eS46m/6YMkMJu7FsaBtOK0UUTthJn0Q7AazauzanbXtO4F6zs!/b/dDEBAAAAAAAA&bo=JgSGAiYEhgIDGTw!&rf=viewer_4) don't know about Bayes' theorem

## Scenario 2: Breathalyzer 

### Problem

> you are a police officer, “Around 2 am you randomly pull over a vehicle and have the driver take a breathalyzer test, and the result is positive. You assume the test is accurate and think nothing of it as you process the driver”
>
> are you really correct in assuming so?

### Visualizing the solution

> prior knowledge on [drunk driving](http://m.qpic.cn/psb?/V119hAgO3eS46m/PGrVZv3KeHAyiqpo9WsTFwc4EtekWFLtErkP.TlO8ko!/b/dPIAAAAAAAAA&bo=0gNOAtIDTgIDCSw!&rf=viewer_4) and [testing positive](http://m.qpic.cn/psb?/V119hAgO3eS46m/xFHDFyAiVDmowyYnsaLLYpFCxp78DiP2g5JujzrSrgk!/b/dDMBAAAAAAAA&bo=zANMAswDTAIDKQw!&rf=viewer_4) in general
>
> visualizing likelihood, [causal effect from drunk driving to test result](http://m.qpic.cn/psb?/V119hAgO3eS46m/1RRkv6RCj8gCteawSESoipr8rtrTidSWyFyzbcQfSqQ!/b/dDEBAAAAAAAA&bo=0ANKAtADSgIDKQw!&rf=viewer_4) 
>
> [apply formula](http://m.qpic.cn/psb?/V119hAgO3eS46m/73ytFVJZsw0fKvrtIsbG2GNX0TgDsu2YarI0VncKC3M!/b/dDABAAAAAAAA&bo=0ANCAtADQgIDKQw!&rf=viewer_4) to the problem
>
> [far cry difference](http://m.qpic.cn/psb?/V119hAgO3eS46m/9IvBOpyyoYgSsPlLoZ0DxaAd3a.GetsUKuDj9i14nYU!/b/dC0BAAAAAAAA&bo=0gNOAtIDTgIDKQw!&rf=viewer_4) between P(positve | drunk driving) vs P(drunk driving | positive) 

## Scenario 3: Peacekeeping - A surprise attack

### problem

> “the probability of the truck being rigged with a gun given that we were just fired at with heavy firepower.”

### visualizing the solution

> [prior knowledge](http://m.qpic.cn/psb?/V119hAgO3eS46m/LnBxi2LH6kUsCuvb3VH0nnfShVShuh2issYDLsvw378!/b/dEMBAAAAAAAA&bo=0ANOAtADTgIDCSw!&rf=viewer_4) P(a rebel truck with guns | all rebel trucks ) = 40%
>
> prior knowledge or [observations](http://m.qpic.cn/psb?/V119hAgO3eS46m/Xn5sSRv3bAHNO*lu97wZ2Y26t8fVgO*aKifW1YtQ29o!/b/dDABAAAAAAAA&bo=0gNMAtIDTAIDORw!&rf=viewer_4) P(rebel truck with heavy firepower | all rebels trucks ) = 50%
>
> [likelihood](http://m.qpic.cn/psb?/V119hAgO3eS46m/xfcdNOQxx.PxTOAsIVqTkUgTOwLp6w*WmH9rWjEEfHI!/b/dDABAAAAAAAA&bo=1gNOAtYDTgIDCSw!&rf=viewer_4) P(rebel truck with heavy firepower | rebel with gun) = 80%
>
> [apply formula](http://m.qpic.cn/psb?/V119hAgO3eS46m/9Lh6TeeJk6*AZEQIYuPpL1b5fgbp8UwCfVQrRsrAkNg!/b/dGEBAAAAAAAA&bo=2gNiAdoDYgEDGTw!&rf=viewer_4) to problem and [calculate the result](http://m.qpic.cn/psb?/V119hAgO3eS46m/5mBpWbSR4Chm4Im34LmlDeoZS31CxudC6*RYVlbs9j4!/b/dEYBAAAAAAAA&bo=0gNEAtIDRAIDGTw!&rf=viewer_4) 
>
> whether or not have a far cry difference depends on how much is updated on the belief

# Solving for one possible outcome with No P(B) provided

> previously 3 ingredients are given, now only 2 ingredients are given, [P(B) must be discovered by ourselves](http://m.qpic.cn/psb?/V119hAgO3eS46m/4N.S5n1qdJUEC9VxsMlZuPwXLZH3AAh1j83zBhh8FCw!/b/dEMBAAAAAAAA&bo=1gNMAtYDTAIDCSw!&rf=viewer_4)  
>
> decision tree is a powerful tool to help find P(B) 

## Scenario 1: The Flu

### Problem

> after lunch, having headache and sore throat
>
> Google tells 5% of population will get Flu every year P(Flu | all) = 5%
>
> App test with symptoms, report Flu positive
>
> P(positive | Flu) = 75% (correctly predict with Flu 75% of time)
>
> P(positive | No Flu) = 20% (wrong predict with Flu 20% of time)
>
> what to know: P(Flu | positive)

### Visualizing the solution

> [start with what we know](http://m.qpic.cn/psb?/V119hAgO3eS46m/*0yhGAfeEeYin3XYtXhKAjvax73vsv5q8*xjqie9zqE!/b/dDMBAAAAAAAA&bo=0ANQAtADUAIDGTw!&rf=viewer_4), the most basic node (have two branches)
>
> - P(Flu | over all population)
> - P(No Flu | over all population)
>
> build upon primary branches, [produce 4 secondary branches ](http://m.qpic.cn/psb?/V119hAgO3eS46m/0vcveN.Vk9OMDKRbh3MeRbX1tS41rObZAGCTdRXUZ.E!/b/dEIBAAAAAAAA&bo=0gNQAtIDUAIDCSw!&rf=viewer_4) 
>
> - branches from each node, sum to 1 
> - having 3 nodes so far
>
> [meaning of final nodes](http://m.qpic.cn/psb?/V119hAgO3eS46m/aCXc6hvH*E7R8HwkQ2dEXK0xWHz2m2Y6PMs1UtelyXw!/b/dDABAAAAAAAA&bo=1gNWAtYDVgIDCSw!&rf=viewer_4) on the end of secondary branches 
>
> - top final node = P(Flu) * P(positive | Flu) = P(Flu ^ Positive)
> - each final node = branches (on each node path) multiple together 
> - final node 1 = path 1 = P(Positive ^ Flu)
> - final node 2 = path 2 = P(Negative ^ Flu)
> - final node 3 = path 3 = P(Positive ^ no Flu)
> - final node 4 = path 4 = P(Negative ^ no Flu)
> - all final nodes sum up to 1
>
> How to discover P(B)
>
> - P(B) = path 1 + path 3 = P(positive ^ Flu) + P(positive ^ no Flu)
>
> [apply the formula](http://m.qpic.cn/psb?/V119hAgO3eS46m/aO0etvHedufQFyIEmRy8IINhWwmGlF*G7VxtOSzwTWM!/b/dDABAAAAAAAA&bo=0ANcAdADXAEDGTw!&rf=viewer_4) and [calc the result](http://m.qpic.cn/psb?/V119hAgO3eS46m/82MnqA.XC3sCg2kl5IDWNAEtyd3S0pJJGJ0SA2moZZg!/b/dC0BAAAAAAAA&bo=0gNOAtIDTgIDKQw!&rf=viewer_4) 

## Scenario 2: The Drunk Driver

### problem

> prior knowledge
>
> - “Approximately 3 out of every 1000 drivers will drive while drunk. This is .3%.
>
> likelihood P(positive | drunk)
>
> - The breathalyzer test does not always detect a drunk person. This is not 100% like you both previously thought, but 98%.
>
> likelihood P(positive | not drunk)
>
> - 4% of the time breathalyzer tests give a positive result for someone who is not drunk. This is called a false positive.”
>
> goal = Posterior probability = P(drunk | positive)

### Visualizing Solution

> [decision tree solution](http://m.qpic.cn/psb?/V119hAgO3eS46m/RxLSR8u4dikmf6YqiGZGxZQpU37wudMaXUXjKPSolZI!/b/dDMBAAAAAAAA&bo=3ANUAtwDVAIDCSw!&rf=viewer_4)  
>
> [apply the formula](http://m.qpic.cn/psb?/V119hAgO3eS46m/Aq8hozlcFJ5k65765Iy.S.tmkY2pNoJn5pZwFFoHQGk!/b/dEcBAAAAAAAA&bo=2ANeAdgDXgEDGTw!&rf=viewer_4)  

## Scenario 3 Peacekeeping - a surprise attack

### problem

> prior knowledge: P(rebels) = 100/175
>
> - “There are roughly 100 rebels in the city and 75 coalition troops.”
>
> likelihood: P(positive | rebels) = 65%
>
> - “Local Intel is not always reliable. In your experience it correctly predicts rebels 65% of the time.”
>
> likelihood: P(positive | no rebels) = 15%
>
> - “Intel has been sketchy lately and has incorrectly predicted men as rebels when they are not rebels 15% of the time”
>
> what to know: Posterior probability = P(rebels | intel says positive)
>
> - “We want to know the probability that the soldiers are rebels given that Intel says they are.”

### Visualizing Solution

> apply what we know above to [a decision tree](http://m.qpic.cn/psb?/V119hAgO3eS46m/t9PtiogZeZD.CsO*3*X.GVdINBtrFZS3MR8MphUNWyc!/b/dDIBAAAAAAAA&bo=1ANSAtQDUgIDCSw!&rf=viewer_4)
>
> [apply the formula](http://m.qpic.cn/psb?/V119hAgO3eS46m/orm5dn6lxJCFOyQ5l63fB9fvdw37gBiDyCCSiI7ivh8!/b/dEEBAAAAAAAA&bo=zANWAcwDVgEDGTw!&rf=viewer_4) 

# Solving for two possible outcomes with all probability data provided

> given symptoms (sneezing and coughing), previously we want to know P(cold | symptoms)
>
> now, we want to know P(cold | symptoms) vs P(allergy | symptoms)?
>
> so, we will use Bayes' formula twice

## Scenario 1: The Flu

### problem

> likelihood on Flu or food poison causing symptoms
>
> - P(symptoms | Flu) = 90%, P(symptoms | food poison) = 75%
> - “You have a slight headache and sore throat, and you see that people with the flu have the same symptoms as you 90% of the time. People with food poisoning have the same symptoms 75% of the time”
>
> prior knowledge on Flu or food poison
>
> - P(Flu | all population) = 5%, P(food poison | all population) = 16%
> - “You see that the probability of having the flu is 5%, while the probability of having food poisoning is 16%”
>
> prior knowledge or observations
>
> - P(symptoms = headache and sore throat | all population) = 20%

### Visualizing Solutions

> using Venn Diagram twice
>
> apply the formula twice

# Advanced usage

## Search and Rescue 

> location and time - find the lost person at sea
>
> ![image-20180630183220523](/var/folders/gz/ch3n2mp51m9386sytqf97s6w0000gn/T/abnerworks.Typora/image-20180630183220523.png) 
>
> [SAROPS paper](http://www.metsci.com/Portals/0/Search%20and%20Rescue%20Optimal%20Planning%20System.pdf)

## spam filtering

> 1998 Microsoft use bayesian filter for spam emails
>
> ![image-20180630183118517](/var/folders/gz/ch3n2mp51m9386sytqf97s6w0000gn/T/abnerworks.Typora/image-20180630183118517.png)
>
> microsoft paper on [Bayesian filter](https://pdfs.semanticscholar.org/b449/8c71651f0327b5d51c8f8008d5a1804a084a.pdf)

## Driverless Car

> use a Bayesian model similar to hidden markov model for localization
>
> [stanford driverless car page](http://stanford.edu/~cpiech/cs221/apps/driverlessCar.html)

# 3 steps to think like a Bayesian everyday

## scenario 1: Dating

### Non-Visual Approach

> prior knowledge 
>
> - P(a gilr likes you | all girls on date) = 20%
> - P(a gilr not like you | all girls on date) = 80%
> - number 1 = 2 (out of 10)
> - number 2 = 8 (out of 10)
>
> likelihood 
>
> - P(laughing and flirting | she likes you) = 90%
> - number 3 = 9 (out of 10)
> - P(laughing and flirting | she not like you) = 10%
> - number 4 = 1 (out of 10)
>
> goal = P(she likes you | laughing and flirting)
>
> - option1 = P(laughing and flirting | she likes you) * P(a girl likes you) = 9 * 2 = 18 = P(laughing and flirting ^ she likes you)
> - option2 = P(laughing and flirting | she not like you) * P(a girl not like you) = 1 * 8= 8 = P(laughing and flirting ^ she not like you)
> - option1 : option2 = 9:4 > 50%

### Visual Approach

> [prior knowledge](http://m.qpic.cn/psb?/V119hAgO3eS46m/NbNmwgrPQ.kT*fvtsAnUvWUIJDnEQfa2hqO2yXEGG6k!/b/dC8BAAAAAAAA&bo=0gNQAtIDUAIDCSw!&rf=viewer_4) visualized
>
> [likelihood](http://m.qpic.cn/psb?/V119hAgO3eS46m/hXFK*DIintJBRVTUPutfO1RD7cCoqHomGL8ZzSAOODo!/b/dFcAAAAAAAAA&bo=1gNUAtYDVAIDORw!&rf=viewer_4) visualized
>
> [calculate](http://m.qpic.cn/psb?/V119hAgO3eS46m/xdyPN31A9xMn6So1h4K1jmbw8sLgeUy52GYwSPRlo1g!/b/dDABAAAAAAAA&bo=0gNKAtIDSgIDGTw!&rf=viewer_4) option 1 and option 2 to compare

## Scenario 2: Can you trust your mechanic?

### Non-Visual approach

> prior knowledge
>
> - P(honest mechanics | all mechanics) = 70%
> - Number 1 = 7 (out of 10)
> - P(dishonest mechanics | all mechanics) = 30%
> - Number 2 = 3 (out of 10)
>
> likelihood 
>
> - P(bad reviews | honest mechanics) = 30%
> - Number 3 = 3
> - P(bad reviews | dishonest mechanics) = 90%
> - Number 4 = 9
>
> goal
>
> - P(honest mechanics ^ bad reviews) = number 1 * number 3 = 21
> - P(dishonest mechanics ^ bad reviews) = number 2 * number 4 = 27
> - 27 > 21 = given bad reviews, more likely to run into a dishonest mechanics

### Visual approach

> [prior knowledge](http://m.qpic.cn/psb?/V119hAgO3eS46m/Y.Nm9E1EVawPHAp1MPvfKlvTMpSzQDupVo2MVxODqwI!/b/dDABAAAAAAAA&bo=0gNOAtIDTgIDCSw!&rf=viewer_4) visualized
>
> [likelihood](http://m.qpic.cn/psb?/V119hAgO3eS46m/SlCwybLjoEHqlONSfyfNAK.pqMDnv0AESBxvsbPOuXs!/b/dDABAAAAAAAA&bo=0ANOAtADTgIDSWw!&rf=viewer_4) visualized
>
> [calculation](http://m.qpic.cn/psb?/V119hAgO3eS46m/GQIC0zBAtWbiopDpD1aLrsNL*jegGrrtfamNLYhvMWc!/b/dEEBAAAAAAAA&bo=zgNMAs4DTAIDGTw!&rf=viewer_4) visualized