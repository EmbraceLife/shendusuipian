[Big Debt Crisis.pdf](Big Debt Crisis.pdf)

## What is goodness or badness of debt

```
goodness-badness = what credit produces or how the debt is repaid
```

> Clearly, giving the ability to make purchases by providing credit is, in and of itself, a good thing, and not providing the power to buy and do good things can be a bad thing. the question of whether rapid credit/ debt growth is a good or bad thing hinges on what that credit produces and how the debt is repaid (i.e., how the debt is serviced).

## No debt can be as bad as Too much bad debt

```
badness-no-debt = value-losing-opportunities = value-too-much-bad-debt
```

> too little credit/debt growth can create as bad or worse economic problems as having too much, with the costs coming in the form of foregone opportunities.

## How to measure whether a debt is good or not 

```
if productivity-on-credit > threshold [ 
   set sufficient-income-service-debt? true
   set debt good-debt]
```

> Generally speaking, because credit creates both spending power and debt, whether or not more credit is desirable depends on whether the borrowed money is used productively enough to generate sufficient income to service the debt.

## When is subway debt good or bad?

```
;; In what scenario, is subway debt a good one?
let repayment-25y subway-revenue * (1 + revenue-growth-rate) ^ 25 - yearly-cost * (1+inflation-rate) ^ 25 + (social-economic-benefit-25y - gov-subsidies-25y)
if debt - repayment-near > 0 and repayment-25y > debt * 1.02 ^ 25  [ set debt good-debt ] 
```

> Suppose that you, as a policy maker, choose to build a subway system that costs $1 billion. You finance it with debt that you expect to be paid back from revenue, but the economics turn out to be so much worse than you expected that only half of the expected revenues come in. The debt has to be written down by 50 percent. Does that mean you shouldn’t have built the subway? 
>
> Rephrased, the question is whether the subway system is worth $500 million more than what was initially budgeted, or, on an annual basis, whether it is worth about 2 percent more per year than budgeted, supposing the subway system has a 25-year lifespan. Looked at this way, you may well assess that having the subway system at that cost is a lot better than not having the subway system. 

```
;; In what scenario, is subway debt a really bad one?
let repayment-25y subway-revenue * (1 + revenue-growth-rate) ^ 25 - yearly-cost * (1+inflation-rate) ^ 25 + (social-economic-benefit-25y - gov-subsidies-25y)
if debt - repayment-near > 0 and repayment-25y < 0  [ set debt really-bad-debt ] 

;; what is the ratio of really-bad-debt to GDP ?
to-report bad-debt-to-gdp write-down-ratio bad-debt-total-debt-ratio
   let bad-debt-value total-debt-value * bad-debt-total-debt-ratio
   let bad-debt-write-down bad-debt-value * write-down-ratio
   let GDP total-debt-value / 2
   report bad-debt-write-down / GDP
end 

;; if bad debt is 20% of total debt, which has to lose 40% of value, total-debt is twice GDP
let gdp-drop bad-debt-to-gdp 40% 20% ;; then value to lose is equal to 16% GDP

;; to drop 16% of GDP within a year, is not tolerable; but drop 1% of GDP per year for 16 years, is tolerable. But whether policy maker will spread loss depend on two factors 
ask really-bad-debt [
  if debt-currency-control > threshold and influence-over-creditor-debtor > threshold [ set tolerable true ]
  ]
```

> downside risks of having a significant amount of debt depends a lot on the willingness and the ability of policy makers to spread out the losses arising from bad debts. I have seen this in all the cases I have lived through and studied. Whether policy makers can do this depends on two factors: 1) whether the debt is denominated in the currency that they control and 2) whether they have influence over how creditors and debtors behave with each other.

## Are Debt cycles inevitable ?

```
;; Debt cycles are inevitable ?
if human-short-sightedness > threshold1 and political-short-sightedness > threshold2 [ set credit-loose true]
;; maybe 95% time human and political short-sightedness is greater than the thresholds
;; how to model human-short-sightedness and political-short-sightedness?
```

> Throughout history only a few well-disciplined countries have avoided debt crises. While policy makers generally try to get it right, more often than not they err on the side of being too loose with credit because the near-term rewards (faster growth) seem to justify it. It is also politically easier to allow easy credit (e.g., by providing guarantees, easing monetary policies) than to have tight credit. That is the main reason we see big debt cycles.

