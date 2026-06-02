---
layout: page
title: "Chapter 2"
permalink: /docs/chapter2/
---

# Developing Research Questions


## Epigraphs


> 
*"The formulation of a problem is often more essential than its solution."*

 Albert Einstein (Einstein)


> 
*"Clarity is the politeness of the analyst."*

 Adapted from Jean d’Alembert


Clarity of purpose is the foundation of analytical reasoning. A poorly framed question misdirects
attention, wastes administrative time, and encourages false precision. A well-formulated question,
by contrast, forces the analyst to be specific about what matters, what can be measured, and what
kinds of conclusions are appropriate. These epigraphs capture the intellectual discipline that
underpins all analytical techniques introduced in this book.


## Opening Case: San Antonio's Aging Water Mains and the Question Behind the Crisis


In 2023, the San Antonio Express-News reported on a pattern that had become difficult to ignore: aging water mains across San Antonio were breaking with increasing frequency, triggering boil-water notices that affected thousands of residents (San Antonio Express-News). Neighborhoods on the city's south and west sides appeared disproportionately affected. City officials acknowledged the problem and pointed to a multi-billion-dollar capital improvement plan, but residents and council members wanted answers now: Was the system getting worse? Were some communities bearing more of the burden than others?

The public debate was framed broadly---"San Antonio has a water infrastructure crisis"---but that framing resisted analytical traction. A crisis of what, exactly? Frequency of breaks? Duration of service disruptions? Cost of emergency repairs? Geographic concentration? Each framing implies a different outcome variable, a different unit of analysis, and a different comparison. A research question about whether break *frequency* is increasing over time requires annual counts by pipe segment or district. A question about *equity* requires mapping breaks against neighborhood demographics. A question about *severity* requires data on how long residents go without safe water after each event.

This case illustrates a challenge that recurs throughout public administration: the gap between a legitimate concern and an answerable analytical question. The tools in this chapter---moving from topics to questions, identifying outcomes and units, and specifying meaningful comparisons---are designed to close that gap.


**Guiding Questions**


    - "San Antonio has a water infrastructure problem" is a concern, not a research question. What outcome, units, and comparison would make this analytically tractable?
    - How would you operationalize "equity" in the distribution of water main breaks across neighborhoods?
    - What data would you need to determine whether boil-water notices are concentrated in particular parts of the city---and what limitations might you anticipate?


## Why This Chapter Matters

Public administration operates in an environment where decisions are consequential and resources
are constrained. City managers must decide where to place new ambulances, budget officers must
defend expenditure decisions, and nonprofit directors must demonstrate impact to funders. Each
actor faces a flood of information: performance dashboards, audit reports, survey data, and
service logs. Yet information is not analysis. The difference lies in the question being asked.

A research question is the hinge between a messy administrative reality and the analytical tools
described in this text. It determines which parts of a dataset are relevant and which can be
ignored, how ambiguous concepts such as "responsiveness" or "equity" are operationalized,
which comparisons are worth making and which would be misleading, and which methods---simple
tabulations, descriptive statistics, or more advanced techniques---are appropriate.

A weak research question leads to familiar pathologies. Analysts generate impressive charts that
no one requested. Committees debate numbers that do not actually illuminate the underlying issue.
Time is spent re-running analyses rather than clarifying aims. In some cases, poorly framed
questions can damage trust: stakeholders feel overwhelmed with technical material yet no closer to
understanding the problem.

Chapter 1 emphasized that analytical habits—skepticism, transparency, and
discipline—provide protection against these errors. This chapter shows how those habits are
translated into practice through the construction of research questions. It is not an
introductory formality. It is a practical chapter about how to think clearly before calculating
anything at all.


> 
**Briefing:** In public administration, a clear research question is often more valuable than an
additional dataset.


## Concepts and Intuition

At its core, a research question is a carefully worded sentence that describes what we are trying
to learn from data. It is deceptively simple. Analysts are often tempted to rush past this step,
assuming that their interest—say, in "service responsiveness" or "budget stress"—is sufficiently
obvious. It rarely is.

To see why, consider the City of Austin's 311 open data, which records service requests submitted
by residents (City of Austin open data). A seemingly straightforward interest in "slow response times"
can mean several different things:

Are we concerned about the slowest individual cases, or about typical performance? Are we comparing departments, neighborhoods, request categories, or time periods? Are we interested in the level of response times, or in changes over time? Are we worried about operational efficiency, equity, or both?

Absent a clear research question, reasonable analysts could pursue entirely different paths. One
might compute a single system-wide average; another might build separate distributions for each
department; a third might track monthly trends. None of them would necessarily be wrong, but they
might all be answering different questions.

A research question is therefore not a slogan ("improve responsiveness") or a strategy
("reduce delays"). It is a precise analytical formulation that bridges broad concerns and
concrete evidence. In this course, such questions typically fall into one of three broad types.
**Descriptive questions** summarize patterns---for example, asking what the distribution
of completion times looks like for infrastructure requests. **Comparative questions**
contrast groups or periods, such as whether median completion times are higher in District A
than in District B. **Relational questions** explore associations, asking whether
neighborhoods with more rental housing are associated with longer response times. Each type
implies a different analytical strategy, and recognizing which type a question belongs to is
the first step toward choosing the right tools.

We will rarely attempt full causal questions in this book, because the tools introduced—while
powerful—are designed primarily for description and association. Understanding these boundaries is
part of the discipline of good questioning.


> 
**Briefing:** A research question should tell you whether you are trying to describe, compare,
or relate.


## From Topics to Research Questions

Students and practitioners alike tend to begin from topics: public safety, housing, homelessness,
park quality, or financial stability. These topics reflect legitimate concerns and political
priorities. But they are too broad to be analyzed directly.

### From Concern to Question

The move from a topic to a question involves three steps:


    - Identify the *outcome* of interest.
    - Identify the *units* and *groups* to be compared.
    - Decide on the *kind of pattern* to be examined (level, difference, change, or
    association).


**Example 1: Traffic Safety**

The topic is traffic safety complaints. The outcome of interest is the number of traffic-related requests. The units and groups are neighbourhoods or council districts, and the pattern to be examined is the relative intensity of complaints, adjusted for population.

A workable question emerges:


> 
*Which council districts file the most traffic-related 311 requests per 10,000 residents?*


> **Returning to the Case:** The San Antonio Water System (SAWS) water infrastructure concern follows the same three-step decomposition. *Outcome:* number of water main breaks (or boil-water notices, or hours without service). *Units:* pipe segments, zip codes, or water service districts. *Pattern:* geographic concentration, trend over time, or comparison across neighborhood income levels. Each choice produces a different---and answerable---research question from the same broad concern.

**Example 2: City Responsiveness**

Here the topic is city responsiveness. The outcome is the number of days required to complete a request. The units are individual service requests, grouped by category or department, and the pattern of interest is differences in central tendency---whether measured by the median or the mean.

A clearer question becomes:


> 
*How do median completion times differ across major request categories?*


**Example 3: Park Maintenance**

The topic is park maintenance. The outcome is the volume of complaints concerning parks. The units and groups are neighbourhoods or park catchment areas, and the pattern to be examined is seasonal variation, perhaps tracked over the course of a year.

An analysable question is:


> 
*How does the monthly volume of park-related service requests vary over the year, and which parks show the largest seasonal swings?*


In each case, the broad concern is preserved, but the analytical task is made precise.


> 
**Briefing:** Turning a topic into a research question means deciding exactly what will be
counted, compared, or tracked.


### Worked Example: From a Mayor's Concern to Three Research Questions

Imagine a city manager receives this directive from the mayor: *"Our responsiveness to residents is unacceptable. Fix it."*

This is a legitimate concern but not a research question. An analyst's task is to decompose it into something answerable. Here are three possible research questions, each addressing a different dimension of "responsiveness":


    - **Descriptive:** What is the distribution of 311 request completion times across major service categories, and which categories exhibit the longest median delays?
    - **Comparative:** Do median completion times for infrastructure requests differ significantly between the city's east-side and west-side council districts?
    - **Relational:** Is there an association between the share of renter-occupied housing in a neighborhood and the average time to complete a 311 request?


**Evaluation.**
Question 1 defines the outcome (completion time), the units (requests by category), and the pattern (distribution shape and central tendency). It is answerable with existing 311 data.
Question 2 adds a specific comparison (east vs. west) and a test (whether the difference exceeds chance).
Question 3 introduces a predictor variable (renter share) and moves toward relational analysis. Each question is progressively more complex---but all three began with the same vague concern. The analyst's job is to make the choice explicit and justified.


## Anatomy of a Research Question

Strong research questions obey five principles: clarity, specificity, answerability, relevance, and
measurability. Each merits careful attention.

### Clarity

A clear question can be restated by a colleague without loss of meaning. It avoids vague terms
like "better," "fair," or "effective" unless these are explicitly defined. Clarity also requires that the question specify the outcome being measured and the units being compared, so that two analysts reading the same question would pursue the same data and the same analysis. When terms are left undefined, each analyst fills in the gaps with different assumptions, producing results that cannot be compared or reconciled.

*Unclear:* Are services delivered fairly?
*Clearer:* Do median completion times differ significantly across council districts?

The second question expresses the idea of fairness in a way that can be examined with data. It names an outcome (median completion time), identifies units (council districts), and implies a specific comparison (differences across those districts).

### Specificity

Specificity means identifying an outcome and a comparison. Analysts should be able to say, in
plain language, "We are comparing X to Y with respect to Z." A specific question constrains the analysis in productive ways: it tells the analyst which variables to extract, which subgroups to create, and which statistical tools to apply. Without specificity, the analyst faces an open-ended exploration that may produce interesting observations but rarely produces actionable conclusions.

*Non-specific:* Are infrastructure requests slow?
*Specific:* How many days elapse, on average, between the creation and closure of
infrastructure-related requests, and how does this compare to other categories?

The specific version identifies the outcome (days elapsed), the units (infrastructure requests), and the comparison (against other request categories), leaving little ambiguity about how to proceed.

### Answerability

Answerability demands that a question be feasible using existing or realistically obtainable data.
A city may wish to know whether residents "trust" a given agency, but if no survey exists and no
new data collection is possible, that question is not analytically answerable within the time
frame of a routine administrative decision.

In this course, answerability usually involves checking that the dataset contains the variables needed, confirming that units and time periods are adequately covered, and accepting that some attractive questions must be set aside for lack of data. These checks should be performed early in the analytical process, before significant time is invested in computation or modeling.

### Relevance

Relevance links an analytical exercise to a substantive decision or concern. It is possible to
frame very precise and answerable questions that are simply unimportant. Analysts should be able
to explain in two or three sentences why the answer would matter for a real-world decision. In public administration, relevance usually means that the question connects to a budgetary choice, a staffing decision, an equity concern, or a performance evaluation that someone in authority needs to act on. A question that cannot be linked to a concrete decision may be intellectually interesting but is unlikely to justify the administrative time required to pursue it.

### Measurability

Finally, measurability requires that concepts can be turned into variables. A question about
"cleanliness" might be operationalized as the number of litter-related complaints per block or
the proportion of inspections failing cleanliness standards. The operationalization need not be
perfect---the important step is that it is explicit. When the path from concept to variable is
left unstated, different analysts may measure the same idea in incompatible ways, producing
results that appear contradictory even when they are not. Making the measurement strategy explicit
also allows colleagues and decision-makers to evaluate whether the chosen indicator genuinely
captures the concept of interest or whether it introduces systematic distortion.


> 
**Briefing:** A strong research question is one that a skeptical colleague could translate
directly into a spreadsheet.


## Units, Variables, and Comparisons

Every research question can be decomposed into three technical components: the unit of analysis,
the variables, and the comparison. Mastering these components early pays dividends throughout the
course.

### Unit of Analysis

The unit of analysis is the entity on which observations are made. In this book we frequently use individual service requests, neighborhoods or zip codes, departments or agencies, time periods (days, weeks, months, years), facilities (parks, libraries), and people (employees, residents, participants). Each choice defines the level at which patterns are observed and conclusions are drawn.


Choosing the unit of analysis is not a neutral decision. It affects how many observations are available, how much variation can be observed, and how results are interpreted. A unit that is too broad may mask important subgroup differences, while one that is too granular may introduce excessive noise or leave the analyst with too few observations to detect meaningful patterns.

For instance, analysing response times at the request level might reveal skewness and outliers,
while analysing them at the neighborhood level might highlight geographic inequality.

### Variables

Variables describe attributes that differ across units.

In the 311 dataset, typical variables include:


    - `DaysToComplete` — a continuous variable measuring the difference between closure
    and creation dates;
    - `Category` — a categorical variable (e.g., "Animal," "Infrastructure,"
    "Traffic");
    - `OnTime` — a binary variable indicating whether a request was completed within a
    specified threshold;
    - `Zipcode` or `CouncilDistrict` — locational identifiers.


Variables must be clearly defined so that every analyst understands what is being measured, consistently coded so that categories are mutually exclusive and exhaustive, and appropriate to the research question so that the level of detail is sufficient to answer the question at hand. When any of these conditions is violated, the resulting analysis may be technically correct but substantively misleading.

### Comparisons

Most research questions require comparing something to something else. Comparisons may be drawn across groups---departments, districts, or request categories---or across time, such as before versus after a policy change or over months and years. Spatial comparisons contrast neighborhoods, zip codes, or regions, while distributional comparisons examine entire patterns rather than merely averages. Explicitly stating the intended comparison at the outset helps analysts avoid improvising midway through the analysis and ensures that the statistical methods selected are appropriate for the structure of the question.


> 
**Briefing:** If you cannot name the unit, list the variables, and describe the comparison,
the research question is not yet ready.


## Worked Examples

Examples illustrate how all of these ideas fit together in practice.

### Example 1: Distribution of Completion Times

**Concern.** Community groups complain that some requests "seem to take forever." The city
manager wants to know whether this is a system-wide issue or confined to particular areas.

**Research question.**

> 
*How does the distribution of completion times differ across request categories and departments?*


**Unit, variables, comparison.**

    - **Unit:** Individual service request.
    - **Variables:** `DaysToComplete`, `Category`, `Department`.
    - **Comparison:** Distributions (medians, quartiles, tails) across groups.


The analysis might reveal, for instance, that animal-related requests are typically resolved
within a few days, while infrastructure requests have a long right tail: most are resolved
promptly, but a small fraction languish for weeks. The research question has directed attention
specifically to distributional features rather than a single overall average.

### Example 2: Seasonal Patterns in Demand

**Concern.** Supervisors suspect that certain services experience seasonal spikes that are
not reflected in staffing schedules.

**Research question.**

> 
*Which request categories exhibit the strongest seasonal variation in monthly call volumes?*


**Unit, variables, comparison.**

    - **Unit:** Month-by-category combination.
    - **Variables:** Count of requests per month per category.
    - **Comparison:** Variation over time within and across categories.


Here, a simple line chart built from monthly counts may reveal that tree-related complaints spike
after storms, while animal-related requests are more stable. The research question has ensured that
the analysis is precise about what "seasonal" means (monthly variation), and for whom (categories
of service).

### Example 3: Neighbourhood Equity

**Concern.** Advocacy organisations raise concerns that some neighborhoods receive slower
service than others, potentially compounding existing inequalities. This echoes a broader
literature on neighborhood effects and spatial disadvantage (Sampson 2012; Chetty et al. 2016).

**Research question.**

> 
*Do neighborhoods with higher proportions of renters experience longer median completion times for infrastructure-related requests?*


**Unit, variables, comparison.**

    - **Unit:** Neighbourhood (or census tract).
    - **Variables:** Median completion time for infrastructure requests; proportion of
    renter-occupied housing.
    - **Comparison:** Relationship between neighborhood rental share and median completion
    time, possibly expressed in descriptive plots or correlation.


Even without formal causal claims, this question pushes the analyst to link administrative data
with demographic indicators and to articulate clearly what "equity" is being used to mean in the
analysis.


> 
**Briefing:** Worked examples demonstrate that a good research question already contains the
outline of the analysis.


## The Data-Generating Process

A research question is strongest when paired with a clear understanding of how the underlying data
record real-world processes. Administrative data are not collected primarily for research. They
are by-products of systems designed to manage work, allocate staff, or document compliance
(Einav & Levin 2014). This has three implications.

### Selective Recording

Some events are recorded more diligently than others. Requests that require site visits may be meticulously logged, while quick telephone resolutions are entered less consistently. Similarly, high-profile categories---such as traffic safety---may receive more attention from supervisors and data entry staff than routine maintenance categories. These differences in recording intensity mean that variation in the data may partly reflect variation in documentation practices rather than variation in actual service delivery. A research question that assumes equal recording quality across categories may therefore produce misleading results.

### Timing and Delays

Timestamps may not perfectly reflect real-world timing. Closure times might be entered in batches
at the end of a shift, and backlogs might be updated only periodically. An analyst asking, "How
long does it take to resolve a request?" should consider whether the recorded times genuinely
measure this or instead reflect data-entry patterns.

### Classification and Reclassification

Categories can change over time. A new mayor's office initiative might introduce a new category,
or staff may receive training that alters how they label requests. Without noticing such changes,
an analyst might misinterpret an apparent trend as a real-world change when it is actually an
administrative artefact.


> 
**Briefing:** A research question that ignores how data are generated invites confident
answers to the wrong problem.


## Common Pitfalls

With the conceptual machinery in place, it is useful to survey the most common ways research
questions fail.

### Vagueness

Questions like "Are services good?" or "Is this program effective?" lack operational content.
They must be broken down into components: timeliness, coverage, satisfaction, cost, or equity. Vague questions are particularly dangerous in public administration because they invite each stakeholder to project a different meaning onto the same words. A council member who asks "Are services good?" may be thinking about equity; a budget officer hearing the same question may focus on cost-efficiency; and a department head may interpret it as a question about workload management. Until the question is made precise, no amount of data can resolve the disagreement.


> **Returning to the Case:** "San Antonio has a water infrastructure crisis" is a textbook example of vagueness. A city council member who asks this cannot be answered with data. But "Has the annual number of water main breaks per 100 miles of pipe increased over the past decade in SAWS service districts?" can be. The difference is not one of ambition but of precision.

### Overly Narrow Focus

At the other extreme, excessively narrow questions---"What was the average completion time for
pothole requests on a single street last week?"---may be answerable but unhelpful. They do not
support generalization or policy decisions. A question that applies to only a handful of observations provides no basis for drawing broader conclusions about system performance. Narrow questions also tend to produce volatile results, because small samples are heavily influenced by individual outliers or one-time events. The goal is to find a level of specificity that is precise enough to guide analysis but broad enough to yield results that inform decisions beyond the immediate case.

### Unanswerable Ambitions

Sometimes the answerable part of a question lies in examining patterns or associations, but the
analyst is tempted to jump directly to causation. For example, asking, "Does the introduction of
a new app cause faster service?" may not be supportable with available data, whereas, "How did
completion times change after the app was introduced, controlling for seasonality?" might be
answerable.

### Category Confusion

Administrative categories rarely line up neatly with analytical concepts. A label such as
"infrastructure" can bundle together very different tasks, from filling potholes to repairing
streetlights, each with its own resource requirements, response timelines, and staffing
implications. When an analyst treats these heterogeneous tasks as a single category, the
resulting summary statistics obscure meaningful variation within the group. A strong research
question may require constructing new variables or grouping categories more thoughtfully---for
instance, separating road maintenance from electrical work---so that the analysis captures the
distinctions that matter for operational decisions.

### Misaligned Methods

Finally, a question may be perfectly well framed, but the chosen method may not match it. Common misalignments include asking about distributions but reporting only means, asking about change over time but ignoring baseline levels, and asking about variation across space but not mapping or stratifying by geography. These errors are surprisingly common in practice because analysts often default to familiar tools rather than selecting the tool that fits the question. Much of this misalignment can be avoided if the research question is explicit about the kind of pattern of interest, since the pattern type---level, difference, trend, or association---directly implies the appropriate analytical approach.


> 
**Briefing:** Many "statistical" problems are actually question problems in disguise.


## Practice and Application

The following exercises are designed to make question formulation a practical skill rather than an
abstract ideal.


    - **From topic to question.**  
    For each topic below, write two research questions:
    
        - a descriptive question, and
        - a comparative question.
    
    Topics:
    
        - emergency medical response,
        - solid waste complaints,
        - public park maintenance.
    
    For each question, write one sentence justifying why it is relevant for a decision-maker.

    - **Decomposing a question.**  
    Take one of your questions from (1). Identify explicitly:
    
        - the unit of analysis,
        - the key variables,
        - and the comparison to be made.
    
    Rewrite the question if these elements are not obvious.

    - **Checking answerability.**  
    Using any dataset assigned in this course (such as the 311 requests sample), assess whether
    your chosen question can be answered with the variables available. If not, revise the question
    or state clearly what data would be needed.

    - **Rewriting for clarity.**  
    Write down a vague question you have encountered in a work, internship, or news setting (for
    example, about "waste," "fraud," or "fairness"). Rewrite it into at least two measurable
    research questions that capture different aspects of the concern.

    - **Briefing note.**
    Draft a two-sentence briefing for a department director explaining how investing an extra
    hour in sharpening a research question can save days of unnecessary analysis and reduce the
    risk of misleading conclusions.
    - Using the SAWS water infrastructure case from this chapter, write three research questions at increasing levels of specificity: (a) a broad descriptive question, (b) a comparative question contrasting two neighborhoods, and (c) a relational question involving a predictor variable. For each, identify the outcome, units, and comparison.
    - A council member says: "Our parks are in terrible shape." Decompose this into two alternative research questions that would lead to different analytical approaches. Explain why the choice of question matters for the type of data collected and the method used.


These exercises are not about clever phrasing. They are about developing a habit: resisting the
temptation to jump into calculations before the analytical task has been defined.


## Sources for Examples in This Chapter

Examples in this chapter draw on:


    - City of Austin 311 open data portal and documentation (City of Austin open data).
    - Research on administrative data structures and interpretation (Einav & Levin 2014).
    - Studies of neighborhood effects and spatial inequality (Sampson 2012; Chetty et al. 2016).


## Transition to Chapter Three

Strong research questions define analytical purpose. They determine what can be measured, which
patterns matter, and how evidence should be interpreted. With these foundations in place, the next
chapter introduces the empirical vocabulary that analysts use to summarize and interpret data: the
logic and language of descriptive statistics.

Chapter 3 turns to that toolkit.