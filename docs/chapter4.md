---
layout: page
title: "Chapter 4"
permalink: /docs/chapter4/
---

# Probability and Uncertainty


> **Course dataset & lab.** Work this chapter's techniques on our spine dataset — [Texas City Sales Panel](../datasets). Standardize per-capita sales tax within a year (z-scores) and use Excel's `NORM.S.DIST` to find proportions.


## Epigraphs


> 
*"Chance is perhaps the pseudonym of God when he does not want to sign."*

 Anatole France


> 
*"Not everything that counts can be counted, and not everything that can be counted counts."*

 Attributed to Einstein


Public administrators confront uncertainty far more often than certainty. Emergency calls fluctuate
hour by hour, budgets shift with economic cycles, and neighborhood-level outcomes vary in ways
that reflect both structural inequalities and unpredictable shocks (Sampson 2012; Chetty & Hendren 2016). Probability is the set of ideas and tools we use to formalize—rather than eliminate—
uncertainty.


## Opening Case: Dallas Flood Maps and the Meaning of a "100-Year Flood"


In 2023, the Dallas Morning News reported that updated Federal Emergency Management Agency (FEMA) flood-plain maps would redraw the boundaries of high-risk flood zones across Dallas County, adding thousands of properties to areas requiring federal flood insurance and removing others (Dallas Morning News 2023). The changes provoked sharp debate. Homeowners newly placed in flood zones faced insurance costs of several thousand dollars per year. Developers whose properties were removed from risk zones gained approval for projects that had previously been blocked. City engineers argued that the new maps better reflected current drainage infrastructure, while residents countered that the models failed to account for recent upstream development that had increased impervious surface area and runoff.

At the center of the controversy was a deceptively simple concept: the "100-year flood." FEMA defines this as a flood event with a 1 percent annual probability of occurrence---not, as many residents assumed, a flood that happens once every hundred years. The distinction matters enormously. A 1 percent annual probability implies roughly a 26 percent chance of at least one such event over a 30-year mortgage. Misunderstanding this probability led both homeowners and elected officials to underestimate risk, while critics of the maps argued that even the 1 percent figure was too low given changing land use patterns and climate trends.

For an analyst, the flood map dispute is a case study in applied probability. Every element of this chapter---probability rules, conditional probability, rare events, and the assumptions built into distributional models---is visible in the public debate over which neighborhoods face flood risk, and why.


**Guiding Questions**


    - What does it mean to say a neighborhood faces a "1% annual chance" of flooding, and why is that not the same as one flood per century?
    - How do the assumptions built into FEMA's hydrological models---about rainfall, drainage capacity, and development patterns---shape the probability estimates on flood maps?
    - If flood risk depends on both location and infrastructure investment, how would you express this relationship using conditional probability?


## Why This Chapter Matters

Probability is foundational to every topic that follows: sampling, confidence intervals, hypothesis
testing, regression, forecasting. Without a clear understanding of uncertainty, statistical
inference collapses into guesswork.

In public administration, uncertainty is not merely an academic abstraction; it is an everyday operational constraint. City 311 call volumes spike unpredictably during storms or heat events (City of Austin open data), and EMS incidents vary by hour, neighborhood, and season in ways that no deterministic staffing plan can fully anticipate. Demand for public services depends on economic conditions and community behavior, while budget revenues fluctuate with tax bases and business cycles. These sources of variation are not anomalies to be eliminated; they are inherent features of the systems administrators manage.


As Einav and Levin note, modern administrative datasets are shaped by data-generating rules, operational constraints, and behavioral responses---not idealized experiments (Einav & Levin 2014). Probability provides structure for interpreting such data, allowing analysts to distinguish meaningful patterns from routine noise.


> 
**Briefing:** In public administration, uncertainty is a feature of the system—not a flaw in the analyst.


## The Concept of Uncertainty

Uncertainty arises when outcomes vary from one instance to the next. This variation might stem from natural randomness, such as the unpredictable arrival times of service requests, or from institutional processes like staffing levels and triage rules that change from shift to shift. Behavioral variation also plays a role: different neighborhoods report problems at different rates, and individual residents vary in how and when they contact government agencies. Environmental shocks---storms, power outages, seasonal temperature swings---add yet another layer of unpredictability. The goal of probability is not to predict perfect outcomes but to quantify these sources of uncertainty so that decisions can be made rationally.


Uncertainty appears in administrative datasets in two broad forms. The first is observable randomness: the number of pothole complaints varies day to day even when nothing about the road system has changed, daily water usage fluctuates with temperature, and EMS call rates shift by hour in patterns that are broadly predictable but never exact. Analysts can see this variation directly in the data and model it with probability distributions.


The second form is latent, structural randomness---uncertainty introduced by data-entry delays, categorization differences across staff members, and institutional processes that vary from one department to another. This type of variation is harder to detect because it is embedded in how data are collected and recorded rather than in the events themselves. Both forms reflect the institutional complexity highlighted in work on administrative data and neighborhood systems (Einav & Levin 2014; Sampson 2012).


## Probability Basics

Probability assigns numerical values to uncertain events. Let $A$ be an event:


$$
0 \leq P(A) \leq 1.
$$


If $P(A)=1$, the event is certain. If $P(A)=0$, it cannot happen. Most outcomes relevant to public
administrators fall in between.

Three rules govern probability:


    - **Non-negativity:** $P(A) \ge 0$
    - **Normalization:** $P(\Omega) = 1$ for the full set of possible outcomes $\Omega$
    - **Additivity:** If $A$ and $B$ are mutually exclusive,
    
$$
    P(A \cup B) = P(A) + P(B)
    $$


These rules allow analysts to build structured models from operational uncertainty.


> 
**Briefing:** Probability is not about predicting the next event—it's about understanding the long-run pattern.


## Random Variables

A random variable maps uncertain events onto numbers. In government operations, almost everything measured is a random variable: the number of 311 calls per hour, EMS response time, the count of overdue inspections, daily water consumption, and the time until a streetlight is repaired are all quantities whose values change unpredictably from one observation to the next. Formalizing these measures as random variables allows analysts to apply the tools of probability theory to operational questions.


A random variable $X$ may be discrete or continuous, and the distinction determines which probability models are appropriate. A discrete random variable takes on countable values, expressed as $X \in \{0, 1, 2, \ldots\}$. In the public sector, discrete random variables include the number of complaints received by a department in a day, the number of police incidents in a precinct during a shift, and the number of failed building inspections in a quarter. Because these variables count events, they are naturally modeled by distributions defined over non-negative integers.


A continuous random variable takes on values along a continuum, expressed as $X \in \mathbb{R}$. Examples from public administration include the time required to complete a service request, the dollar amount of property damage from a storm, and temperature-related demand for electricity. Continuous variables require density functions rather than simple probability tables, and their distributions often exhibit skewness and heavy tails that reflect the operational realities of government service delivery. Recognizing whether a variable is discrete or continuous is the first step toward selecting an appropriate probability model.


## Probability Distributions

Random variables have probability distributions that describe how likely different values are.

For a discrete variable:


$$
P(X = x_i) \ge 0, \quad \sum_i P(X = x_i) = 1.
$$


For a continuous variable, probabilities come from a density function $f(x)$:


$$
P(a \le X \le b) = \int_{a}^{b} f(x) \, dx.
$$


Descriptive statistics tell us what happened in a sample; probability distributions tell us the
patterns we expect in the long run.

This distinction mirrors the difference between neighborhood-level descriptive variation
(Sampson 2012) and national-level probabilistic mobility forecasts (Chetty & Hendren 2016).


> 
**Briefing:** Distributions translate uncertainty into structure.


## Common Distributions in Public Administration

Some probability distributions recur so frequently in public-sector problems that they deserve
special attention.

### Poisson Distribution

The Poisson distribution models counts of independent events occurring over a fixed period of time or within a fixed region. Its probability mass function is:


$$
P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}.
$$


The Poisson distribution appears throughout public administration because many operational processes involve counting discrete events that arrive more or less independently. A city department might use it to model the number of 311 complaints received per hour, allowing managers to estimate the probability of unusually high-volume periods and plan staffing accordingly. Emergency medical services rely on Poisson models to predict the number of calls per district per shift, which informs ambulance deployment and mutual-aid agreements. Traffic engineers apply the distribution to accident counts at intersections, identifying locations where observed crash frequencies exceed what the Poisson model predicts and thus warrant safety interventions. Even routine services such as library checkouts per day follow Poisson-like patterns when individual borrowing decisions are roughly independent of one another.

### Worked Example: Poisson Probabilities for 311 Complaints

Suppose a city department receives an average of $\lambda = 5$ complaints per hour. What is the probability of receiving exactly 3 complaints in a given hour? And what is the probability of receiving 8 or more?

**Step 1: $P(X = 3)$.**

$$
P(X=3) = \frac{5^3 \, e^{-5}}{3!} = \frac{125 \times 0.0067}{6} = \frac{0.842}{6} = 0.140
$$

There is approximately a 14% chance of receiving exactly 3 complaints in a given hour.

**Step 2: $P(X \geq 8)$.**
Rather than computing infinitely many terms, use the complement: $P(X \geq 8) = 1 - P(X \leq 7)$. Summing the Poisson PMF for $k = 0, 1, \ldots, 7$:

$$
P(X \leq 7) = 0.0067 + 0.0337 + 0.0842 + 0.1404 + 0.1755 + 0.1755 + 0.1462 + 0.1044 = 0.8666
$$


$$
P(X \geq 8) = 1 - 0.8666 = 0.133
$$

About a 13% chance of an unusually high-volume hour with 8 or more complaints.


*Figure: The Poisson distribution for $\lambda = 5$ complaints per hour, with probability mass concentrated between 2 and 8 complaints and a long right tail.*


### Exponential Distribution

Describes time between events:


$$
f(t) = \lambda e^{-\lambda t}, \qquad t \ge 0.
$$


Applications:


    - time until next emergency call,
    - time until next inspection failure,
    - time between utility outages.


### Normal Distribution

Although much administrative data are skewed (City of Austin open data), some aggregated measures
approximate normality due to the central limit theorem (Section below).

### Heavy-Tailed Distributions

Completion times, repair delays, and public complaints often follow long right-tailed distributions
because institutional bottlenecks produce extreme but informative cases (Einav & Levin 2014).


## The Normal Curve and z-Scores

The normal distribution—the familiar symmetric, bell-shaped curve—is the most important continuous distribution in statistics. Many measured quantities cluster around a central value, with values farther from the center growing progressively less common, and the normal curve gives this pattern a precise mathematical form. A normal distribution is fully described by just two numbers: its mean, which locates the center, and its standard deviation, which controls how spread out the values are.

Its central role comes partly from the Central Limit Theorem (discussed below): even when the underlying data are not normal, averages and totals computed from large samples tend toward a normal shape. This is why so much of statistical inference—confidence intervals, hypothesis tests, performance bands—rests on normal-curve reasoning.

### The Empirical Rule

For any normal distribution, the proportion of values falling within a given number of standard deviations of the mean is fixed. This is the **empirical rule**, often summarized as 68/95/99.7:

    - About **68%** of values fall within 1 standard deviation of the mean,
    - About **95%** fall within 2 standard deviations,
    - About **99.7%** fall within 3 standard deviations.

These benchmarks let an analyst judge quickly whether an observation is typical or unusual. A value more than two standard deviations from the mean lands in the outer 5% of a normal distribution—rare enough to warrant a second look.

### z-Scores: Standardizing a Value

To compare a value to the rest of its distribution, we convert it into a **z-score**, which expresses how many standard deviations the value lies above or below the mean:

$$
z = \frac{x - \bar{x}}{s}.
$$

A positive z-score means the value is above the mean; a negative one means below. A z-score of 0 sits exactly at the mean. Because z-scores are expressed in standard-deviation units, they let us place any value on a common scale and read off the area to its left—the percentile—from the standard normal curve.

### Reading Areas and Percentiles

The area under the normal curve to the left of a given z-score equals the proportion of values below it, which is its percentile. A z-score of 0 corresponds to the 50th percentile; a z-score of about 1.0 corresponds to roughly the 84th percentile (since 50% sit below the mean and another 34% sit between the mean and one standard deviation above it). Rather than memorizing a table, analysts read these areas directly with spreadsheet functions.

### Doing It in Excel

Excel handles every step of normal-curve work:

    - `STANDARDIZE(x, mean, standard_dev)` converts a raw value into its z-score.
    - `NORM.S.DIST(z, TRUE)` returns the area to the left of a z-score on the *standard* normal curve (mean 0, SD 1)—that is, the percentile.
    - `NORM.DIST(x, mean, standard_dev, TRUE)` returns the area to the left of a raw value directly, without first computing a z-score.
    - `NORM.INV(probability, mean, standard_dev)` runs the calculation in reverse: given a percentile, it returns the value at that point in the distribution.

The `TRUE` argument requests the cumulative area (the percentile); `FALSE` would instead return the height of the curve, which is rarely what an analyst wants.

> **Spine dataset.** Across our 1,180 Texas cities, 2024 per-capita sales tax averages about \$395 with a standard deviation of about \$596. Consider a city collecting \$585 per resident. Its z-score is
>
> $$
> z = \frac{585 - 395}{596} \approx 0.32.
> $$
>
> Entering `=NORM.S.DIST(0.32,TRUE)` returns about 0.63, so this city sits near the **63rd percentile**—higher than roughly two-thirds of Texas cities. Equivalently, `=NORM.DIST(585,395,596,TRUE)` gives the same answer without the intermediate z-score.

> **Caution: the normal model is only approximate here.** Per-capita sales tax is strongly right-skewed—a handful of tourism- and retail-heavy cities collect far more than the typical city—so the symmetric normal curve fits the data only loosely. The mismatch is easy to see at the tails. The normal model with mean \$395 and SD \$596 predicts that about 43% of cities exceed \$500 (`=1-NORM.DIST(500,395,596,TRUE)`), yet only about 21% of cities actually do. When a distribution is skewed, treat normal-curve percentiles as rough guides, not exact statements, and check them against the data.


## Joint Probability and Dependence

Events interact. Joint probability measures the likelihood of multiple events happening together:


$$
P(A \cap B).
$$


Events are:


    - **Independent** if $P(A \cap B) = P(A)P(B)$,
    - **Dependent** otherwise.


Dependence is common in public operations:


    - Heat waves increase electricity outages and EMS calls simultaneously.
    - Severe weather increases both flood complaints and traffic accidents.
    - Staffing shortages increase the chance of delays and backlogs.


Such dependencies mirror the structural clustering documented in neighborhood-level research
(Sampson 2012).


## Conditional Probability

Conditional probability focuses on how one event affects another:


$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}.
$$


Interpretation in public administration:


    - $P(\text{delay} \mid \text{weekend})$
    - $P(\text{high EMS volume} \mid \text{heat advisory})$
    - $P(\text{missing data} \mid \text{department})$ (U.S. GAO data-quality guidance)


> **Returning to the Case:** The Dallas flood map case is a natural application of conditional probability. Residents want to know $P(\text{flood} \mid \text{in FEMA zone})$ versus $P(\text{flood} \mid \text{not in FEMA zone})$. But the probability also depends on infrastructure: $P(\text{flood} \mid \text{in zone, new drainage})$ may differ substantially from $P(\text{flood} \mid \text{in zone, aging infrastructure})$. The policy debate over flood maps is, at its core, a debate about which conditioning variables belong in the probability model.

### Worked Example: Flood Probability Over a Mortgage

A property in a FEMA 100-year flood zone faces a 1% annual probability of a major flood. What is the probability of at least one flood over a 30-year mortgage?

**Step 1: Probability of no flood in a single year.**

$$
P(\text{no flood in year } i) = 1 - 0.01 = 0.99
$$


**Step 2: Probability of no flood in 30 years.**
Assuming independence across years:

$$
P(\text{no flood in 30 years}) = 0.99^{30} = 0.740
$$


**Step 3: Complement.**

$$
P(\text{at least one flood in 30 years}) = 1 - 0.740 = 0.260
$$


A 1% annual flood risk translates into roughly a 26% chance of at least one major flood over a 30-year mortgage—far higher than most homeowners assume.

Conditional patterns often reveal deep institutional insights—for example, that delays cluster in
specific neighborhoods or during certain seasons.


> 
**Briefing:** Conditional probability reveals hidden structure in operational systems.


## Bayes’ Rule

Bayes' Rule updates beliefs in light of new evidence:


$$
P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)}.
$$


Examples:


    - Updating outage risk when the weather forecast changes.
    - Revising projected call volume after early-morning patterns are observed.
    - Updating likely inspection failures given new information about facility age.


Bayesian reasoning mirrors real-time decision-making in emergency management, where agencies adjust
plans dynamically.


## Expectation and Variance

The expected value of a random variable $X$ is its long-run average:


$$
E[X] = \sum_i x_i P(X=x_i) \quad \text{(discrete)},
$$


$$
E[X] = \int x f(x) \, dx \quad \text{(continuous)}.
$$


Variance measures dispersion:


$$
\text{Var}(X) = E[(X - E[X])^2].
$$


These quantities are not just mathematical abstractions. They apply directly to:


    - forecasting call volumes,
    - budgeting under uncertainty,
    - assessing workload variability,
    - designing performance standards (U.S. OMB performance guidance).


High-variance neighborhoods often correspond to the structural inequalities documented in urban
research (Sampson 2012).


## Law of Large Numbers

The Law of Large Numbers (LLN) states:


$$
\bar{X}_n \to E[X] \quad \text{as } n \to \infty.
$$


This explains why aggregated administrative metrics (monthly totals, yearly averages) are stable
even when individual observations vary wildly.

Federal agencies such as the Census Bureau and the Bureau of Labor Statistics (BLS) rely on LLN when reporting economic and
demographic indicators (U.S. Census ACS; BLS).


> 
**Briefing:** The LLN explains why aggregate trends look orderly even when individual cases look chaotic.


## Central Limit Theorem

The Central Limit Theorem (CLT) states that averages of many independent observations tend toward a
normal distribution:


$$
\frac{\bar{X} - E[X]}{\sigma/\sqrt{n}} \to N(0, 1).
$$


The CLT justifies why:


    - budget forecasts use normal-theory confidence bands,
    - performance measures use normal approximations,
    - sampling distributions behave predictably.


But independence and identical distribution assumptions can fail in neighborhood-level processes
(Sampson 2012), which is why analysts must interpret CLT results carefully.


> 
**Briefing:** The CLT makes inference possible—but only when the administrative context supports it.


## Probability in Public Administration Practice

### Forecasting


$$
P(\text{High Volume Tomorrow})
$$


Used by 311 call centres to schedule staffing during weather events.

### Risk Assessment


$$
P(\text{Severe Delay} \mid \text{Low Staffing})
$$


Helps identify operational vulnerabilities.

### Equity Analysis


$$
P(\text{Delay} \mid \text{Neighbourhood Characteristics})
$$


Connects descriptive disparities to structural probabilities, consistent with neighborhood effects
research (Sampson 2012; Chetty & Hendren 2016).

### Performance Standards

Agencies often set probability-based standards (e.g., 90% of calls answered within 30 seconds), drawing on federal performance-measurement guidance (U.S. OMB performance guidance).


## Common Pitfalls

### Assuming Independence

Administrative processes are rarely independent; weather, staffing, and neighborhood conditions
create dependence structures.

### Overinterpreting Short-Run Frequencies

Small samples produce deceptive probabilities.

### Treating Rare Events as Impossible


> **Returning to the Case:** Dallas homeowners frequently interpreted their "100-year flood zone" designation as meaning a flood would not happen in their lifetime. But a 1% annual probability is far from impossible: over a 30-year mortgage it implies roughly a 26% chance of at least one major flood. Treating a rare event as an impossible one is one of the most consequential errors in applied probability.

### Ignoring Data-Generating Processes

Analysts must understand how data are collected (Einav & Levin 2014; U.S. GAO data-quality guidance) before
applying probability models.

Rare-but-consequential events (system outages, extreme delays, revenue collapses) matter
disproportionately.


> 
**Briefing:** Probability requires humility. Misapplied, it produces confident but empty claims.


## Practice and Application


    - Using 311 completion time data, estimate $P(\text{Delay} > 7 \text{ days})$ and compare across neighborhoods (Sampson 2012).

    - Compute conditional probabilities such as $P(\text{High Volume} \mid \text{Rain})$ using hourly call data (City of Austin open data).

    - Simulate Poisson arrivals for EMS calls and compare simulation outcomes with real administrative data (Texas DSHS EMS data).

    - Use Bayes’ Rule to update the probability of a major outage given new weather alerts.

    - Write a short memo explaining why LLN and CLT justify (or fail to justify) current departmental performance metrics.
    - A Texas city experiences an average of 3 water main breaks per month. Using the Poisson distribution, compute (in Excel or by hand) the probability of (a) zero breaks in a given month, (b) exactly 5 breaks, and (c) 6 or more breaks. Show your work. What staffing implications does the answer to (c) have?
    - Using the flood probability formula from this chapter, compute the probability of at least one major flood ($P = 0.02$ annually) over a 50-year planning horizon. Compare this to the 30-year mortgage calculation in the worked example. Write a one-paragraph memo to a city planner explaining why a "50-year flood" is not as rare as it sounds.


## Sources for Examples in This Chapter


    - City of Austin 311 open data portal (City of Austin open data).
    - Administrative data processes (Einav & Levin 2014).
    - Neighbourhood variation research (Sampson 2012; Chetty & Hendren 2016).
    - Federal standards and measurement guidance (U.S. OMB performance guidance).
    - Data reliability and reporting guidance (U.S. GAO data-quality guidance).
    - ACS and BLS methodological documentation (U.S. Census ACS; BLS).


## Transition to Chapter Five

Probability provides the conceptual foundation for statistical inference. In the next chapter,
we use probability to evaluate whether differences in data are meaningful or simply due to chance.
Chapter 5 introduces that toolkit.