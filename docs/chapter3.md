---
layout: page
title: "Chapter 3"
permalink: /docs/chapter3/
---

# Describing Data


> **Course dataset & lab.** Work this chapter's techniques on our spine dataset — [Texas City Sales Panel](../datasets). Describe the 2024 distribution of `sales_tax_alloc_per_capita` (filter `year`): histogram, mean vs. median, outliers.


## Epigraphs


> 
*"The first step toward wisdom is calling things by their right names."*

 Confucius


> 
*"If you torture the data long enough, it will confess to anything."*

 Ronald Coase


These observations capture the spirit of descriptive statistics. Good descriptive work depends on
clear definitions, careful measurement, and a disciplined respect for what data can and cannot
show. As Einstein noted, the formulation of a problem is often more critical than its solution
(einsteinIdeas). Describing data is the act of defining problems correctly.


## Opening Case: Houston's 911 Call Center and the Number That Hid a Crisis


In 2022, the Houston Chronicle reported that the city's Houston Emergency Center (HEC) was hemorrhaging staff. Dispatchers were leaving faster than the city could replace them, and the consequences showed up in a statistic that should have alarmed every city official: the 911 call abandonment rate---the share of callers who hung up before reaching a dispatcher---had climbed to roughly 12 percent systemwide (chronicleHEC911). City leaders acknowledged the problem and pointed to hiring initiatives, but the single figure obscured a more troubling pattern.

Beneath the system-wide average, the data revealed enormous variation by time of day and day of week. Daytime weekday shifts, when staffing was closest to full strength, posted abandonment rates near 5 percent. Overnight and weekend shifts---when the fewest dispatchers were on duty and call volumes spiked with bar closings, domestic disturbances, and medical emergencies---saw abandonment rates approach 25 percent. A single mean of 12 percent described a system with two very different realities: one that functioned adequately and one in severe distress.

This case illustrates a foundational principle of descriptive statistics: a summary number is only as useful as the distributional structure it represents. The tools introduced in this chapter---measures of central tendency, variation, percentiles, and graphical display---exist precisely to prevent the kind of false reassurance that a single average can create.


**Guiding Questions**


    - If Houston reports an average 911 call abandonment rate of 12%
    - What graphical tools would reveal whether the abandonment problem is concentrated at specific times or spread evenly across the week?
    - How might the distribution of hold times differ from the distribution of abandonment rates, and why does the distinction matter for staffing decisions?


## Why This Chapter Matters

Descriptive statistics are the backbone of analytical practice in public administration. Before a
city manager can evaluate responsiveness, before a budget officer can assess fiscal risk, and
before a policy analyst can examine equity, they must understand the patterns in the underlying
data. This requirement is especially important in administrative datasets, which are generated
through complex institutional processes rather than designed studies.

As Einav and Levin note, modern administrative data emerge from operational systems, workflows,
and reporting technologies—not from controlled experiments (einav2014datarev). This makes
careful description essential: analysts must identify how observations cluster, vary, or deviate
before drawing conclusions.

Similarly, neighborhood-level differences in public services—documented extensively in urban
research (sampson2012great,chetty2016mto)—are visible only when descriptive statistics are
used to compare groups, distributions, and extremes.


> 
**Briefing:** Clear description prevents analytical overreach and ensures that later techniques
build on a solid empirical foundation.


## What It Means To Describe Data

To describe data is to turn thousands of observations into a coherent picture. For example, the
City of Austin’s 311 dataset contains timestamps, categories, and departmental assignments
(austin311open). On their own, these records say little. But with descriptive tools—means,
medians, percentiles, and graphs—they begin to reveal:


    - typical experiences,
    - sources of delay,
    - seasonal trends,
    - and inequities across neighborhoods.


These descriptive structures form the empirical baseline for understanding how services operate.
Without them, interpretation becomes guesswork.

Moreover, because administrative data reflect institutional rules and behaviors (einav2014datarev),
analysts must describe not only the values themselves but also the patterns those values betray:
clustering, skewness, outliers, or stability over time.


> 
**Briefing:** Description converts administrative records into interpretable evidence.


## The Structure of Distributions

A distribution summarizes how often particular values occur. Public-sector data rarely resemble
the idealized bell curve. Instead, their shapes reflect the operational systems that produced
them—an insight emphasized in studies of neighborhood variation and institutional systems
(sampson2012great).

### Skewed Distributions in Public Data

311 request completion times, EMS response delays, and capital project durations often exhibit
long right tails: many events occur quickly, but a handful take much longer due to coordination
issues, data-entry delays, or resource constraints (austin311open).

Such skewness is typical in administrative data because organizations triage work: easy tasks are
completed rapidly, while difficult tasks accumulate.

### Multimodality

Multimodal distributions—which exhibit multiple peaks—often reflect subpopulations or distinct
institutional processes. Research on neighborhood effects emphasizes that urban patterns often
reflect overlapping social structures (sampson2012great). Similarly, service request data may
contain morning and evening peaks, or weekday and weekend regimes.

Recognizing this structure is essential for understanding the populations being served---not a single
"average citizen," but groups with different needs and behaviors.


> **Returning to the Case:** A histogram of Houston 911 call abandonment rates by shift would likely show exactly this kind of multimodal structure: a cluster of low rates during well-staffed daytime shifts and a second cluster of high rates during overnight and weekend shifts. The system-wide mean of 12%


## Measures of Central Tendency

### Mean

The mean:


$$
x} = 1}{n}\sum_{i=1}^n x_i
$$


is intuitive but sensitive to outliers—a recurring challenge in administrative datasets. For
example, a single delayed request due to interdepartmental coordination may inflate the mean
dramatically (austin311open).

### Median

The median, by contrast, is robust to outliers and captures the typical experience more reliably.
This distinction is crucial in assessing neighborhood effects, where extreme values may distort
aggregated metrics (sampson2012great).


> **Returning to the Case:** In the Houston 911 case, the mean abandonment rate of 12%

### Mode

The mode is most useful for understanding categorical patterns, such as identifying which request
types dominate the workload---information vital for resource allocation. In a 311 dataset, the modal category might be code compliance or street maintenance, indicating where the largest share of staff time and resources is directed. For continuous variables, the mode is less informative than the mean or median, but for categorical data it provides a quick answer to the question "What is the most common type?"---a question that city managers ask frequently when setting priorities or justifying budget requests.


> 
**Briefing:** In administrative data, the median usually answers the managerial question; the
mean answers the accounting question.


### Worked Example: EMS Response Times in Two Counties

Consider response times (in minutes) for 10 recent EMS calls in two Texas counties:


*[Table — see PDF version]*


**Step 1: Compute the mean.**

$$
x}_A = 7+8+8+9+9+10+10+11+12+36}{10} = 120}{10} = 12.0  minutes}
$$


$$
x}_B = 6+9+10+11+12+12+13+14+15+18}{10} = 120}{10} = 12.0  minutes}
$$

Both counties have the same mean: 12.0 minutes.

**Step 2: Compute the median.**
With 10 observations, the median is the average of the 5th and 6th values (when sorted):

$$
Median}_A = 9 + 10}{2} = 9.5  minutes} \qquad
Median}_B = 12 + 12}{2} = 12.0  minutes}
$$

County A's median is 2.5 minutes lower than its mean---the mean is pulled upward by the single 36-minute outlier (likely a rural call with extended travel distance). County B's mean and median are identical, indicating a symmetric distribution.

**Step 3: Visualize.**
A histogram reveals the structure the mean conceals:


*[Figure — see PDF version]*


**Interpretation.** A city manager reviewing only the mean would conclude that these two counties perform identically. The median and histogram tell a different story: County A's typical response is faster (9.5 minutes), but it has a severe outlier problem. County B is consistently slower but more predictable. These are different operational challenges requiring different policy responses.


## Measures of Variation

Variation describes how spread out the data are and is essential for diagnosing systemic stress,
inequity, or instability. Areas with high variation in service delays, for example, often mirror
patterns identified in neighborhood-based studies (sampson2012great).

### Variance and Standard Deviation (SD)

Variance:


$$
s^2 = 1}{n-1}\sum_{i=1}^n (x_i - x})^2
$$


and standard deviation:


$$
s = s^2}
$$


highlight average deviation from the mean, though they are most interpretable when the mean itself
is meaningful—an assumption that frequently fails in skewed data.

### Interquartile Range (IQR)

The IQR:


$$
IQR} = Q_3 - Q_1
$$


captures the middle 50%
or long tails, such as 311 service times (austin311open).

### Range

Though simple, the range often signals data quality issues or neighborhood-level disparities
(sampson2012great) — especially when extreme values cluster in specific geographic areas.

### Worked Example: Variation in County A vs.\ County B

Using the same EMS data from the central tendency example:

**Standard Deviation.**
For County A ($x} = 12.0$):

$$
s_A^2 = (7-12)^2 + (8-12)^2 + \cdots + (36-12)^2}{9} = 690}{9} = 76.7 \quad \Rightarrow \quad s_A = 8.8  min}
$$

For County B ($x} = 12.0$):

$$
s_B^2 = (6-12)^2 + (9-12)^2 + \cdots + (18-12)^2}{9} = 102}{9} = 11.3 \quad \Rightarrow \quad s_B = 3.4  min}
$$

County A's standard deviation is nearly three times larger---driven almost entirely by the 36-minute outlier.

**IQR.**
For County A: $Q_1 = 8, \; Q_3 = 11$, so $IQR}_A = 3$ minutes.

For County B: $Q_1 = 10, \; Q_3 = 14$, so $IQR}_B = 4$ minutes.

The IQR tells a different story than the standard deviation. County B has a wider middle range (4 vs.\ 3 minutes), but County A has far more extreme variation. The IQR is robust to outliers; the standard deviation is not. In Excel, use `=STDEV.S()` for standard deviation and `=QUARTILE.INC()` for quartiles.


*[Figure — see PDF version]*


## Percentiles and Outliers

Percentiles translate data into operational standards. For example, a department might aim to
resolve 90%

This logic echoes how neighborhood experts interpret distribution tails when assessing mobility
outcomes (chetty2016mto).

### Outliers

Outliers may signal rare but critical administrative failures. In service datasets, these values
often reflect the structural features of administrative systems emphasized in the literature on
urban inequality (sampson2012great).

Rather than removing outliers reflexively, analysts should interpret them in context:


    - Are they due to missing data?
    - Do they reflect unusual events?
    - Are they concentrated in particular neighborhoods?


This last question directly connects descriptive statistics to broader structural inequities, as
highlighted by neighborhood studies.


> 
**Briefing:** Outliers often reveal the institutional story behind the data.


## Graphical Description

Visualization serves as a descriptive complement to numerical summaries. Because administrative data often come from disparate sources and processes (einav2014datarev), graphics reveal structure that numbers alone may obscure. As Tufte argues, the best statistical graphics communicate complex quantitative information with clarity, precision, and efficiency (tufte2001visual). In public administration, where analysts present findings to city managers, council members, and budget officers who may not read regression output, the ability to construct and interpret graphs is not optional---it is a core professional skill.

### Histograms

A histogram divides a continuous variable into equal-width bins and displays the count or proportion of observations in each bin as a bar. The shape of the histogram reveals the distribution's central tendency, spread, and skewness at a glance. In administrative data, histograms are particularly valuable because operational processes frequently produce right-skewed distributions: most service requests are completed quickly, but a long right tail captures the requests that stall due to coordination failures, resource shortages, or data-entry backlogs. An analyst examining EMS response times, for example, would use a histogram to determine whether the distribution is approximately symmetric (suggesting consistent performance) or heavily skewed (suggesting a subset of calls with serious delays). When building histograms in Excel, use the Data Analysis ToolPak or the `FREQUENCY()` function, and choose bin widths that balance detail against readability---too few bins obscure patterns; too many create noise.


*[Figure — see PDF version]*


### Boxplots

A boxplot (or box-and-whisker plot) displays the five-number summary---minimum, first quartile ($Q_1$), median, third quartile ($Q_3$), and maximum---in a compact visual format. The box spans the IQR, the line inside the box marks the median, and whiskers extend to the most extreme observations within 1.5 times the IQR. Points beyond the whiskers are plotted individually as potential outliers. Boxplots are especially powerful for comparing groups side by side: placing urban, suburban, and rural EMS response times in adjacent boxplots immediately reveals whether the distributions overlap or separate, whether one group has greater variability, and whether outliers concentrate in a particular category. Research on neighborhood inequality has shown that such group comparisons often reveal systemic disparities invisible in aggregate statistics (sampson2012great). In Excel, boxplots are available under Insert $>$ Chart $>$ Box and Whisker (Excel 2016 or later).


*[Figure — see PDF version]*


### Line Charts

Line charts connect observations over time, making them ideal for identifying trends, seasonal cycles, and structural breaks in administrative data. A line chart of monthly 311 request volumes, for instance, might reveal a summer peak driven by infrastructure complaints (potholes after winter, air conditioning failures) and a winter trough when residents spend less time outdoors. Overlaying multiple lines---one for each department or neighborhood---can expose divergent trends that an aggregate line would mask. Line charts also make reporting anomalies visible: a sudden spike or drop often reflects a change in data collection rather than a change in the underlying process, a distinction emphasized in the literature on administrative data quality (einav2014datarev, gaoDataQuality). When constructing line charts, label axes clearly, avoid cluttering with more than 4--5 lines, and consider whether a change in scale or baseline distorts the visual impression.


*[Figure — see PDF version]*


### Bar Charts

Bar charts display counts or proportions for categorical variables, making them the natural choice for comparing workload across departments, request types, or geographic units. Unlike histograms (which bin continuous data), bar charts represent discrete categories with gaps between bars to emphasize that each category is distinct. A bar chart of 311 requests by category---code compliance, street maintenance, water utilities, parks---immediately shows which services generate the most demand and where staffing or budget discussions should focus. Horizontal bar charts are preferable when category labels are long, and sorted bar charts (from highest to lowest) draw the reader's eye to the most important categories first. The Economist style favors clean, uncluttered bar charts with a single accent color and no 3D effects or heavy gridlines (tufte2001visual).


*[Figure — see PDF version]*


As Tufte emphasizes, a well-constructed graph is not decoration---it is an argument (tufte2001visual). Every element should serve the analytical purpose: axes should be labeled, scales should be honest, and chart junk (unnecessary gridlines, 3D effects, decorative fills) should be removed. In public administration, where graphs appear in council presentations, budget documents, and audit reports, the analyst's credibility depends on visual honesty as much as numerical accuracy.


## Describing Groups and Subgroups

Administrative datasets allow analysts to examine variation across space and subgroup---that is,
across neighborhood boundaries, demographic characteristics, or organizational units. Research on
neighborhood effects provides a strong conceptual foundation for understanding such variation
(sampson2012great,chetty2016mto). In practice, the most important descriptive findings in public administration often emerge not from system-wide summaries but from subgroup comparisons that reveal where the system is working well and where it is failing.

### Operational Relevance

Describing subgroups helps answer a wide range of managerial questions. Are certain neighborhoods consistently facing longer delays in 311 service completion? Are service backlogs clustered in particular request categories, such as infrastructure or code compliance, rather than spread evenly across all types? Are reporting patterns shaped by demographic or institutional factors---for instance, do neighborhoods with younger, more digitally connected populations file more online requests, while older populations rely on phone calls that may be logged differently?


Consider an EMS dataset that reports average response times by county. A statewide summary might show a mean of 10 minutes, but disaggregating by urban and rural subgroups could reveal that urban counties average 7 minutes while rural counties average 16 minutes. Further disaggregation by time of day might show that rural overnight responses exceed 25 minutes---a finding invisible in any aggregate statistic. Similarly, a 311 dataset disaggregated by council district might reveal that two districts with similar total request volumes have very different completion time distributions: one resolves requests steadily, while the other shows a bimodal pattern with a cluster of quick resolutions and a second cluster of requests that languish for weeks.


Subgroup description often reveals structural inequality---a theme central to both administrative
datasets (einav2014datarev) and neighborhood research (sampson2012great). The analyst's task is not merely to compute separate statistics for each group but to interpret the differences in light of the institutional processes, resource allocations, and historical patterns that produced them.


> 
**Briefing:** Subgroup analysis reveals who the system serves—and who it does not.


## Common Pitfalls

### Mean--Median Confusion

In right-skewed data, the mean exaggerates delays, costs, or risks, because a small number of extreme values pulls the average upward while the majority of observations cluster well below it. This issue parallels aggregated measures that conceal neighborhood-level disparities (sampson2012great). When an analyst reports a mean completion time of 14 days for 311 infrastructure requests, a city manager may assume that most requests take roughly two weeks. In reality, the median might be 6 days, with a handful of stalled requests stretching past 60 days. Choosing the wrong measure of central tendency can lead to staffing plans calibrated for a "typical" case that does not actually exist.

### Ignoring Population Scale

Comparing complaint counts across neighborhoods without accounting for population size risks
serious misinterpretation. A neighborhood with 500 residents and 25 complaints has a far higher complaint rate than a neighborhood with 10{,}000 residents and 80 complaints, even though the second neighborhood produces more complaints in absolute terms. This issue is analogous to the cross-neighborhood comparisons in social mobility studies that must be adjusted for population composition (chetty2016mto). Analysts should normalize counts---per capita, per household, or per service unit---before drawing conclusions about which areas are most affected.

### Assuming Normality

Public-sector data rarely follow a normal distribution. EMS response times, 311 completion times, and capital project durations typically exhibit right skew, with long tails driven by institutional bottlenecks and coordination failures. Relying on normal-theory summaries---such as reporting mean plus or minus one standard deviation as a "typical range"---leads to misguided thresholds and flawed evaluations that undercount extreme cases. Analysts should examine histograms and boxplots before selecting summary statistics, and should prefer robust measures such as the median and interquartile range when the data depart substantially from symmetry.


> 
**Briefing:** Many descriptive errors arise from assumptions imported from textbooks, not from reality.


## Practice and Application


    - Compute the mean, median, IQR, and standard deviation for completion times in the 311 dataset. 
    Discuss why the median may more accurately capture typical experience in skewed service systems (austin311open).
    
    - Create a histogram and describe its shape. 
    Relate it to structural features of administrative data-generating processes (einav2014datarev).
    
    - Identify neighborhood-level differences in percentiles for response times. 
    Connect these patterns to broader insights about spatial inequality (sampson2012great).
    
    - Compare boxplots across multiple request categories. 
    Explain how differences reflect institutional processes or resident behaviors.
    
    - Write a short memo interpreting outliers in one request category.
    Discuss whether these outliers reflect operational failures, rare events, or structural issues highlighted in neighborhood research (chetty2016mto).
    - Using the EMS response time data provided in this chapter's worked example (Table for Counties A and B), open Excel and verify the mean, median, and standard deviation calculations. Then create a histogram for each county using the Chart tool. In two sentences, explain what the histogram reveals that the mean alone does not.
    - Download the voter turnout dataset from the [Course Datasets page](../datasets). In Excel, compute the mean, median, and IQR of turnout rates across all counties for a single election year. Create a boxplot. Identify any outlier counties and speculate (in one paragraph) about what might explain their unusual turnout rates.


## Sources for Examples in This Chapter


    - City of Austin 311 open data portal (austin311open).
    - Research on administrative data interpretation (einav2014datarev).
    - Studies on neighborhood variation and spatial inequality (sampson2012great,chetty2016mto).


## Transition to Chapter Four

Descriptive statistics summarize what has happened; probability helps us reason about uncertainty
and what might happen next. Chapter~*chap:probability* introduces the foundations of
probabilistic thinking and its role in administrative decision-making.