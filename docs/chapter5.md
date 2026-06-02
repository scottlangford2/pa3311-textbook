---
layout: page
title: "Chapter 5"
permalink: /docs/chapter5/
---

# Statistical Inference


> **Course dataset & lab.** Work this chapter's techniques on our spine dataset — [Texas City Sales Panel](../datasets). Build a 95% confidence interval for the mean per-capita sales tax (one year).


## Epigraphs


> 
*"Statistics are the triumph of the quantitative method, and the quantitative method is the victory of sterility and death."*

 Hilaire Belloc


> 
*"In God we trust; all others must bring data."*

 W. Edwards Deming


Belloc warns that statistical reasoning—used poorly—produces hollow certainty. Deming counters that
public administration requires evidence, not intuition. This chapter reconciles these views through
the logic of statistical inference: the disciplined process of drawing conclusions from incomplete,
uncertain, and often imperfect administrative data (Einav & Levin 2014; U.S. GAO data-quality guidance).


## Opening Case: Texas Teacher Vacancies and the Data That Could Not Settle the Debate


In 2023, the Texas Tribune reported that school districts across the state were sounding alarms about teacher shortages---but no one could agree on how bad the problem actually was (Texas Tribune 2023). Large urban districts like Houston ISD and Dallas ISD reported vacancy rates of 5--8 percent. Rural districts in West Texas and the Rio Grande Valley reported rates exceeding 15 percent, sometimes for months at a time. Yet the Texas Education Agency's (TEA) statewide figures told a more moderate story, and some legislative analysts questioned whether the crisis was as severe as district leaders claimed.

The disagreements were not primarily political; they were statistical. Districts defined "vacancy" differently: some counted only positions posted for more than 30 days, others included any unfilled position at the start of the school year, and still others counted positions filled by long-term substitutes as vacant. Reporting was voluntary and inconsistent---districts with the most severe shortages were often the least resourced to track and report accurate data. And the numbers themselves were inherently noisy: a rural district with 40 teaching positions reporting a 15 percent vacancy rate had a confidence interval wide enough to encompass rates from 5 to 25 percent.

This case captures the core challenge of statistical inference. The question is not "What do the numbers say?" but "How much should we trust what the numbers say?" The tools introduced in this chapter---sampling distributions, standard errors, confidence intervals, and the logic of inference from imperfect data---are precisely the tools an analyst needs to evaluate competing claims built on administrative data of uneven quality.


**Guiding Questions**


    - If a rural Texas district reports a 15% vacancy rate based on only 40 positions, how confident should we be that the true rate is near 15%?
    - When different districts define "vacancy" differently, what does that mean for the precision of statewide estimates?
    - How does the standard error of a vacancy rate change between a district with 40 positions and one with 4{,}000---and what are the policy implications?


## Why This Chapter Matters

Descriptive statistics summarize what happened, but policy decisions require more:  
*Do the differences we observe reflect real patterns or random noise?*

Public administrators face uncertainty constantly. City 311 call volumes vary by hour and neighborhood (City of Austin open data), EMS response times fluctuate due to staffing levels, weather conditions, and call severity, Census estimates contain margins of error that widen as geographic units shrink (U.S. Census ACS), and budget forecasts must account for volatility in economic conditions and revenue streams (BLS). None of these sources of uncertainty can be eliminated; they are structural features of the systems administrators manage.


Inference provides structured tools to reason about this uncertainty. Without inference, observed differences may be misinterpreted as meaningful when they reflect only noise, routine variation may be mistaken for a trend warranting action, random fluctuations may be mistaken for genuine policy effects, and sampling bias may distort assessments of equity across communities (Sampson 2012). Each of these errors carries real consequences: misallocated resources, premature policy changes, and false conclusions about whether government is serving all residents fairly.

As Manski argues, public institutions often fall prey to the "lure of incredible certitude" when
statistics are interpreted without understanding uncertainty (Manski 2019). Inference
avoids this trap.


> 
**Briefing:** Inference is the process through which data become evidence.


## Populations, Parameters, and Samples

The previous section established that inference matters because administrators must distinguish real patterns from noise. Before we can build the tools to do so, we need precise language for what we are trying to learn and what data we have available to learn it.

A *population* is the full set of units relevant to a question. A *parameter* is a
numerical summary of that population—such as the true mean EMS response time citywide.

A *sample* is the data we actually have, which may differ from the population due to nonresponse, reporting differences across agencies or jurisdictions (U.S. GAO data-quality guidance), neighborhood-level variation in how often residents interact with government systems (Sampson 2012), and the design of administrative data systems themselves (Einav & Levin 2014). These sources of discrepancy are not minor technicalities; they determine whether the sample is a reliable guide to the population or a distorted reflection of it.


Let $\mu$ be the true population mean and $\bar{X}$ the sample mean. Inference concerns how confidently we can use $\bar{X}$ to learn about $\mu$.

Gelman and Hill emphasize that almost all real-world data arise from multilevel structures:
residents nested within neighborhoods, requests nested within departments, and time-series patterns
nested within operational cycles (Gelman & Hill 2007). Recognizing these layers is essential for
interpreting samples correctly.


> 
**Briefing:** All administrative data are samples—sometimes by design, often by accident.


## Sampling Variation

With the distinction between populations and samples in place, we can now address a fundamental consequence of working with samples: no two samples will produce exactly the same result, even when nothing about the population has changed.


Even if two analysts draw samples of equal size from the same population, their results will differ.
This *sampling variation* is not a flaw; it is a lawlike feature of uncertain processes.

Consider a few concrete examples. One week a city department receives 18 pothole complaints; the next week it receives 27---yet nothing about the road system has changed. One sample of 311 completion times yields a median of 2 days, while a second sample drawn from the same period yields a median of 3 days. American Community Survey (ACS) estimates of median household income for a census tract fluctuate from one release to the next, not because incomes have changed but because each release is based on a different random sample of respondents (U.S. Census ACS). Understanding sampling variation prevents overinterpretation of small changes---one of Freedman’s core lessons on statistical skepticism (Freedman 2007).


> 
**Briefing:** Sampling variation is the reason statistics must be interpreted, not merely computed.


## Sampling Distributions

Sampling variation tells us that estimates will differ from sample to sample. The sampling distribution formalizes this idea by describing exactly how much variation to expect and in what pattern.


A sampling distribution is the distribution of a statistic (e.g., the mean) across repeated
hypothetical samples from the population. It provides the foundation for inference.

For a sample mean $\bar{X}$:


$$
\bar{X} \sim \text{Sampling Distribution Centered at } \mu.
$$


Three key insights follow from this idea. First, sampling distributions quantify uncertainty objectively by describing the full range of estimates that a procedure could produce. Second, they explain why repeated samples yield different results---not because something has changed, but because each sample captures a slightly different slice of the population. Third, they justify the standard errors and confidence intervals that analysts use to communicate precision. Tukey’s work on exploratory data analysis emphasized exactly this point: understanding how a statistic behaves across many samples is more informative than fixating on a single dataset (Tukey 1977).

As sample size $n$ grows, the sampling distribution shrinks, reflecting increased precision:


$$
SE(\bar{X}) = \frac{s}{\sqrt{n}}.
$$


This relationship underlies the reliability of federal statistical estimates, including those from
the BLS and Census Bureau (BLS; U.S. Census ACS).


## Standard Error: The Measure of Precision

The sampling distribution tells us that estimates vary across samples; the standard error distills that variation into a single number. It is the practical bridge between the abstract concept of a sampling distribution and the concrete task of communicating how precise an estimate is.


The *standard error* (SE) measures how much a statistic fluctuates due to sampling variation.
It is a fundamental tool for all inference:


$$
SE(\bar{X}) = \frac{s}{\sqrt{n}}.
$$


A small standard error means the estimate is precise---repeated samples would produce similar values. A large standard error indicates substantial uncertainty, signaling that the estimate could shift considerably with a different sample.


The standard error is especially consequential in public-sector settings where sample sizes vary dramatically across units. Estimating average EMS response times in a low-volume rural district with only a few dozen calls per month yields a large SE, making it difficult to benchmark performance with confidence (Texas DSHS EMS data). Comparing median incomes across census tracts requires attention to the SE published alongside each ACS estimate, because tracts with small populations carry wide margins of error (U.S. Census ACS). Tracking departmental performance metrics over short time horizons---a common requirement under Office of Management and Budget (OMB) performance guidelines---also produces small samples and correspondingly large standard errors (U.S. OMB performance guidance). In Gelman and Hill’s multilevel framework, the SE reflects both sampling noise and hierarchical structure, reminding analysts that precision depends not only on sample size but also on how observations are organized across levels of government and geography (Gelman & Hill 2007).


> **Returning to the Case:** The teacher vacancy case makes the standard error tangible. A rural district with $n = 40$ positions reporting a 15% vacancy rate carries a far larger standard error than an urban district with $n = 4{,}000$ positions reporting the same rate. Because the standard error shrinks as the square root of the sample size grows, the small district's estimate could plausibly range from single digits to well over 25%, while the large district's estimate is pinned down tightly. Identical headline rates can therefore reflect very different degrees of certainty.

### Worked Example: Confidence Intervals for Voter Turnout

Suppose we sample turnout rates from 25 Texas counties in a recent general election and observe a mean turnout of $\bar{x} = 58.2\%$ with a sample standard deviation of $s = 9.4$ percentage points. We want a 95% confidence interval for the true mean turnout.

**Step 1: Compute the standard error.**

$$
SE = \frac{s}{\sqrt{n}} = \frac{9.4}{\sqrt{25}} = \frac{9.4}{5} = 1.88\%
$$


**Step 2: Construct a 95% confidence interval.**
Using the approximate critical value $z^* = 1.96$:

$$
\bar{x} \pm z^* \cdot SE = 58.2 \pm 1.96 \times 1.88 = 58.2 \pm 3.7
$$


$$
95\% \text{ CI} = [54.5\%,\ 61.9\%]
$$


**Step 3: Interpret.**
We are 95% confident that the true mean turnout across Texas counties lies between about 54.5% and 61.9%. The interval is wide because the sample of 25 counties is small.


*Figure: A 95% confidence interval for mean county turnout, centered at 58.2% and extending roughly 3.7 percentage points on each side.*


## Confidence Intervals

Standard errors quantify precision, but they are difficult for non-technical audiences to interpret on their own. Confidence intervals translate that precision into a range of plausible values for the parameter, providing a more intuitive way to communicate uncertainty to policymakers and the public.


A 95% confidence interval gives a range of plausible values for the parameter:


$$
\bar{X} \pm 1.96 \cdot SE(\bar{X}).
$$


The correct interpretation requires care. Across repeated sampling, 95% of the intervals constructed this way would contain the true parameter—not that any single interval has a 95% probability of doing so.


Confidence intervals appear throughout public administration practice. Performance benchmarking relies on them to determine whether a district's service times are genuinely slower than the citywide average or merely reflect sampling noise. Equity analysis uses overlapping or non-overlapping intervals to assess whether delay differences across neighborhoods are real or attributable to chance (Sampson 2012; Chetty & Hendren 2016). Budget offices construct intervals around revenue forecasts to communicate the range of expected collections under economic uncertainty (BLS). Federal reporting agencies publish margins of error alongside every ACS estimate precisely because the estimates are derived from samples, not censuses (U.S. Census ACS).

Manski emphasizes that CIs express uncertainty honestly—an antidote to misleading
"incredible certitude" in policy claims (Manski 2019).


> 
**Briefing:** Confidence intervals communicate uncertainty better than point estimates ever can.


## The Logic of a Hypothesis Test

Confidence intervals answer the question "What values of the parameter are plausible?" A closely related question reverses the framing: "Is a specific claimed value plausible at all?" A **hypothesis test** is the formal procedure for answering that question. Rather than estimating where the parameter lies, it asks whether the data are consistent with a particular hypothesized value—and the two approaches, properly applied, always reach the same conclusion.

### The Two Hypotheses

Every test begins with two competing statements about the population. The **null hypothesis** ($H_0$) is the default claim of "no effect" or "no difference"—the status quo we will believe unless the data give us strong reason to abandon it. The **alternative hypothesis** ($H_1$) is the claim we entertain only if the evidence is strong enough. For a question about a single mean, these take the form:

    - $H_0: \mu = \mu_0$ (the population mean equals some specified value),
    - $H_1: \mu \neq \mu_0$ (the population mean differs from that value).

The logic is deliberately conservative: we assume the null is true and ask how surprising our data would be under that assumption. Only genuinely surprising data lead us to reject it.

### The Test Statistic

To measure how far the data fall from the null hypothesis, we compute a **test statistic** that expresses the gap between the observed estimate and the hypothesized value in standard-error units:

$$
t = \frac{\bar{x} - \mu_0}{SE(\bar{x})}.
$$

A test statistic near 0 means the data are close to what the null predicts; a large value (positive or negative) means the data sit far out in the tail of the distribution we would expect if $H_0$ were true.

### The p-Value and Significance Level

The **p-value** is the probability of observing a test statistic at least as extreme as the one we obtained, *assuming the null hypothesis is true*. A small p-value means the data would be very unlikely under $H_0$, which counts as evidence against it. We compare the p-value to a pre-chosen **significance level** $\alpha$—conventionally 0.05—that sets the threshold for "surprising enough." If the p-value is below $\alpha$, we **reject $H_0$**; otherwise we **fail to reject** it. Note that failing to reject is not the same as proving the null true; it simply means the evidence was not strong enough to overturn it.

### Two Ways to Be Wrong

Because we are reasoning under uncertainty, a test can reach the wrong conclusion in two distinct ways. A **Type I error** occurs when we reject a true null hypothesis—a false alarm, declaring an effect that is not really there. Its probability is exactly $\alpha$. A **Type II error** occurs when we fail to reject a false null hypothesis—a missed detection, overlooking a real effect. Choosing a smaller $\alpha$ guards against Type I errors but makes Type II errors more likely, so the threshold reflects a judgment about which mistake is more costly in a given policy setting.

> **Spine dataset.** Suppose a state agency claims that Texas cities collect, on average, \$300 in per-capita sales tax in 2024, and we want to test whether the true mean differs from that figure. Our sample of 1,180 cities has a mean of about \$395, and the standard error of the mean works out to about \$17.64. We state:
>
> $$
> H_0: \mu = 300, \qquad H_1: \mu \neq 300.
> $$
>
> The test statistic is
>
> $$
> t = \frac{395 - 300}{17.64} = 5.39.
> $$
>
> A value of 5.39 is far out in the tail—the corresponding p-value is far below 0.05—so we **reject $H_0$** at $\alpha = 0.05$ and conclude the mean differs from \$300.
>
> This agrees with the confidence-interval approach. The 95% CI for the mean is about $395 \pm 1.96 \times 17.64$, or roughly **[\$361, \$430]**. Because that interval does not contain \$300, we reach the same conclusion: \$300 is not a plausible value for the true mean. A hypothesis test and a confidence interval are two views of the same evidence.


## Inference for Differences Between Groups

So far, we have focused on estimating a single population mean and quantifying its uncertainty. But many of the most consequential questions in public administration involve comparisons: Is one neighborhood served more slowly than another? Did response times improve after a staffing change? These questions require extending the tools of inference to differences between groups.


Suppose we compare mean delays between two neighborhoods:


$$
\Delta = \bar{X}_A - \bar{X}_B.
$$


The standard error of the difference is:


$$
SE(\Delta) = \sqrt{SE(\bar{X}_A)^2 + SE(\bar{X}_B)^2}.
$$


This quantifies whether observed disparities reflect structural inequality—as documented in the
neighborhood effects literature (Sampson 2012; Chetty & Hendren 2016)—or merely noise.

Gelman and Hill note that group comparisons often require hierarchical reasoning because groups may
have different sample sizes and variances (Gelman & Hill 2007). This is common in service
delivery: some neighborhoods generate far more requests than others.


> 
**Briefing:** A difference in means is not evidence of inequality unless it exceeds sampling uncertainty.


## Bias, Representativeness, and Missing Data

The inferential tools developed so far---standard errors, confidence intervals, and comparisons between groups---all rest on the assumption that the sample is a reasonable reflection of the population. When this assumption fails, even technically correct calculations produce misleading results. Administrative data violate this assumption more often than analysts realize, and the violations tend to be systematic rather than random.

Key risks:

### 1. Measurement Error

Measurement error arises when the values recorded in an administrative dataset do not accurately reflect the underlying reality they are supposed to capture. Misclassification and inconsistent coding are among the most common sources: one department may categorize a service request as "resolved" when it is assigned to a crew, while another records it as resolved only after the work is physically completed (Einav & Levin 2014). In EMS data, response times may be measured from the moment a call is dispatched or from the moment it is received, and the choice of starting point can shift average response times by several minutes. Data-entry errors---transposed digits, defaulted date fields, and free-text inconsistencies---accumulate quietly across thousands of records and introduce noise that inflates standard errors and biases estimates in unpredictable directions. The fundamental problem is that measurement error is rarely random; it tends to be systematic, varying by department, by time period, and by the training and workload of the staff entering data. Analysts who treat administrative records as perfectly measured will produce confidence intervals that are misleadingly narrow and point estimates that may be substantially off target.


> **Returning to the Case:** In the teacher vacancy debate, measurement error and non-random missingness compound each other. Districts that define "vacancy" differently introduce systematic measurement error into statewide aggregates. And districts with the most severe shortages---often small, rural, and under-resourced---are the least likely to report complete data. The missing observations are not random; they are correlated with the outcome of interest. Any statewide inference that ignores this selection problem will understate the severity of teacher shortages.

### 2. Non-Random Missingness

Missing data in administrative systems rarely disappear at random. Instead, the gaps in a dataset typically reflect the institutional processes, resource constraints, and organizational incentives that govern data collection (U.S. GAO data-quality guidance). A small rural health clinic that is overwhelmed with patients is less likely to submit timely reports to a state agency than a well-staffed urban hospital, which means the most burdened providers are systematically underrepresented in statewide datasets. In 311 systems, residents who lack internet access or English proficiency may never file a request, so the complaints that appear in the data overrepresent neighborhoods with higher connectivity and language resources. Government Accountability Office (GAO) audits have repeatedly found that federal grant programs suffer from non-random missingness: grantees that struggle with compliance are the same ones least likely to submit performance data on time, creating a dataset that paints an artificially rosy picture of program effectiveness. When missingness is correlated with the outcome of interest, standard statistical procedures---which assume data are missing at random---produce biased estimates and unjustifiably precise confidence intervals.

### 3. Selection Bias

Selection bias occurs when the process that determines which observations enter a dataset is related to the outcome being studied. Neighborhoods differ markedly in how often and how effectively their residents report problems to city government, and these differences correlate with income, education, language, and social capital (Sampson 2012). A city that uses 311 complaint data to allocate road repair resources will systematically underserve neighborhoods where residents are less likely to call, not because those neighborhoods have fewer potholes, but because the reporting mechanism filters out their needs. In program evaluation, selection bias arises when the individuals or units that receive a treatment differ systematically from those that do not: cities that voluntarily adopt a new budgeting practice may already be more fiscally sophisticated, making it impossible to attribute their superior outcomes to the practice alone. Administrative data are particularly vulnerable to selection bias because they are generated by operational processes rather than designed experiments, and analysts who ignore the selection mechanism risk drawing conclusions that reflect who reports rather than what is happening (Einav & Levin 2014).

### 4. Aggregation and Suppression

Aggregation bias arises when summary statistics computed at a higher level of analysis obscure meaningful variation at lower levels. Federal statistical agencies routinely warn that aggregated estimates can hide substantial uncertainty, particularly for small geographic areas or demographic subgroups (U.S. Census ACS). A statewide average EMS response time of 8 minutes may combine urban districts averaging 5 minutes with rural districts averaging 14 minutes, and the aggregate figure communicates neither the disparity nor the uncertainty surrounding each component. Suppression compounds the problem: when cell sizes are small, agencies suppress estimates to protect confidentiality, which removes precisely the observations most relevant to equity analysis. A county-level poverty rate that is suppressed because the sample contains fewer than 50 respondents is missing from the dataset not because poverty is absent but because the sample is too thin to report safely. Analysts who work only with published aggregates inherit these distortions, and any inference drawn from such data must acknowledge that the numbers reflect both the underlying reality and the editorial decisions of the publishing agency.

Freedman warns that statistical models fail dramatically when analysts apply them without attention
to data-generating processes (Freedman 2007).


> 
**Briefing:** You cannot fix a biased sample with better mathematics.


## The Logic of Statistical Evidence

The preceding sections have built the machinery of inference piece by piece: sampling distributions, standard errors, confidence intervals, group comparisons, and the threats posed by bias and missing data. This section steps back to consider the broader logic that unifies these tools---the fundamental question of how analysts distinguish genuine patterns from random noise.


Inference is the disciplined process of distinguishing **signal**---patterns too large to arise from sampling variation---from **noise**---variation due purely to randomness. Every analytical question in public administration ultimately reduces to this distinction: is the pattern we observe in the data real enough to act on, or could it have appeared by chance alone?


Anscombe’s famous quartet illustrates why numerical inference alone is insufficient. Four datasets with identical means, variances, correlations, and regression lines display radically different underlying patterns when graphed (Anscombe 1973). Inference must therefore incorporate both graphical and numerical reasoning---a principle echoed in Cleveland’s foundational work on statistical visualization (Cleveland 1993). Gelman and Hill reinforce this point by emphasizing model checking: analysts should routinely compare theoretical expectations to observed variation and investigate discrepancies rather than accepting model output at face value (Gelman & Hill 2007). The need for formal inference is made more urgent by research from Kahneman and Tversky showing that humans systematically misjudge randomness, seeing patterns in noise and underestimating the role of chance (Kahneman & Tversky 1974). Structured statistical inference corrects these cognitive biases by replacing intuition with probability.


> 
**Briefing:** Inference is a safeguard against intuitive but incorrect interpretations of uncertainty.


## Practice and Application


    - Compute the standard error of mean completion times for three request categories in the
          311 dataset. Discuss how reporting processes shape uncertainty (City of Austin open data; Einav & Levin 2014).

    - Construct 95% confidence intervals for mean delays in two neighborhoods and discuss the results in light
          of neighborhood effects research (Sampson 2012; Chetty & Hendren 2016).

    - Using ACS margins of error for median income (U.S. Census ACS), explain how sampling
          uncertainty affects resource allocation decisions.

    - Compare two time periods (before/after a program). Compute the SE of the difference and
          assess whether changes exceed sampling variation (U.S. OMB performance guidance).

    - Write a memo evaluating the credibility of a claim based on small-sample data. Use GAO
          criteria for data reliability (U.S. GAO data-quality guidance) and Manski’s argument against
          unwarranted certainty (Manski 2019).
    - Download the voter turnout dataset from the [Course Datasets page](../datasets). Select 10 small counties (population under 20,000) and 10 large counties (population over 200,000). For each group, compute the mean turnout rate, standard error, and 95% confidence interval. Compare the widths of the two intervals and write a short note explaining why the small-county interval is wider.


## Sources for Examples in This Chapter


    - Administrative data systems (Einav & Levin 2014).
    - City of Austin 311 data (City of Austin open data).
    - Neighbourhood variation (Sampson 2012; Chetty & Hendren 2016).
    - Federal performance guidance (U.S. OMB performance guidance).
    - Data quality and reliability guidance (U.S. GAO data-quality guidance).
    - ACS and BLS methodological documentation (U.S. Census ACS; BLS).
    - Foundational statistical texts (Tukey 1977; Cleveland 1993; Anscombe 1973;
          Freedman 2007; Gelman & Hill 2007; Manski 2019;
          Casella & Berger 2002; Ross 2014; McElreath 2020).


## Transition to Chapter Six

Inference quantifies uncertainty. The next step is evaluating whether observed patterns—the
differences between groups or the changes over time—are statistically meaningful. Chapter 6
introduces hypothesis testing through the independent *t*-test, the formal framework for distinguishing signal from noise.