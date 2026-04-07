---
layout: page
title: "Chapter 9"
permalink: /docs/chapter9/
---

# Putting It All Together: Completing the Final Project


## Epigraphs


> 
*"Theory without data is a daydream; data without theory is a nightmare."*

 Anonymous (found in modern applied statistics)


> 
*“Statistics are the triumph of the quantitative method, and the quantitative method is the 
victory of sterility and death.”*

 Hilaire Belloc


Students now possess the full analytical toolkit needed to conduct an applied research project in
public administration. The Final Project is not an exercise in formula memorization; it is the
integration of data, statistical reasoning, conceptual framing, and real-world public-sector
problem solving. This chapter provides practical guidance on how to structure, execute, and present
a rigorous quantitative analysis.

Public administrators do not ask, “What is the mean?” They ask:


    - Is service delivery equitable across neighborhoods?
    - Does a policy reform improve performance?
    - How do staffing, workload, and context shape outcomes?
    - What can data tell us—and what can it not tell us?


These questions are at the heart of modern public management and echo the themes developed
throughout this book: careful measurement, transparent assumptions, respect for uncertainty, and
attention to institutional context (gaoDataQuality, einav2014datarev, gelman2007data).


## Opening Case: San Marcos and Hays County---Can Services Keep Up with Growth?


Hays County and its largest city, San Marcos, have ranked among the fastest-growing communities in the United States for more than a decade. Between 2010 and 2023, the county's population roughly doubled, driven by Austin-area spillover along the I-35 corridor, new residential developments, and a growing Texas State University student population. The Austin American-Statesman and Texas Tribune reported extensively on the consequences: building permit backlogs stretching months beyond comparable cities, water infrastructure strained to capacity, public safety staffing ratios that lagged behind population growth, and contentious bond elections to fund roads and drainage projects (statesmanHaysGrowth).

For a public administration analyst, this is not a single problem---it is a constellation of problems that requires every tool introduced in this course. Describing the growth pattern demands the distributional thinking of Chapter~*chap:descriptive*. Forecasting future service demand under uncertainty invokes the probability concepts of Chapter~*chap:probability*. Assessing whether San Marcos's staffing ratios are significantly different from peer cities requires the inferential tools of Chapters~*chap:inference* and~*chap:independentttests*. Evaluating whether a bond-funded infrastructure investment improved permit processing times calls for the paired comparisons of Chapter~*chap:pairedttests*. And modelling which factors---population density, staffing levels, budget allocation, geographic constraints---best predict permit processing time is a regression problem (Chapter~*chap:regression*).

This chapter guides you through the process of integrating these tools into a single, coherent analysis. The San Marcos case will serve as a running example of how a Final Project moves from question formulation to data description, statistical testing, modelling, and policy-relevant interpretation.


**Guiding Questions**


    - If asked to evaluate whether San Marcos's rapid growth has degraded public service delivery, what research question would you formulate---and which analytical tools would you use?
    - How would you combine descriptive statistics, inferential tests, and regression to build a comprehensive picture of service delivery strain?
    - What limitations would you acknowledge, and how would uncertainty affect your policy recommendations?


> 
**Briefing:** The Final Project is an exercise in *integrated analytical thinking*.  
It is your opportunity to apply each concept from the course—not in isolation, but as a 
coherent methodological toolkit.


## Step One: Defining a Research Question

A compelling research question is analytical, specific, and grounded in public administration.

Good examples:


    - Do 311 service delays differ across neighborhoods with different socioeconomic characteristics?
    - Did EMS response times improve after a staffing reform? (dshsEMS)
    - Do census tract income levels predict emergency call volume? (uscensusACS)
    - Does digital recordkeeping reduce inspection processing times? (einav2014datarev)


Weak questions are overly broad ("Is the city doing well?") or descriptive without inference
("What is the average?").


> **Returning to the Case:** For the San Marcos case, "Has rapid growth hurt the city?" is too vague. A stronger formulation: "Has the ratio of building permits issued to planning staff declined in San Marcos relative to peer cities between 2015 and 2023, and is the difference statistically significant?" This question specifies an outcome (permits per staff), units (cities), a comparison (San Marcos vs. peers), and a time frame---all requirements of a well-formed research question.}

Use Chapter~*chap:research_questions* to refine scope and align your analysis with theoretical
motivation, managerial relevance, and available data.


> 
**Briefing:** A good question narrows possibilities; a weak question expands confusion.


## Step Two: Identifying and Understanding Your Data

All empirical work begins with data, and a strong Final Project demonstrates that the analyst understands not just what the data contain but how they came to exist. Your data section should clearly describe the source (whether 311 logs, ACS estimates, EMS incident records, budget documents, or other administrative files), the unit of analysis (individual incidents, neighborhoods, census tracts, monthly aggregates, or some other entity), the measurement processes that produced each variable, and any known limitations or sources of bias. This is not a formality; it is the foundation on which every subsequent analytical choice rests. An analyst who does not understand the data-generating process risks drawing conclusions that reflect administrative artifacts rather than real-world conditions (gaoDataQuality).

Administrative data differ fundamentally from data collected through designed surveys or experiments. As Einav and Levin emphasize, administrative records are by-products of operational systems---they exist because agencies need to manage workflows, allocate staff, and document compliance, not because a researcher designed a study (einav2014datarev). This means that coverage may be uneven (some departments log every interaction while others record only completed cases), definitions may shift over time (a "vacancy" in one year may not match the definition used three years later), and missingness is rarely random (the units with the worst outcomes are often the least likely to report complete data). Your data description should connect explicitly to the concepts introduced in Chapters~*chap:descriptive* and~*chap:probability*, showing that you understand how the distributional characteristics and uncertainty in your data flow from the institutional processes that generated them.

With Step One having established a clear research question, the transition to Step Two should feel natural: the question determines what data are needed, and the data's characteristics in turn constrain what questions can be answered credibly.


## Step Three: Descriptive Statistics and Visualization

Before modeling or inference, you must understand the shape, spread, and structure of your data. Descriptive statistics are not a preliminary hurdle to clear before reaching the "real" analysis; they are themselves a form of analysis that frequently reveals the most important features of the problem. Computing means, medians, standard deviations, and percentiles for your key variables establishes the empirical baseline. Examining distributions through histograms and boxplots reveals whether your data are symmetric, skewed, or multimodal---each of which has implications for the inferential tools you will use later. Identifying outliers and structural features helps you determine whether extreme values reflect genuine phenomena (such as a single catastrophic delay in permit processing) or data-entry errors that should be flagged before modeling.

Visualization deserves particular attention. Scatterplots of your outcome variable against each predictor provide an early indication of whether relationships are linear, curved, or absent. Grouped bar charts and side-by-side boxplots reveal whether subgroups differ in ways that your research question anticipated---or in ways you did not expect. As Tukey, Cleveland, and Anscombe all emphasize, graphical analysis is not decoration; it is a diagnostic tool that often catches problems invisible in numerical summaries (tukeyEDA, clevelandGraphing, anscombe1973graphs). Your goal in this step is to interpret every figure and table in light of the public-sector context: a right-skewed distribution of completion times tells one story in a department with chronic understaffing and a different story in a department that processes most requests quickly but occasionally encounters regulatory bottlenecks.

Having described your data thoroughly, you are now equipped to move to Step Four, where the uncertainty embedded in those descriptions becomes the central concern.


> 
**Briefing:** Good descriptive work often reveals 70\


## Step Four: Applying Probability and Uncertainty

Chapter~*chap:probability* introduced the central idea of uncertainty, and the Final Project is where that idea must move from the abstract to the applied. Every dataset you work with contains multiple sources of uncertainty: measurement error (timestamps recorded to the nearest hour rather than the nearest minute), sampling error (ACS estimates based on a fraction of the population), administrative irregularities (coding changes, staff turnover, reorganizations that alter data collection), and genuine randomness in the processes being studied (uscensusACS). Your project should explicitly name the sources of uncertainty relevant to your analysis and explain how each one could affect your conclusions.

Incorporating uncertainty into interpretation means more than reporting confidence intervals, though that is important. It means acknowledging that your point estimates are surrounded by ranges of plausible values, that small differences between groups may not be distinguishable from noise, and that the precision of your conclusions depends on sample size, data quality, and the assumptions underlying your statistical methods. Manski warns against the "lure of incredible certitude"---the tendency to present findings as more definitive than the evidence supports (manski2019policy). Public administrators make consequential decisions based on analytical work, and an analyst who overstates certainty risks directing resources toward problems that may not exist while overlooking problems obscured by imprecise data. A clear, honest explanation of uncertainty is what distinguishes excellent projects from merely adequate ones.

The descriptive patterns identified in Step Three now acquire probabilistic context: the variation you observed is not just a feature of the data but a reflection of underlying processes whose behavior you can characterize with the tools from Chapter~*chap:probability*.


## Step Five: Using Inferential Tools Appropriately

Depending on your question, you may employ:

### 1. Independent *t-tests*
Comparing two independent groups (e.g., rural vs. urban EMS response times).

### 2. Paired *t-tests*
Comparing the same unit over time (e.g., before/after a policy change).

### 3. ANOVA or comparisons across >2 groups
Testing whether more than two neighborhoods differ meaningfully.


> **Returning to the Case:** The San Marcos growth case requires multiple tools working in sequence. An independent *t*-test could compare current staffing ratios in San Marcos against a pooled sample of peer cities. A paired *t*-test could evaluate whether permit processing times in the same departments changed before and after a bond-funded hiring initiative. And regression could model which factors---population growth rate, staff-to-population ratio, budget per capita---best predict permit backlog severity. Choosing the right tool for each sub-question is the integrative skill this chapter develops.}

### 4. Regression
Modeling multiple predictors simultaneously (Chapter~*chap:regression*).

You must justify your chosen test based on:


    - the structure of your data,
    - the nature of your research question,
    - the assumptions underlying the statistical method (casella2002statistical, ross2014probability).


> 
**Briefing:** A statistical test is not a flavor choice—it must match the design of your data.


## Step Six: Building and Interpreting Regression Models

Most Final Projects will incorporate regression, whether simple or multiple, and the quality of the project depends heavily on how clearly the model is built and interpreted. For each coefficient, you should state in plain language what it represents: the expected change in the outcome variable for a one-unit increase in the predictor, holding all other variables in the model constant. You should also evaluate whether each predictor is substantively important---not merely statistically significant. A coefficient that is statistically distinguishable from zero but represents a change of 0.1 days in completion time may not warrant a policy recommendation, while a coefficient that is marginally significant but represents a 5-day change might deserve serious attention. Use diagnostics---residual plots, QQ-plots, VIF calculations---to evaluate whether the model's assumptions hold, following the guidance in Chapter~*chap:regression* and the principles emphasized by Gelman and Hill (gelman2007data).

Equally important is what the model does not include. Every regression model omits variables, and your write-up should discuss which omitted variables are most likely to bias your estimates and in which direction. Public-sector data frequently violate the assumptions underlying OLS: observations may be clustered within neighborhoods or departments (violating independence), the spread of residuals may increase with the predicted value (heteroskedasticity), and measurement error in administrative records may attenuate coefficients toward zero (gaoDataQuality, uscensusACS). Address these issues directly rather than hoping the reader will not notice. Finally, exercise caution with causal language. Regression coefficients describe associations; causal claims require research designs---randomization, natural experiments, or instrumental variables---that go beyond what most Final Projects can deliver (angrist1996identification, freedman2007statisticalmodels).

The inferential tools applied in Step Five provide the statistical foundation for the regression work here; now the analyst layers multiple predictors and diagnostics on top of that foundation to build a richer, more nuanced model.


## Step Seven: Presenting Results Clearly

The analytical work is only as valuable as its communication. Your results section should integrate well-labeled tables, informative figures, and clear narrative interpretation into a coherent presentation that a non-specialist reader---a city manager, a budget officer, a council member---can follow without statistical training. Regression tables should include coefficients, standard errors, confidence intervals, and measures of model fit (adjusted $R^2$ at minimum), with clear labels that use variable names a reader can understand ("Debt-to-Revenue Ratio" rather than "X3"). Figures should include scatterplots of key relationships, diagnostic plots that demonstrate the model's assumptions are reasonably satisfied, and trend lines or grouped comparisons that make the story visible at a glance. Visualization principles from Tukey and Cleveland apply directly: every element of a graph should serve the analytical purpose, and chart junk should be eliminated (tukeyEDA, clevelandGraphing).

The narrative that accompanies your tables and figures is where the real interpretation happens. Write results in plain, administrative English: "An additional 10 calls per department per week predicts 3.2 more minutes of average delay, holding staffing constant" is far more useful than "$\beta_1 = 0.32, p < 0.01$." Similarly, "Post-reform response times decreased by 1.7 minutes (95\

Step Seven builds directly on the modeling work of Step Six: the regression results are now translated from technical output into a form that supports decision-making.


## Step Eight: Discussing Limitations and Uncertainty

The strongest projects are not the ones with the most impressive results; they are the ones that most honestly confront the boundaries of their evidence. Your limitations section should address four categories of concern. First, data limitations: incomplete coverage, non-random missingness, measurement error, and changes in data collection procedures over time. If your dataset excludes certain types of incidents, certain time periods, or certain geographic areas, say so explicitly and explain how these gaps might affect your conclusions. Second, model limitations: the functional form you chose may not perfectly capture the true relationship, omitted variables may bias your estimates, and the assumptions underlying your statistical tests may not hold perfectly in your data. Third, uncertainty: report confidence intervals for your key estimates and discuss what those intervals imply about the range of plausible conclusions. A finding that permit processing times increased by 14 days (95\

Manski's warning against "incredible certitude" should guide the tone of your entire discussion (manski2019policy). Acknowledging limitations does not weaken your project; it strengthens it by demonstrating analytical maturity. A reader who sees that you have anticipated the most important objections to your analysis will trust your findings more, not less.

Having presented results clearly in Step Seven and bounded their interpretation in Step Eight, you are ready to translate the analysis into policy-relevant recommendations.


## Step Nine: Writing the Policy-Relevant Discussion

A policy analysis must answer three questions: What did you find? Why does it matter? And what should a public administrator do with this information? The discussion section is where your statistical findings are translated into the language of managerial action. This is the section that a city manager, a department director, or a council member will read most carefully, and it must bridge the gap between technical results and operational decisions.

Your recommendations should be realistic and proportional to the evidence. If your regression shows that each additional staff member per shift reduces average response time by 2.3 minutes, you might recommend that the department pilot an additional position during peak hours and evaluate the results---not that the city immediately hire 50 new employees. If your analysis reveals that service delays are concentrated in disadvantaged neighborhoods, the appropriate recommendation is further investigation into the mechanisms driving the disparity, not a sweeping claim about systemic discrimination that your data cannot fully support (sampson2012great, chetty2016mto). If your before-and-after comparison shows modest improvements following an inspection reform, you might note that digital tools appear promising but that longer follow-up periods and larger samples would strengthen the conclusion. In every case, the tone should be one of informed caution: here is what the evidence suggests, here is how confident we are, and here is a reasonable next step.


> 
**Briefing:** Data analysis becomes public administration when it informs action.


## Step Ten: Structuring the Final Paper

A clear structure:


    - **Introduction**  
          Research question, motivation, short preview.

    - **Background and Theory**  
          Based on organizational or policy context.

    - **Data**  
          Source, variables, limitations.

    - **Descriptive Statistics**  
          Tables, graphs, interpretation.

    - **Methods**  
          Tests and models used, with justification.

    - **Results**  
          Tables, regression output, graphics, interpretation.

    - **Discussion**  
          Relevance, policy insights, implications.

    - **Limitations**  
          Data quality, uncertainty, generalizability.

    - **Conclusion**
          Final message, possible next steps for administrators.


### Annotated Example: A Mini-Project on San Marcos Permit Processing

The following outline illustrates what a completed analysis might look like, using the San Marcos growth case:


    - **Research Question.** Has the average time to process a building permit in San Marcos increased between 2018 and 2023, and does current processing time differ significantly from peer cities?

    - **Data.** Building permit records from the City of San Marcos (2018--2023), including submission date, approval date, and permit type. Peer-city data from New Braunfels, Kyle, and Georgetown.

    - **Descriptive Statistics.** Mean and median processing times by year. Histogram showing right-skewed distribution. IQR increasing from 12 days (2018) to 28 days (2023), suggesting growing backlog variability.

    - **Inferential Test.** Paired *t*-test comparing same-month processing times in 2018 vs.\ 2023 ($n = 12$ monthly averages). Result: $D} = 14.2$ days, $t = 3.81$, $p = 0.003$. The increase is statistically significant.

    - **Regression.** Multiple regression of processing time on applications per staff member, permit type, and month. Key finding: each additional 5 applications per staff member is associated with a 3.2-day increase in processing time ($p = 0.01$), controlling for permit complexity.

    - **Limitations.** Data do not capture informal pre-submission consultations. Staff turnover is not measured directly. Peer-city data may use different definitions of "processing time."

    - **Policy Discussion.** The staffing coefficient suggests that adding one full-time planner (reducing the applications-per-staff ratio by approximately 8) could reduce average processing time by roughly 5 days. This is a modest but operationally meaningful improvement for a city where permit delays have become a public concern.


This example is not a template to copy. It is a model of the *reasoning process*: question drives data, data drive method, method drives finding, finding drives recommendation. Every step is transparent, every limitation is acknowledged, and the conclusion is proportional to the evidence.


## Final Advice

The Final Project is where technique becomes applied judgment. Throughout this course, you have learned to describe data, reason about uncertainty, test hypotheses, compare groups, and model relationships among multiple variables. The Final Project asks you to deploy all of these skills in a single, integrated analysis---and, crucially, to exercise the kind of analytical judgment that no formula can provide. As Gelman and Hill observe, good analysis requires a blend of statistical reasoning, contextual understanding, clarity of communication, respect for uncertainty, and an appreciation for how public agencies actually function (gelman2007data).

The most common mistake in student projects is not technical error but a failure of integration. Students produce competent descriptive statistics, run a correct hypothesis test, and fit a reasonable regression---but treat each as an isolated exercise rather than building each step on the one before it. A strong project tells a story: the research question motivates the data, the descriptive statistics reveal patterns that the inferential tests then evaluate, the regression model quantifies the relationships the earlier steps identified, and the discussion connects the statistical findings back to the original policy concern. Every section should reference what came before and anticipate what comes next.

A second common mistake is overreach. Students who find a statistically significant result sometimes write as though they have proven a causal relationship or solved a policy problem. The strongest projects are the ones that state their findings clearly, bound them with appropriate uncertainty, and resist the temptation to claim more than the evidence supports. A well-crafted sentence like "Our results are consistent with the hypothesis that staffing increases reduce response times, though the observational design does not rule out alternative explanations" demonstrates far more analytical sophistication than a confident but unsupported causal claim.

Finally, remember that the audience for your work is not your statistics instructor---it is a public administrator who needs to make a decision. Write in clear, direct prose. Define technical terms when you use them. Present tables and figures that a non-specialist can interpret. And always connect your findings to the question that motivated the analysis in the first place. If you can define a question clearly, use data responsibly, interpret uncertainty transparently, and connect results to public-sector decisions, you will have produced work that reflects the best traditions of evidence-informed public administration.


> 
**Briefing:** The goal is not perfection—it is rigor, clarity, and usefulness.


## Practice and Application


    - **Mini-project.** Using either the voter turnout, EMS, or weather dataset from the appendices, complete the following in no more than 3 pages: (a) state a research question, (b) describe the data and its limitations, (c) present descriptive statistics with at least one figure, (d) conduct one inferential test or regression, (e) interpret the results, and (f) write a one-paragraph policy recommendation. This exercise mirrors the structure of the Final Project at reduced scale.