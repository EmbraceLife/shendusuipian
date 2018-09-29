# An Agent-Based Model of the English Housing Market

[original paper and model](http://cress.soc.surrey.ac.uk/housingmarket/ukhm.html) 

## Abstract

> Uniqueness of UK house market 
>
> - Stock of houses is fixed in short term
> - buyers need finance to buy houses 
> - prices are set by realtors 
>
> Why ABM
>
> - to explore the emergence features out of interactions between multiple agents 

## The Housing Market

> Conventional approach 
>
> - top down, econometric model 
> - use interest rate, income, supply and demand of houses 
> - to estimate price projection 
>
> drawbacks of conventional approach 
>
> - know little of underlying mechanism of housing market 
>
> potential advantages of using ABM 
>
> - to model **locations**, which is critical to prices at micro-level 
> - to incorporate **realtors**, who set the price, as a different agent to households, 
> - to explain better the house price to earning ratio **over time** 
>
> Uniqueness to previous researches 
>
> - incorporate realtors 
> - don't model buyer or seller utility nor assume utility maximization
>   - this paper, all buyers assume high price equal to high quality 
>
> Simulating complex patterns of housing market 
>
> - to replicate real world housing market key features 
>
> - phenomena 1 : sticky downward 
>
>   - demand increase, price rise in short term, price stable and fall as more houses are into the market 
>   - demand decrease, price will be stable in short term, but in long run it will fall 
>
>
>

# Code Problems 

## Drop owner numbers

### Problem Description

> within 100 ticks number of owners halfed
>
> nDiscouraged and nForceOut continued to rise, nDiscouraged is the larger part
>
> no matter how interest rate change, income-shock change, the above situation does not change 

### Approach 1

> nDiscouraged is due to long time being homeless, not able to buy a house 
>
> nForceOut is due to repayment is greater than income 
>
> so, I suspect the problem lies at the buying and valuation processes 
>
> [Inspection strategy](https://github.com/EmbraceLife/shendusuipian/blob/8aec0a6fa95307dfeeaf664218426cb3ce28099b/complexity_demos/Housing%20market%20in%20process#L693) to look for the cause of the problem

### Reflection 1

> Inspection on the entire system is difficult, as it is too complex and interactive. 
>
> ==Inspect thoroughly each part during code construction== 
