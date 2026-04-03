---
layout: default
title: "Chapter 7"
nav_order: 7
---

# Paired *t-Tests*


## Epigraphs


> 
*"Without data, you are just another person with an opinion."*

 W. Edwards Deming


> 
*"Comparison is the death of joy."*

 Mark Twain


Deming reminds us that evidence must drive decisions; Twain reminds us that comparisons can mislead
when made poorly. The paired *t*-test resolves both tensions by comparing two measurements taken
on the *same* units—before and after a policy change, across two conditions, or across two time
points. This design removes much of the noise caused by individual differences and isolates the
effect of a treatment or intervention. In public administration, paired comparisons are among the
most powerful and common tools for evaluating reforms, service improvements, and operational
efficiency.


## Opening Case: Austin's Proposition B and the Homeless Counts That Could Not Agree


In May 2021, Austin voters passed Proposition B, reinstating a ban on public camping that had been relaxed two years earlier. This textbook takes no position on the merits of the policy itself; the case is included solely because the policy change created a natural analytical opportunity for a paired design. The city conducted point-in-time homeless counts in the same census tracts before and after the ban took effect. If the same geographic units were measured at two time points, any change in counts could be evaluated using within-unit comparisons (statesmanPropB).

The results were ambiguous. Some tracts showed substantial declines in visible homelessness after the ban. Others showed little change, and a few showed increases. Advocates for the ban pointed to the tracts with declines as evidence that the policy "worked." Opponents argued that the declines reflected displacement rather than resolution---people moved to less visible locations, wooded areas, or neighbouring jurisdictions---and that the counting methodology itself had changed between periods, with different volunteers, different routes, and different weather conditions affecting the tallies.

This case presents a textbook paired design: the same units (census tracts) measured at two time points (before and after a policy change). The paired *t*-test is the natural tool for evaluating whether the average within-tract change is distinguishable from zero. But the case also illustrates the limits of the method: measurement error in point-in-time counts, the possibility of displacement rather than reduction, and the challenge of attributing change to a single intervention when multiple forces operate simultaneously. The analytical value of the example lies entirely in its research design structure, not in any judgment about the policy's desirability.


**Guiding Questions**


    - If the same 50 census tracts are counted before and after Proposition B, why is a paired *t*-test more appropriate than an independent *t*-test?
    - Suppose 35 of 50 tracts show lower counts after the ban. Does that necessarily mean the ban reduced homelessness---or could other explanations account for the change?
    - How does measurement error in point-in-time counts affect the reliability of the paired comparison?


## Why This Chapter Matters

Many of the most important questions in public administration involve *change over time* for the
same units. A city manager may want to know whether average 311 completion times improved after a new workflow reform (austin311open), or whether an EMS district responded faster after staffing increases (dshsEMS). Inspectors and their supervisors ask whether inspection durations decreased after digital recordkeeping was introduced. Planners track whether census tracts experienced income growth from one ACS cycle to the next (uscensusACS), and community development officials examine whether residents in a neighborhood saw improved service delivery after targeted investment (sampson2012great). In every case, the analyst is comparing two measurements of the same unit---not two separate groups of units.

These questions do not compare two independent groups; they compare two *measurements of the same
units*. Ignoring this structure discards information, reduces power, and inflates noise---a point
emphasized repeatedly in statistical literature (gelman2007data, freedman2007statisticalmodels). A paired design eliminates variation between individuals by using each unit as its own control, dramatically increasing sensitivity to detect change, especially in small samples. When units vary widely at baseline---as neighborhoods, districts, and agencies almost always do---the gains from pairing can be substantial.


> 
**Briefing:** Paired tests measure *within-unit change*, not between-unit differences.


## What Makes a Paired Design Different?

In an independent *t*-test (Chapter~*chap:independentttests*), Group A and Group B
contain separate units. In a paired *t*-test, each observation in Period 1 has a natural partner
in Period 2:


$$
Unit}_i^{(1)} \leftrightarrow Unit}_i^{(2)}.
$$


Consider several examples of natural pairing in administrative data. A neighborhood’s average 311 request completion time before and after a workflow change forms a pair; the same EMS station’s response time early versus late in the year forms another. When the same inspector completes both paper and electronic forms, the two processing times are paired observations on the same individual. Similarly, the same census tract measured across two ACS survey cycles produces a natural pair of income estimates. In each case, the unit serves as its own baseline, and the analyst focuses on how much that unit changed rather than on how different two separate groups appear.

This structure reflects the principle Gelman and Hill stress: inference improves when analysts
respect the hierarchical and longitudinal structure of their data (gelman2007data).


## The Paired Difference

The paired *t*-test converts two variables into a single set of *differences*:


$$
D_i = X_{i,after}} - X_{i,before}}.
$$


The test evaluates whether the average change is zero:


$$
H_0: \mu_D = 0 
\qquadvs.}\qquad 
H_1: \mu_D \ne 0.
$$


> **Returning to the Case:** In the Proposition B case, $D_i$ represents the change in homeless count for census tract $i$: $D_i = count}_{after}} - count}_{before}}$. If the ban reduced visible homelessness, we would expect $D} < 0$. The paired design is essential here because tracts differ enormously in baseline counts---a tract near downtown Austin might count 50 individuals while a suburban tract counts 3. Comparing aggregate before-and-after totals (an unpaired approach) would be dominated by the high-count tracts. The paired difference isolates within-tract change, giving equal analytical weight to each geographic unit.}

### Worked Example: Homeless Counts Before and After Proposition B

Consider point-in-time homeless counts for 8 census tracts before and after the camping ban:


*[Table — see PDF version]*


**Step 1: Compute the mean difference.**

$$
D} = (-13) + (-2) + (-9) + 3 + (-13) + (-1) + (-11) + 3}{8} = -43}{8} = -5.375
$$


**Step 2: Compute the standard deviation of differences.**

$$
s_D = \sum(D_i - D})^2}{n-1}} = (-7.6)^2 + (3.4)^2 + \cdots + (8.4)^2}{7}} = 6.48
$$


**Step 3: Compute the $t$-statistic.**

$$
t = D}}{s_D / n}} = -5.375}{6.48 / 8}} = -5.375}{2.29} = -2.35
$$


**Step 4: Evaluate.**
With $df = 7$, the critical value for a two-tailed test at $\alpha = 0.05$ is approximately $\pm 2.36$. Our $t = -2.35$ falls just short of the threshold ($p \approx 0.051$). The result is borderline---suggestive of a decline but not conclusive at conventional significance levels. In Excel, use `=T.TEST(before\_range, after\_range, 2, 1)` for a two-tailed paired test.

**Interpretation.**
The average tract-level count declined by about 5.4 individuals, but substantial variation across tracts (some increased, most decreased) means we cannot rule out chance at the 5\


*[Figure — see PDF version]*


We then compute:


$$
D} = mean difference}, \qquad
s_D = standard deviation of differences}.
$$


The *t*-statistic is:


$$
t = D}}{s_D / n}}.
$$


This method removes between-unit variability, dramatically increasing statistical power—especially
when units vary widely at baseline, as they often do in service performance data.

Freedman notes that such within-unit adjustments often outperform more complex models when carefully
applied (freedman2007statisticalmodels).


> 
**Briefing:** The paired test focuses on *change*, not levels.


## Why Paired Designs Are Powerful

Paired tests are more sensitive than independent tests for three interconnected reasons, each of which matters in the administrative settings where these tests are most commonly applied.

### 1. They remove baseline variability

Neighbourhoods differ enormously at baseline---in demographics, population density, infrastructure age, reporting patterns, and the capacity of local service providers (sampson2012great, austin311open). An independent comparison of two groups of neighborhoods would have to contend with all of this heterogeneity, which inflates the denominator of the test statistic and makes it harder to detect genuine change. By comparing each neighborhood to itself before and after a change, the paired design removes this between-unit heterogeneity entirely. The only variation that remains is within-unit change over time, which is typically much smaller and more directly relevant to the policy question.

### 2. They reduce error variance

The variance of differences is almost always smaller than the variance of levels:


$$
Var}(D_i) < Var}(X_{i,before}})
+ Var}(X_{i,after}}).
$$


This inequality holds whenever the before and after measurements are positively correlated---which is nearly always the case in administrative data, because a neighborhood that was slow last year tends to be slow this year as well. The reduction in variance translates directly into a larger *t*-statistic for the same mean difference, improving the test's ability to detect real change even in small samples.

### 3. They increase interpretability

Differences provide a clearer causal story than comparing two separate groups---an insight echoed in the causal inference literature (angrist1996identification, freedman2007statisticalmodels). When an analyst reports that the average neighborhood experienced a 2.3-minute improvement in response time, stakeholders can immediately grasp the magnitude and direction of change. By contrast, reporting that Group A's mean was 8.1 minutes while Group B's was 10.4 minutes invites questions about whether the groups were comparable to begin with. The within-unit framing of paired designs aligns naturally with the before-and-after logic that policymakers and managers use when evaluating reforms.


These advantages make paired designs essential for policy evaluation, program assessment, and
performance monitoring under OMB guidelines (ombPerfGuide).


## Assumptions of the Paired *t-Test*

The paired *t*-test has fewer assumptions than its independent counterpart, but three remain
critical:

### 1. Differences are independently sampled

Each unit’s change should not influence another unit’s change. In practice, this means that one neighborhood’s improvement in response time should not mechanically cause a neighboring area to improve or deteriorate. Independence can be violated when resources are reallocated across units---for example, if staffing gains at one EMS station come at the expense of another---or when geographic spillover effects operate, as when a crackdown on one block displaces activity to adjacent blocks. Analysts should consider whether the administrative process that generated the data creates dependencies among the paired differences.

### 2. Differences are approximately normal

Because the Central Limit Theorem applies to averages, moderately sized samples yield robust results even when individual differences are not perfectly normal (ross2014probability). However, administrative differences---particularly in skewed service metrics such as response times or processing durations---may depart substantially from normality in small samples. Graphical inspection in the spirit of Tukey’s EDA approach (tukeyEDA) is essential: a histogram or normal probability plot of the differences can reveal heavy tails, outliers, or asymmetry that would undermine the test’s validity. When normality is severely violated and the sample is small, nonparametric alternatives such as the Wilcoxon signed-rank test provide a more reliable inference.

### 3. Matched pairs are correctly aligned

Misalignment creates misleading inferences, especially in multi-agency data systems where unit identifiers change over time (einav2014datarev). If a city reorganizes its EMS districts between the before and after periods, the ``same’’ station number may refer to a different geographic area, rendering the paired comparison meaningless. Similarly, census tract boundaries are occasionally redrawn between decennial censuses, so tracts that share a FIPS code across two ACS cycles may not cover identical populations. Analysts must verify that the pairing variable genuinely links the same unit across both measurement occasions before computing differences.


> 
**Briefing:** The paired test reduces assumptions—but makes data alignment essential.


## Effect Sizes for Paired Data

Effect size quantifies the magnitude of change.  
The most common measure is:


$$
d = D}}{s_D},
$$


Cohen’s *d* for paired designs.

Interpretation depends on:


    - operational thresholds (e.g., minutes of EMS response time (dshsEMS)),
    - measurement error (ACS margins of error (uscensusACS)),
    - underlying variability in baseline service levels,
    - neighborhood context (sampson2012great).


Cleveland’s visualization principles emphasize showing effect sizes graphically to facilitate
interpretation (clevelandGraphing).


## Applications in Public Administration

### 1. Before-and-After Workflow Reform (311 Requests)

Paired tests evaluate whether the same request categories experienced meaningful improvement after
a workflow redesign (austin311open).

### 2. EMS Response Time Improvements

If the same stations are tracked across periods, paired tests measure within-station change
(dshsEMS).

### 3. Inspection Duration Before and After Digital Forms

This is one of the most common and clearest use cases for paired tests.

### 4. Budget Processing Times Across Fiscal Years

If the same divisions or staff are followed longitudinally, paired tests isolate performance trends.

### 5. ACS Income Changes Over Time at the Census Tract Level

Tracking tracts from one ACS cycle to another yields natural pairs, especially when using margins of
error to quantify uncertainty (uscensusACS).


> 
**Briefing:** Paired tests answer “Did this unit change?” Independent tests answer “Are these units different?”


## Robustness and Model Checking

Following Gelman and Hill’s advice on hierarchical and longitudinal data (gelman2007data),
paired-data diagnostics should examine:


    - histograms of differences (tukeyEDA),
    - symmetric vs. skewed difference distributions,
    - outliers (Anscombe’s warning about summary statistics (anscombe1973graphs)),
    - missingness patterns across time (gaoDataQuality),
    - department- or neighborhood-level clustering.


Freedman cautions that statistical models must align with institutional realities
(freedman2007statisticalmodels).  
Thus, analysts should verify that units are comparable across periods and that changes do not
reflect shifts in reporting rather than operational improvement (einav2014datarev).


## Common Pitfalls

### 1. Treating paired samples as independent

Doing so discards within-unit information and reduces power.

### 2. Ignoring measurement error across periods

Census MOEs, administrative coding shifts, and system upgrades affect comparability
(uscensusACS, gaoDataQuality).


> **Returning to the Case:** The Proposition B homeless counts are vulnerable to exactly this pitfall. Point-in-time counts depend on volunteer availability, weather conditions, and route coverage---all of which may have differed between the pre- and post-ban counts. If the second count used fewer volunteers or occurred during inclement weather, the observed decline in counts might reflect measurement differences rather than a genuine reduction in homelessness. Analysts must assess whether the measurement instrument was held constant across periods before interpreting paired differences.}

### 3. Misaligned pairs

If units shift boundaries (e.g., station reorganizations), comparisons become invalid.

### 4. Using *p-values without effect sizes*

Manski emphasizes the perils of overstating certainty (manski2019policy).  
Effect sizes clarify practical relevance.

### 5. Ignoring neighborhood structure

Differences may reflect broader inequality patterns rather than interventions
(sampson2012great, chetty2016mto).


## Practice and Application


    - Using 311 request data, compute paired differences for completion times before and after a
          workflow reform. Interpret change in the context of administrative process variation
          (austin311open, einav2014datarev).

    - Evaluate EMS response times across two periods using a paired *t*-test.
          Graph the distribution of differences in the spirit of Tukey’s EDA (tukeyEDA).

    - Using ACS median income estimates from two five-year cycles for a tract, compute paired
          differences and incorporate margins of error into interpretation (uscensusACS).

    - For inspection durations, compare paper vs. digital processing for the same inspectors.
          Assess effect size and robustness using graphical diagnostics (clevelandGraphing).

    - Critically evaluate a paired comparison published by a public agency using GAO data-quality
          criteria (gaoDataQuality) and Freedman’s cautions about model assumptions
          (freedman2007statisticalmodels).
    - Using the EMS response time dataset, identify stations that appear in both 2022 and 2023 data. Compute the paired difference in average response time for each station. In Excel, use the Data Analysis ToolPak to run a paired *t*-test. Report results and discuss whether any observed improvement (or decline) could reflect changes in measurement rather than true operational change.


## Transition to Chapter Eight

Paired *t*-tests evaluate within-unit change over time or across conditions.  
But administrators often need to compare more than two periods, more than two conditions, or multiple
groups simultaneously.  
Chapter~*chap:regression* introduces regression analysis, the framework for modeling relationships among multiple variables simultaneously.