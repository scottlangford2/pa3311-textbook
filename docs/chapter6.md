---
layout: page
title: "Chapter 6"
permalink: /docs/chapter6/
---

# Independent *t-Tests*


> **Course dataset & lab.** Work this chapter's techniques on our spine dataset — [Texas City Sales Panel](../datasets). Compare **Metro vs. Non-Metro** cities' per-capita sales tax with an independent-samples t-test.


## Epigraphs


> 
*"It is easy to lie with statistics; it is easier to lie without them."*

 Frederick Mosteller


> 
*"The first principle is that you must not fool yourself—and you are the easiest person to fool."*

 Richard Feynman


Mosteller’s observation reflects a central motivation for hypothesis testing: informal comparisons
can be misleading, especially when human cognitive biases distort interpretation
(Kahneman & Tversky 1974). Feynman’s warning complements this idea—analysts must rely on
formal methods rather than intuition alone. Independent *t*-tests provide a rigorous way to
evaluate whether differences between two groups are meaningful or simply the result of sampling
variation, a foundational concept in statistical inference (Casella & Berger 2002;
Freedman 2007).


## Opening Case: El Paso Libraries and the Peer-City Comparison


In 2023, El Paso library advocates brought data to the city council showing that El Paso's public library branches averaged roughly 42 hours per week of open time---substantially fewer than branches in peer cities of comparable population, including Tucson, Albuquerque, Memphis, and Oklahoma City, which averaged approximately 48 hours per week (El Paso Times). The advocates argued that El Paso residents were being underserved and that the gap demanded a budget response.

City officials pushed back on two fronts. First, they argued that staffing constraints and cost-of-living differences made direct comparisons misleading. Second, they questioned whether the six-hour difference was meaningful or simply reflected normal city-to-city variation---the kind of gap that might appear even if El Paso's libraries were funded at the same level as its peers. The debate, in other words, was not about the numbers themselves but about whether the observed difference exceeded what one would expect from ordinary variation across cities.

This is precisely the question an independent *t*-test is designed to answer. Given two groups---El Paso branches and peer-city branches---and a continuous outcome---weekly open hours---the test evaluates whether the observed gap is large enough, relative to the variation within each group, to reject the possibility that it arose by chance. The case also raises the distinction between statistical significance and practical significance: even if the gap is statistically detectable, a six-hour difference per branch per week must be evaluated in terms of its operational and budgetary implications.


**Guiding Questions**


    - If El Paso branches average 42 hours/week and peer-city branches average 48 hours/week, is this difference statistically meaningful---or could it reflect normal city-to-city variation?
    - What assumptions must hold for an independent *t*-test to validly compare these two groups?
    - Even if the difference is statistically significant, how would you assess whether it is practically significant for policy decisions?


## Why This Chapter Matters

Group comparisons are ubiquitous in public administration:


    - Do two neighborhoods experience different average 311 completion times? (City of Austin open data)
    - Are EMS response times slower in rural than urban districts? (Texas DSHS EMS data)
    - Do renter-majority neighborhoods face longer delays than owner-majority ones?
    - Did a staffing reform reduce average processing time compared to the previous year?
    - Do ACS estimates of income differ across two census tracts? (U.S. Census ACS)


But descriptive differences alone cannot answer these questions. Sampling variation (Chapter 5)
ensures that two sample means will differ even when population means are equal
(Ross 2014). Independent *t*-tests formalize the comparison by quantifying
how large the observed difference is relative to what we would expect by chance.

Gelman and Hill stress the centrality of such comparisons across levels of government and public
service delivery (Gelman & Hill 2007), while Freedman warns that naïve comparisons may produce
misleading conclusions if uncertainty is ignored (Freedman 2007).


> 
**Briefing:** The independent *t*-test protects analysts from mistaking noise for policy-relevant difference.


## The One-Sample t-Test

Before comparing two groups to each other, analysts often need to compare a single group against a fixed benchmark. The one-sample *t*-test asks whether the mean of one group differs from a predetermined value $\mu_0$---a statutory target, a budget threshold, a service standard, or a peer-group average treated as a fixed reference point. This is the simplest hypothesis test, and it is the natural starting point before the two-sample machinery developed in the rest of this chapter.

The hypotheses compare the population mean to the benchmark:

$$
H_0: \mu = \mu_0 \qquad \text{vs.} \qquad H_1: \mu \ne \mu_0.
$$

The test statistic measures how many standard errors the sample mean $\bar{x}$ sits away from the benchmark:

$$t=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}$$

Here $s$ is the sample standard deviation and $n$ is the sample size, so $s/\sqrt{n}$ is the standard error of the mean. If $|t|$ is large relative to the *t* distribution with $n-1$ degrees of freedom, we reject $H_0$ and conclude the group mean differs from the benchmark.

**Doing it in Excel.** There is no single one-sample function in Excel, but two approaches work. The first is to create a new column equal to each observation minus the benchmark, then run `=T.TEST(diff_range, constant_range, 2, 1)` against a column filled with zeros---this tests whether the differences average to zero, which is equivalent to testing whether the original values average to $\mu_0$. The second, more transparent approach is to compute $t$ by hand from `=AVERAGE()`, `=STDEV.S()`, and `=COUNT()`, then convert it to a two-tailed *p*-value with `=T.DIST.2T(ABS(t), n-1)`.

**Spine tie: do Metro cities clear a \$300 benchmark?**
Our [Texas City Sales Panel](../datasets) covers 1,180 Texas cities' sales tax collections. Suppose a state policy discussion proposes \$300 in per-capita sales tax as a rough benchmark for a fiscally healthy mid-size city. We can ask whether the mean 2024 per-capita sales tax among Metro cities differs from that \$300 figure. Metro cities average about \$438 per capita; with the variation observed across those cities, the one-sample statistic comes out to roughly

$$t=\frac{438-300}{s/\sqrt{n}}\approx 5.6,$$

which is far beyond any conventional critical value, so we reject $H_0$: Metro cities' mean per-capita sales tax is statistically distinguishable from \$300.

A practical-versus-statistical-significance note belongs here. With 1,180 cities, the sample size is so large that even small departures from a benchmark will register as "statistically significant." The reason we reject $H_0$ in this case is not merely the large sample, however---the gap itself is substantial, roughly \$138 per capita, or about 46% above the benchmark. Analysts should always pair the *t*-statistic with the size of the gap: a statistically significant difference of a few cents per capita would tell a policymaker very little, whereas a \$138 gap is large enough to matter for budgeting regardless of the *p*-value.


## What an Independent *t-Test Does*

An independent *t*-test evaluates whether two population means are equal:


$$
H_0: \mu_A = \mu_B \qquad \text{vs.} \qquad H_1: \mu_A \ne \mu_B.
$$


The logic mirrors the structure of classical hypothesis testing described by Casella and Berger
(Casella & Berger 2002): compare an observed statistic to its sampling distribution under the
null hypothesis. If the observed difference exceeds what the null predicts, we reject $H_0$.

Administrative examples include:


    - comparing completion times across neighborhoods,
    - assessing whether a new operational unit is faster than the old,
    - comparing service performance across demographic groups (with care for representativeness),
    - evaluating the impact of a pilot program on processing delays.


Freedman emphasizes that such tests must be grounded in realistic assumptions about how the data
were generated (Freedman 2007). Administrative datasets rarely arise from
random sampling, so analysts must interpret results within institutional
context.


## The Formula and Its Intuition

Let $\bar{X}_A$ and $\bar{X}_B$ be the sample means of Groups A and B. Their difference is:


$$
\Delta = \bar{X}_A - \bar{X}_B.
$$


The key question is:  
*Is this difference large relative to the noise expected under sampling variation?*

The standard error of the difference is:


$$SE(\Delta)=\sqrt{\frac{s_A^2}{n_A}+\frac{s_B^2}{n_B}}$$


The *t*-statistic is:


$$t=\frac{\Delta}{SE(\Delta)}$$


This structure embodies Freedman's argument that inference depends on comparing observed effects to
expected variation (Freedman 2007).

For unequal variances, Welch’s test adjusts degrees of freedom, improving robustness—especially
important in public-sector contexts where neighborhoods differ in size, variance, and reporting
rates.


> 
**Briefing:** A difference is meaningful only when benchmarked against its expected variability.


### Worked Example: Comparing Library Hours in El Paso vs.\ Peer Cities

Suppose we collect weekly open hours for 12 El Paso library branches and 15 branches from peer cities:


| Group | $n$ | Mean hours/week | Std. dev. |
|---|---|---|---|
| El Paso branches | 12 | 42.3 | 4.8 |
| Peer-city branches | 15 | 48.1 | 5.2 |


**Step 1: State the hypotheses.**

$$
\mu_{\text{EP}} = \mu_{\text{Peer}} \qquad H_1: \mu_{\text{EP}} \neq \mu_{\text{Peer}}
$$


**Step 2: Compute the standard error of the difference.**

$$SE(\Delta)=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}=\sqrt{\frac{4.8^2}{12}+\frac{5.2^2}{15}}=\sqrt{\frac{23.04}{12}+\frac{27.04}{15}}=\sqrt{1.92+1.80}=\sqrt{3.72}=1.93$$


**Step 3: Compute the $t$-statistic.**

$$t=\frac{\bar{x}_1-\bar{x}_2}{SE(\Delta)}=\frac{42.3-48.1}{1.93}=\frac{-5.8}{1.93}=-3.01$$


**Step 4: Determine the $p$-value.**
With approximately 24 degrees of freedom (Welch's approximation), $|t| = 3.01$ yields $p \approx 0.006$. This is below the conventional $\alpha = 0.05$ threshold, so we reject $H_0$. In Excel, use `=T.TEST(range1, range2, 2, 3)` for a two-tailed Welch's test.

**Step 5: Compute Cohen's $d$.**

$$d=\frac{|\bar{x}_1-\bar{x}_2|}{s_{\text{pooled}}}=\frac{5.8}{5.0}=1.16$$

This is a *large* effect size by conventional standards ($d > 0.8$).

**Interpretation.**
El Paso library branches are open approximately 5.8 fewer hours per week than peer-city branches, and this difference is both statistically significant ($p = 0.006$) and practically large ($d = 1.16$). A city council reviewing these numbers has evidence that the gap exceeds normal city-to-city variation.


*Figure: Side-by-side box plots of weekly open hours for El Paso and peer-city branches would display both the central gap and the overlap in distributions.*


## Assumptions of the Independent *t-Test*

Hypothesis tests are meaningful only when their assumptions reflect the data-generating process
(Freedman 2007).

### 1. Independence Between Groups

The independence assumption requires that observations in one group do not influence observations in the other. In concrete terms, a 311 completion time recorded in Neighborhood A should have no effect on a completion time recorded in Neighborhood B. This assumption matters because the *t*-test’s standard error formula treats the two groups as unrelated sources of information; if the groups are correlated, the formula underestimates uncertainty and produces artificially small *p*-values. Independence can fail in several administrative settings: departments that coordinate responses across districts create shared workload effects, neighborhoods that draw from the same pool of maintenance crews are linked by resource constraints, and citywide shocks such as severe weather or budget freezes affect all units simultaneously. To check this assumption, analysts should consider whether the data-generating process creates connections between the groups---shared staffing, shared budgets, or shared external shocks. In Excel, there is no direct test for independence; the check is conceptual, based on knowledge of how the data were produced.

### 2. Approximately Normal Sampling Distribution

The *t*-test assumes that the sampling distribution of each group mean is approximately normal. By the Central Limit Theorem, this assumption is often satisfied even when the underlying data are skewed, provided the sample sizes are reasonably large (Ross 2014). However, administrative response times and completion times frequently exhibit heavy right tails---most requests are handled quickly, but a small number take weeks or months due to institutional bottlenecks (City of Austin open data). When samples are small (under 30 observations per group) and the data are strongly skewed, the normal approximation may not hold, and the *t*-test may produce unreliable results. To check this assumption, analysts should examine histograms or box plots of each group’s data in Excel, looking for extreme skewness or outliers. If the distribution is severely non-normal and the sample is small, a nonparametric alternative such as the Mann-Whitney U test provides a more defensible comparison.

### 3. Equal Variances (Pooled Version Only)

The classical (pooled) *t*-test assumes that both groups have the same population variance. This assumption allows the test to combine the two groups’ variability into a single pooled estimate, which increases statistical power when the assumption is correct. However, in public administration, groups almost always differ in variability: high-volume urban districts produce more variable service times than low-volume rural ones, and departments with complex caseloads generate wider spreads than those with routine processing. When variances are unequal and the pooled test is used, the resulting *p*-value can be either too liberal or too conservative, depending on the relationship between sample sizes and variances. In practice, Welch’s test---which does not assume equal variances---is more robust and is recommended by both Gelman and Hill and the broader statistical literature (Gelman & Hill 2007; Casella & Berger 2002). In Excel, the Data Analysis ToolPak offers both versions; select "t-Test: Two-Sample Assuming Unequal Variances" for Welch’s test, which should be the default choice unless there is strong reason to believe variances are equal.

### 4. Representative Samples

The *t*-test, like all inferential procedures, assumes that the samples used in the analysis reflect the populations they are intended to represent. If the data are drawn from a biased or incomplete source, the test may yield a statistically significant result that applies only to the observed data, not to the broader population of interest. GAO audits and ACS documentation repeatedly warn that administrative and survey samples often exhibit systematic bias: voluntary reporting systems underrepresent units that lack resources, 311 data overrepresent neighborhoods with higher digital access, and performance databases may exclude cases that were never formally opened in the tracking system (U.S. Census ACS). To check this assumption, analysts should ask whether the observations in each group were selected by a process that could introduce systematic differences between the sample and the population. If representativeness is questionable, the *t*-test result should be interpreted as descriptive of the available data rather than generalizable to the full population.


> 
**Briefing:** Inference is valid only when the analyst respects the data’s origins.


## The Logic of the *p-Value*

A *p*-value represents:


$$
P(\text{observing a difference at least this large}\mid H_0\text{ is true}).
$$


Crucially, a *p*-value is not the probability that $H_0$ is true, nor is it the probability that the observed difference is meaningful, nor is it an indicator of effect size. These three misconceptions are among the most persistent in applied statistics, and each leads to a different kind of analytical error. Kahneman and Tversky show that people tend to misinterpret probabilities systematically, often treating a small *p*-value as definitive proof that an effect is large and important (Kahneman & Tversky 1974). Formal hypothesis testing helps counteract these biases by imposing a structured decision rule, but it does not eliminate the need for judgment. Analysts often overstate the certainty implied by small *p*-values, treating statistical significance as a substitute for substantive reasoning. Responsible analysis requires considering the context in which the data were generated, the magnitude of the observed effect, and the uncertainty surrounding the estimate---not merely whether the *p*-value falls below a threshold.


> 
**Briefing:** A small *p*-value indicates evidence against $H_0$—not evidence for a large or important effect.


## Effect Sizes and Practical Significance

Statistical significance does not imply policy relevance.

Effect size for independent samples is:


$$d=\frac{\bar{X}_A-\bar{X}_B}{s_{\text{pooled}}}$$


Interpretation of effect size must consider the specific operational context in which the difference matters. Two minutes of EMS response time may appear small in a statistical summary but can be the difference between life and death in a cardiac emergency. Small average differences in service delivery may mask large subgroup disparities---an overall gap of half a day in 311 completion times might conceal a two-day gap for specific request types in specific neighborhoods. Measurement error in both administrative and survey systems can inflate or deflate effect sizes in ways that are difficult to detect without careful data auditing (U.S. Census ACS). Finally, institutional context shapes interpretation: a moderate effect size in a setting characterized by systemic neighborhood inequality may carry far greater policy significance than a large effect size in a setting where the baseline is already equitable.


> **Returning to the Case:** In the El Paso library case, the observed difference is approximately 6 hours per week per branch. Even if a *t*-test confirms this gap is statistically significant, the policy question remains: what does 6 fewer hours mean operationally? For a branch that serves a low-income neighborhood where residents rely on the library for internet access, job applications, and after-school programs, 6 hours may represent the difference between adequate and inadequate service. For a branch in a neighborhood with high home internet penetration, the same gap may matter less. Effect size must be interpreted through the lens of the communities affected.

Graphical analysis clarifies practical significance by
displaying effect magnitude and distributional shape.


## Applications in Public Administration

### 1. 311 Completion Times Across Neighborhoods

When city managers examine 311 service request data, they frequently discover that average completion times differ across neighborhoods. Some areas see requests resolved in two or three days, while others wait a week or more. These persistent differences may signal structural inequities in how city resources are allocated. However, descriptive differences alone cannot distinguish genuine disparities from sampling noise. An independent *t*-test provides the formal assessment: if the gap between two neighborhoods’ mean completion times exceeds what sampling variation would predict, the analyst has evidence of a real difference that warrants investigation into root causes such as staffing patterns, geographic distance from service depots, or the complexity of requests in each area.

### 2. EMS Response Times: Urban vs. Rural

Performance evaluation under OMB guidelines often requires comparing mean response times across districts to determine whether service standards are being met equitably. Urban EMS districts, with shorter distances and more available units, typically report faster average response times than rural districts, where longer travel distances and fewer ambulances produce slower averages. An independent *t*-test provides a principled basis for determining whether the observed urban-rural gap is large enough to constitute a statistically meaningful difference or whether it falls within the range of normal variation. Analysts should use Welch’s version of the test, since urban and rural districts almost certainly differ in variability as well as in means, and should supplement the statistical result with a discussion of whether the observed gap has operational significance for patient outcomes.

### 3. Budget Processing Times Before vs. After Reform

When a government agency implements a process reform---such as a new electronic procurement system or a streamlined approval workflow---managers want to know whether the reform actually reduced processing times. If the reform was implemented at a single point in time and the analyst has data on cases processed before and after that date, the two cohorts of cases are independent (different invoices, different requisitions), making the independent *t*-test the appropriate tool. The test evaluates whether the post-reform cohort’s mean processing time is significantly lower than the pre-reform cohort’s, accounting for the natural variation in how long individual cases take. Analysts should be cautious about confounding factors---seasonal budget cycles, staffing changes, or shifts in case complexity---that might explain the difference independently of the reform itself.

### 4. Census Measures of Income Across Tracts

The ACS publishes median household income estimates for individual census tracts, each accompanied by a margin of error that reflects the uncertainty inherent in small-area estimation (U.S. Census ACS). When analysts compare incomes across two tracts to assess economic disparities or target program resources, they must account for this uncertainty. An independent *t*-test can formalize the comparison, but it should be supplemented with MOE-aware interpretation: two tracts whose confidence intervals overlap substantially may not differ in any meaningful sense, even if their point estimates appear several thousand dollars apart. Treating ACS estimates as exact values---a common error in municipal planning---overstates the precision of the comparison and can lead to misallocation of resources.

### 5. Contracted vs. In-House Inspection Durations

Local governments frequently debate whether to contract out inspection services or keep them in-house. One way to inform this decision is to compare the average duration of inspections completed by contracted firms versus in-house staff. Because contracted and in-house inspectors often differ in training, caseload, and the types of inspections they handle, the two groups typically exhibit different variances in addition to different means. Welch’s *t*-test is the appropriate choice in this context, consistent with Gelman and Hill’s emphasis on accounting for hierarchical heterogeneity (Gelman & Hill 2007). Beyond the statistical comparison, analysts should consider whether the two groups handle comparable cases, since differences in inspection duration may reflect case mix rather than efficiency.


## Robustness and Model Checking

Statistical modeling must be evaluated using diagnostics. Following Gelman and Hill (Gelman & Hill 2007) and Freedman (Freedman 2007), analysts should begin by examining graphical summaries---histograms, box plots, and density plots---for each group to identify skewness and outliers that could distort the test. They should then assess whether the two groups exhibit similar variances, either through visual inspection of side-by-side box plots or through a formal test such as the F-test for equality of variances (available in Excel's Data Analysis ToolPak). Sample-size imbalance deserves attention because when one group is much larger than the other, the test's sensitivity to departures from normality and equal variance increases. Patterns in missing data should also be investigated: if one group has substantially more missing observations than the other, the comparison may be biased toward the group with more complete records. Finally, analysts should consider whether the data cluster at organizational or neighborhood levels, since observations within a single department or geographic area are often more similar to each other than to observations elsewhere. Anscombe's famous quartet demonstrates why these checks matter: identical summary statistics can mask dramatically different data patterns, underscoring the need to combine numerical inference with careful graphical inspection.


## Common Pitfalls

### 1. Confusing statistical significance with importance

Analysts often overstate the certainty of small differences.

### 2. Assuming equal variances

When groups differ systematically—common in neighborhood or departmental comparisons—Welch’s test
should be used.

### 3. Ignoring sampling design

ACS and BLS estimates require attention to margins of error and design effects (U.S. Census ACS; BLS).

### 4. Treating administrative data as random samples

Administrative data have selection mechanisms, reporting bias, and structural missingness.

### 5. Overreliance on *p-values*

Interpretation requires examining effect size, uncertainty, and practical relevance.


## Practice and Application


    - Compare 311 completion times across two neighborhoods using Welch’s *t*-test.
          Use graphical diagnostics to examine skewness (City of Austin open data).

    - Evaluate whether EMS response times differ between two districts.
          Assess both statistical and operational significance (Texas DSHS EMS data).

    - Using ACS median income estimates for two census tracts, compute the independent
          *t*-test while incorporating margins of error (U.S. Census ACS).

    - Compare processing times before and after a staffing reform (independent samples).
          Interpret results using the conceptual framework of sampling variance
          (Casella & Berger 2002; Freedman 2007).

    - Evaluate the reliability of a published group comparison using GAO criteria for
          data integrity, and critique claims of certainty about small differences.
    - Using the EMS response time dataset from the [Course Datasets page](../datasets), separate incidents into rural and urban groups. In Excel, use the Data Analysis ToolPak to run an independent *t*-test (two-sample assuming unequal variances). Report the $t$-statistic, $p$-value, and compute Cohen’s $d$ by hand. Write a three-sentence interpretation: Is the difference statistically significant? Is it practically meaningful? What would you recommend to a county administrator?


## Transition to Chapter Seven

Independent *t*-tests allow analysts to compare two groups.  
Many administrative questions, however, involve more than two categories—multiple neighborhoods,
districts, or policy treatments.  
Chapter 7 introduces paired *t*-tests, which compare two measurements taken on the *same* units---before and after a policy change, or across two time points---isolating within-unit change.