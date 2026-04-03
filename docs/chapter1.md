---
layout: default
title: "Chapter 1"
nav_order: 1
---

# Introduction to Analytical Foundations


## Epigraphs


> 
*``If you can't measure it, you can't improve it.''*

 Peter F.~Drucker (drucker1973,drucker1966)


> 
*``You've got to know what you're doing before you can do it right.''*

 Willie Nelson (nelsonTexMonthly,nelsonACL)


These quotations capture the analytical spirit of this course. Drucker’s maxim highlights the
importance of measurement and disciplined inquiry, while Nelson’s remark speaks to the need for
understanding foundational concepts before relying on tools. Both set the tone for the habits of
mind developed in this chapter.


## Opening Case: Winter Storm Uri and the Battle Over Grid Failure Data


In February 2021, Winter Storm Uri struck Texas, producing the most catastrophic power failure in the state's modern history. Millions of residents lost electricity for days in subfreezing temperatures. In the aftermath, public agencies, journalists, and researchers attempted to quantify what had happened---and immediately encountered conflicting numbers. Various parties offered competing explanations: the Electric Reliability Council of Texas (ERCOT) pointed to surging demand, engineers cited failures in natural gas supply infrastructure, and some commentators attributed losses to frozen wind turbines, though grid data showed wind represented a small share of total generation loss (tribuneWinterStorm2021). This textbook takes no position on the policy or regulatory debates surrounding the grid failure; the case is used here because the competing claims illustrate fundamental challenges in measurement, data collection, and analytical interpretation.

The disagreements extended to human consequences. The official state death toll, compiled from death certificates listing hypothermia or storm-related causes, initially stood at 246. Independent analyses by investigative reporters and epidemiologists---using excess-mortality methods that compared observed deaths during the storm period against historical baselines---estimated the toll at 700 or higher. The same event, the same weeks, the same state: yet the numbers diverged by a factor of three, because different agencies used different definitions, different data collection methods, and different counting rules.

For an analyst in public administration, this case is not primarily about weather or energy policy. It is about what happens when institutional measurement systems produce the data we use. Every number in a government dashboard or news report reflects choices about what to count, how to count it, and who does the counting. The analytical habits introduced in this chapter---reading data critically, understanding data-generating processes, and resisting premature confidence---are the tools that help an analyst navigate exactly this kind of situation.


**Guiding Questions**


    - When two agencies report different numbers for the same event (e.g., storm-related deaths), what analytical habits help an analyst evaluate which figure is more credible?
    - How does the way data are collected---by hospitals, by ERCOT, by county medical examiners---shape the statistics that appear in news reports?
    - What does it mean to "read data critically" when the data themselves are produced by institutions under political pressure?


## Why This Chapter Matters

Public administration operates under pressure: fixed budgets, political scrutiny, and urgent
decisions. Analysts rarely control the data they inherit, yet their conclusions can shape policy,
budget allocations, staffing levels, and public trust. Poorly framed questions mislead. Weak
methods distort. Sloppy interpretation generates false confidence.

Analytical techniques are therefore not a luxury; they are a requirement. Whether estimating
ambulance delays, explaining revenue trends, or identifying disparities across communities,
public institutions need evidence that is cautious, transparent, and defensible. The habits
introduced here provide the foundation for every tool used in this book.

Strong analysis protects institutions from predictable mistakes. It forces the analyst to confront
the limits of the data, challenge attractive but weak narratives, and work systematically toward
evidence that is modest but useful. This chapter explains how to think about data before we
calculate anything at all.


## Concepts and Intuition

Analytical reasoning in public administration requires more than familiarity with formulas. It
demands an ability to link observations to underlying mechanisms. Data never speak for themselves.
They represent slices of administrative systems shaped by technology, staffing, incentives,
geography, and policy constraints. Understanding this context is not optional; it is central to
the analytical task.


> **Returning to the Case:** The Winter Storm Uri death toll dispute illustrates this directly. Death certificates---the data source for the official count---reflect choices made by county medical examiners about how to classify cause of death. Excess-mortality estimates use a different data source entirely: total death counts compared against historical baselines. Neither method is wrong, but each answers a slightly different question. The analyst who treats either number as "the truth" without understanding the measurement system behind it has already made an error.}

Consider a dataset of EMS response times from the Texas Department of State Health Services
(DSHS). On the surface, it lists durations between call receipt and arrival on scene. In reality,
each number reflects call triage practices, dispatcher training, ambulance availability, traffic
conditions, neighborhood street design, and the maintenance schedules of aging vehicles
(dshsEMS). To interpret such data responsibly, the analyst must think about these forces
before drawing conclusions.

The same logic applies across all techniques. Descriptive statistics summarize behavior, but they
do not explain it. Probability quantifies uncertainty but depends on knowing which processes
generate variation. Regression reveals relationships but cannot substitute for domain knowledge.
The core habits that anchor every method in this text follow from these realities. First, analysts must *ask precise questions*, because vague questions produce meaningless answers and waste institutional time. Second, they must *understand how data are generated*, recognizing that every dataset reflects the incentives, rules, and constraints of the organization that produced it. Third, they must *stay skeptical*, because real administrative data contain noise, gaps, and contradictions that can mislead even experienced practitioners. Fourth, they must *be transparent*, documenting their reasoning and assumptions so that colleagues can evaluate and build on their work. These four habits---precision, awareness, skepticism, and transparency---recur throughout every chapter of this text, and analysts who adopt them early avoid the most common errors in public-sector analysis.


> 
**Briefing:** Good analysis reduces complexity without obscuring truth.


## Worked Examples

Examples reveal the difference between mechanical calculation and genuine analysis. In public
administration, where data quality varies and reporting systems differ across jurisdictions,
analysts must actively interrogate patterns rather than accept them at face value.

### A Quick Illustration: Same Number, Different Realities

Consider two Texas counties that both report an average EMS response time of 12 minutes. On the surface, they appear identical. But examine the underlying data:


*[Table — see PDF version]*


County A's average is pulled up by a single 36-minute call---likely a rural incident with long travel distance. Its *typical* response (the median) is actually 9.5 minutes. County B's mean and median are identical, indicating consistent performance. A city manager who sees only the average would treat these counties the same. An analyst who looks deeper would recognize that County A has an outlier problem requiring targeted intervention, while County B has a systemic issue affecting all calls. The analytical habits introduced in this chapter---asking precise questions, understanding how data are generated, and staying skeptical of summary numbers---are what distinguish these two conclusions.

### Texas EMS Response Times

A superficial analysis of statewide EMS response data might compute a single average and consider
the matter settled. A deeper look quickly reveals disparities. Rural counties often lack full-time
ambulance coverage, relying on volunteers who respond from home. Urban jurisdictions record
thousands of calls per month, creating congestion in dispatch systems. Neighborhoods classified as "historically redlined"---a designation drawn from federal Home Owners' Loan Corporation maps of the 1930s and used as a standard variable in contemporary urban research---show persistently slower response times, a pattern researchers attribute to decades of reduced infrastructure investment in those areas (andersonAmbulanceDeserts,hassaneinRedlined).

In some counties, long distances and sparse station coverage drive higher averages. In others,
reporting systems are incomplete: calls may be recorded without full timestamps, or only a subset
of incidents may be uploaded to the state system (dshsEMS). One county may appear to have
exceptionally fast response times simply because it submitted only a handful of cases that month.
Another may look slow because its data-entry procedures timestamp calls differently.


> 
**Briefing:** Statistics without context misrepresent performance.


The lesson is straightforward: averages alone cannot describe system performance. Analysts must
examine distributions, subgroup patterns, and missingness before drawing conclusions about equity
or effectiveness.

### Austin ACFR Revenue Trends

City financial statements tell a similarly complicated story. The City of Austin’s Annual
Comprehensive Financial Report (ACFR) lists revenue from property taxes, sales taxes, charges for
services, grants, and enterprise activities (austinACFR). A simple year-over-year comparison
can mask larger structural shifts: tourism cycles, population growth, new fee structures, or
legislative limits on tax rates (tribuneBudget).

A spike in sales-tax revenue may signal economic growth—or it may reflect one-time events,
inflation, or a change in vendor remittance schedules. A dip in enterprise revenue may result
from weather disruptions, capital maintenance closures, or policy decisions designed to rebalance
fees.

A more robust analysis decomposes trends by category, examines moving averages, and checks for
structural breaks. Analysts might compare year-over-year change against a five-year baseline or
examine revenue per capita to account for population growth. Such steps prevent misinterpretation
that could drive poor budgeting decisions.


> 
**Briefing:** Examples are not decoration; they are evidence.


These examples show how the same numerical tools—averages, growth rates, charts—can either
clarify or mislead depending on how analysts think about the systems behind the numbers.


## Common Pitfalls

Analysts regularly confront traps that produce overconfidence and weak conclusions. Understanding
these pitfalls is central to analytical discipline.

*Mistaking averages for insight* is perhaps the most pervasive error. Averages hide inequality, skewness, and risk, collapsing complex distributions into a single number that can obscure the very patterns analysts need to detect. A county-wide average EMS response time, for example, may look acceptable even when specific communities experience dangerously long waits. Responsible analysis almost always requires looking beyond the average to examine the full distribution.


*Ignoring the data-generating process* leads analysts to treat numbers as objective facts when they are, in reality, products of specific reporting systems, definitions, and institutional practices. Reporting systems vary across jurisdictions; definitions of key terms change over time; and the agencies collecting data operate under their own incentive structures. An analyst who does not ask how the data were produced risks drawing conclusions that reflect administrative artifacts rather than real-world conditions.


*Overinterpreting small samples* is especially dangerous when dealing with rare events. Opioid-related deaths in a small county, for example, may jump from two to six in a single year---a 200\


*Confusing precision with accuracy* occurs when analysts mistake fine-grained measurement for reliable measurement. More decimal places do not mean more truth; they mean only that the recording instrument is detailed, not that it is correct. 
> **Returning to the Case:** ERCOT reported outage durations to the minute during Winter Storm Uri, but the underlying data contained large temporal gaps where monitoring equipment had itself lost power. Precise timestamps masked fundamentally incomplete records.} This pitfall is particularly seductive in an era of dashboards and automated reporting, where the polish of the output can obscure the fragility of the input.


*Assuming stability means reliability* is a subtler trap. Smooth trends can mask corrections, backfilled records, or quiet redefinitions of what is being counted. A performance metric that holds steady for three years may reflect genuine consistency---or it may reflect an agency that updates its numbers retroactively, smoothing out embarrassing fluctuations before they reach the public. Analysts should investigate the editorial history of any dataset that appears suspiciously stable.


Another common error is assuming that more data automatically improve analysis. A dashboard with
two hundred indicators is not inherently better than a table with five. Without a clear question
and disciplined reasoning, abundant data produce abundant confusion. Analytical skill lies not in collecting every number, but in identifying which numbers answer a given question---and in recognizing when the available data simply cannot support a confident conclusion.


## Recurring Examples Used Throughout This Textbook

Three anchor examples appear throughout this textbook to illustrate analytical concepts consistently. Each was chosen because it offers a distinctive analytical challenge while remaining accessible to students with no prior statistical training. Together, they span political, administrative, and general contexts, ensuring that the techniques introduced in each chapter are demonstrated across the range of problems public administrators encounter.


**Texas Voter Registration and Turnout Patterns (Political Science).** Data from the Texas Secretary of State provide a rich setting for descriptive statistics, inference, and regression. Turnout varies widely by county, age group, election type, and geography, offering clean demonstrations of distributions, group comparisons, and modelling. This dataset was chosen because it combines large sample sizes with meaningful subgroup variation: urban counties behave differently from rural ones, midterm elections differ from presidential cycles, and demographic patterns create natural comparisons that motivate the statistical tools introduced in later chapters. It also connects directly to questions students encounter in political science and public affairs coursework, making the analytical exercises feel immediately relevant.


**Texas EMS Response Times (Public Administration).** Drawn from the DSHS 911 Run Times dashboard, these data reveal how administrative systems generate information. Reporting delays, staffing constraints, geography, and legacy infrastructure shape observed response times in ways that complicate straightforward interpretation. This dataset was chosen precisely because it is messy in the ways that real administrative data tend to be: timestamps may reflect data-entry patterns rather than actual events, rural and urban systems operate under fundamentally different constraints, and coverage gaps make statewide comparisons difficult. These features make the EMS data an ideal vehicle for teaching students to think critically about measurement, missingness, and the institutional forces behind the numbers.


**Texas Weather and Extreme Heat Events (General).** Daily temperature data from NOAA provide a neutral, intuitive dataset for illustrating probability, sampling distributions, rare-event analysis, and long-run trends. Unlike the voter and EMS datasets, weather data carry no political valence, which makes them useful for introducing abstract statistical concepts---such as the normal distribution, confidence intervals, and hypothesis testing---without the interpretive complications that accompany politically sensitive topics. The dataset also demonstrates how rare events, such as extreme heat days, behave statistically: they are infrequent by definition, yet their consequences for public health and infrastructure are disproportionately severe, making them a natural setting for discussions of tail risk and uncertainty.


## Practice and Application


    - Identify a public-sector dataset (state, local, or federal). In one paragraph, describe three ways its data-generating process could influence interpretation. Be explicit about reporting rules, incentives, or constraints.
    - Obtain a simple distribution of EMS response times for two Texas counties (or use a synthetic example provided in class). Compare mean and median for each county. Write a short note explaining what the comparison does—and does not—tell you.
    - Find a figure or table in a recent government report. Rewrite the caption so that it makes the analytical claim more precise and acknowledges at least one limitation.
    - In Excel, build a histogram using any administrative dataset discussed in class (EMS, ACFR, or another source). Describe what the shape of the distribution reveals about typical cases and outliers.
    - Write a two-sentence briefing for a city manager summarizing why transparency in assumptions and methods matters for public analysis.
    - Two news outlets report different numbers of power outages during a recent Texas storm: one says 2.1 million households, the other says 4.5 million. Using the analytical habits from this chapter, list three specific reasons the numbers might differ (consider definitions, data sources, and timing). Write a two-sentence note explaining which figure you would cite in a policy brief and why.


## Key Terms

    - [Analytical Habits] The disciplined ways analysts frame questions, interrogate data, and justify conclusions.
    - [Data-Generating Process] The administrative and operational forces that shape how data come into existence.
    - [Distribution] The shape and spread of values in a dataset, essential for identifying variation and outliers.
    - [Measurement Error] The difference between the recorded value and the underlying reality, often produced by reporting rules.
    - [Transparency] Clear communication of assumptions, methods, and limitations to support credible decision-making.


## Key Takeaways

    - Strong analysis begins with precise questions and an understanding of how data are generated.
    - Averages alone rarely reveal the full story—distributions and context matter.
    - Administrative datasets reflect operational constraints, reporting rules, and structural inequalities.
    - Transparency, skepticism, and disciplined reasoning prevent common analytical errors.
    - The recurring examples used throughout this textbook—voter turnout, EMS response times, and Texas weather—illustrate how analytical tools apply across political, administrative, and general contexts.


## Sources for Examples in This Chapter
This chapter draws on real reporting and administrative datasets used throughout the book:


  - DSHS EMS 911 Run Times Dashboard and Technical Notes ((dshsEMS)).
  - Anderson, J. "Rural Ambulance Funding" in *County Progress* (andersonAmbulanceDeserts).
  - Hassanein, N. "Historically Redlined Communities Have Slower EMS Response Times" in *Stateline* (hassaneinRedlined).
  - City of Austin Annual Comprehensive Financial Report ((austinACFR)).
  - Texas Tribune reporting on local budgets and opioid mortality ((tribuneBudget), (simpsonAstudillo)).
  - San Antonio Express-News statewide reporting on synthetic opioid trends ((expressNewsOpioids)).


## Transition to Chapter Two
Analytical habits matter because real data are messy. Public datasets reflect systems, incentives,
and constraints as much as they reflect outcomes. To make sense of such data, analysts begin with
a fundamental toolkit: describing how values are distributed, how much they vary, and where
anomalies lie.

Chapter~*chap:descriptive* introduces that toolkit—the essential language of descriptive
statistics.