---
layout: page
title: "Chapter 8"
permalink: /docs/chapter8/
---

# Regression Analysis


> **Course dataset & lab.** Work this chapter's techniques on our spine dataset — [Texas City Sales Panel](../datasets). Regress `sales_tax_alloc` on `taxable_sales`, then add a second predictor; see omitted-variable bias.


## Epigraphs


> 
*"All models are wrong, but some are useful."*

 George Box


> 
*"The greatest value of a picture is when it forces us to notice what we never expected to see."*

 John Tukey (Tukey 1977)


Regression is the backbone of modern quantitative analysis in public administration.  
It is used to forecast demand, evaluate equity, estimate performance, analyze neighborhood
variation, and assess policy impact. Yet, as Box warns, regression models are approximations.
Their value depends on thoughtful construction, careful diagnostics, and an understanding of the
administrative systems from which data arise (Freedman 2007; Einav & Levin 2014).

This chapter introduces both simple and multiple regression---tools that transform raw data into
structured, interpretable relationships while respecting uncertainty (Chapter 5).


## Opening Case: What Determines a Texas City's Credit Rating?


When Texas cities need to build roads, expand water systems, or renovate public buildings, they typically issue municipal bonds. The interest rate they pay depends heavily on their credit rating---a score assigned by agencies like Moody's and Standard & Poor's that reflects the city's fiscal health and repayment capacity. In reporting on municipal finance across Texas, the Texas Tribune documented how mid-size cities with similar populations sometimes received markedly different ratings, translating into borrowing cost differences of millions of dollars over the life of a bond (Texas Tribune).

The natural analytical question is: which fiscal variables best predict a city's creditworthiness? Candidates include the general fund balance as a share of expenditures, total debt relative to revenue, revenue diversification (the degree to which a city relies on a single source like property tax versus a mix of sales tax, fees, and intergovernmental transfers), population growth trajectory, and pension funding levels. A simple regression of credit rating on any single predictor---say, debt-to-revenue ratio---might show a strong negative relationship. But omitting pension obligations or fund balance from the model could bias the coefficient, because cities with high debt loads sometimes also have strong reserves that mitigate risk.

This case sets up the core machinery of regression analysis. The outcome variable (credit rating or borrowing cost spread) is continuous. The predictors are multiple and potentially correlated. Omitted variable bias, multicollinearity, and the interpretation of "holding other variables constant" are not abstract concerns---they are the difference between a useful fiscal model and a misleading one.


**Guiding Questions**


    - Which fiscal variables would you include in a regression model to predict a Texas city's credit rating---and why?
    - If a simple regression of credit rating on debt-to-revenue ratio shows a strong negative relationship, what omitted variables might bias this estimate?
    - How would you interpret a coefficient that says "each additional percentage point of fund balance ratio is associated with a 0.3-point improvement in credit rating, holding other factors constant"?


## Why Regression Matters in Public Administration

Public-sector questions often involve relationships among variables:


    - Do call volumes predict 311 service delays? (City of Austin open data)
    - Do staffing levels influence EMS response times? (Texas DSHS EMS data)
    - Do neighborhood characteristics explain disparities in service delivery?
          (Sampson 2012; Chetty et al. 2016)
    - Do economic indicators forecast revenue collections? (BLS)
    - Does digital recordkeeping reduce inspection duration?


Regression analysis quantifies these relationships and provides tools for inference, prediction,
and explanation (Gelman & Hill 2007; Hastie et al. 2009).


> 
**Briefing:** Regression links descriptive statistics, probability, and causality.


## Simple Linear Regression

The simplest regression model describes the relationship between an outcome $Y$ and a predictor $X$:


$$
Y_i = \beta_0 + \beta_1 X_i + \varepsilon_i.
$$


Ordinary least squares (OLS) estimates coefficients that minimize squared differences between observed and predicted values.

Interpretation:


    - $\beta_0$ — expected $Y$ when $X=0$.
    - $\beta_1$ — expected change in $Y$ for a one-unit change in $X$.


Examples:


    - Each additional 311 call is associated with added delay (City of Austin open data).
    - Each additional EMS staff member reduces response time (Texas DSHS EMS data).
    - Higher neighborhood disadvantage predicts longer delays (Sampson 2012).


Interpreting regression coefficients requires care.  
Freedman emphasizes that regression is a descriptive method unless strong assumptions support causal
claims (Freedman 2007).


## The Error Term

The error term $\varepsilon_i$ captures:


    - randomness in administrative processes (Einav & Levin 2014),
    - omitted variables (weather, seasonality),
    - measurement error (GAO; U.S. Census ACS),
    - institutional variation across neighborhoods (Sampson 2012).


Understanding the error structure is key to credible modeling.


> 
**Briefing:** Regression models what you include—and hides what you omit.


## From Simple to Multiple Regression

Simple regression observes the slope of one predictor.  
But public-sector outcomes rarely depend on a single factor.

Multiple regression models allow simultaneous analysis of several predictors:


$$
Y_i = \beta_0 + \beta_1 X_{1i} + \beta_2 X_{2i} + \cdots + \beta_k X_{ki} + \varepsilon_i.
$$


This framework isolates the relationship between each predictor and $Y$ while adjusting for confounding variables, improves the precision of estimated effects by accounting for additional sources of variation, and supports both policy analysis and forecasting by incorporating the multiple factors that jointly determine public-sector outcomes.

Gelman and Hill argue that multivariable models are essential for understanding complex,
multilevel public-sector processes (Gelman & Hill 2007).


## Interpreting Coefficients in Multiple Regression

Each coefficient $\beta_j$ represents:


$$
\text{the expected change in } Y \text{ for a one-unit increase in } X_j, \text{ holding all other variables constant}.
$$


Examples:


    - Controlling for weather and staffing, does call volume still predict 311 delays?
    - Holding distance constant, does EMS staffing reduce response time?
    - Controlling for income, does housing tenure predict neighborhood variation 
          in delays? (Sampson 2012)
    - Controlling for economic indicators, does population growth predict revenue? (BLS)


This “all else equal” interpretation is powerful—but can mislead if important variables are omitted
(Freedman 2007).


## Omitted Variable Bias (OVB)

Omitting relevant predictors biases coefficients:


$$
\hat{\beta}_1 = \beta_1 + \underbrace{\beta_2\,\frac{\text{Cov}(X_1, X_2)}{\text{Var}(X_1)}}_{\text{bias term}}.
$$


This occurs when:


    - workload and staffing correlate,
    - neighborhood disadvantage correlates with municipal investment (Sampson 2012),
    - economic conditions correlate with revenues (BLS).


Angrist and Imbens’s identification framework stresses that interpretation demands attention to such
sources of confounding (Angrist & Imbens 1996).


> **Returning to the Case:** In the Texas city credit rating case, a simple regression of credit rating on debt-to-revenue ratio might show a strong negative coefficient. But cities with high debt often issued that debt to fund infrastructure that boosted economic growth and tax revenue---and they may also maintain substantial reserve funds precisely because they are fiscally sophisticated borrowers. Omitting fund balance ratio and revenue growth from the model would bias the debt coefficient, making high debt appear more harmful to creditworthiness than it actually is when accompanied by strong fiscal management.

### Worked Example: Credit Ratings and Fiscal Variables

> **On course data:** fund balance isn't available in free public data. To reproduce an omitted-variable-bias story on the course dataset, use the 2022 finance cross-section and regress `total_debt_os` on `total_taxes`, then add `population` — the tax coefficient drops sharply because taxes and population are highly correlated.

Consider data on 10 Texas cities. The two regression models estimated from these data are summarized below.

| Predictor | Model 1 (simple) | Model 2 (multiple) |
|---|---|---|
| Intercept | 104.2 | 78.5 |
| Debt/Revenue | −52.3 | −28.1 |
| Fund Balance | — | 0.95 |
| $R^2$ | 0.93 | 0.97 |

*Coefficients are taken from the two model equations below; the underlying 10-city dataset is not reproduced here.*


**Model 1: Simple regression.**
Regressing credit score on debt-to-revenue ratio alone:

$$
\widehat{\text{Score}} = 104.2 - 52.3 \times \text{Debt/Revenue} \qquad R^2 = 0.93
$$

Each 0.10 increase in debt-to-revenue is associated with a 5.2-point decline in credit score. This looks like a strong, clean result.

**Model 2: Multiple regression.**
Adding fund balance ratio:

$$
\widehat{\text{Score}} = 78.5 - 28.1 \times \text{Debt/Revenue} + 0.95 \times \text{Fund Balance} \qquad R^2 = 0.97
$$

The debt coefficient *drops from $-52.3$ to $-28.1$*. Why? Because debt-to-revenue and fund balance are negatively correlated: cities with high debt often have lower reserves. In Model 1, the debt coefficient absorbed part of the fund balance effect. This is OVB in action.

**Interpretation.**
The simple regression overstated the harm of debt by nearly a factor of two. After controlling for fund balance, high debt still predicts lower credit scores, but the relationship is substantially weaker. A city manager who relied on Model 1 to argue against *any* borrowing would be misled. In Excel, use `Data Analysis > Regression` to fit both models and compare coefficients.


*Figure: Scatterplot of credit score against debt-to-revenue ratio, with the Model 1 and Model 2 fitted regression lines overlaid.*


> 
**Briefing:** If you ignore a relevant variable, your regression will not ignore it—it will distort other coefficients.


## Categorical Predictors (Dummy Variables)

Many public-sector predictors are categorical rather than continuous: a neighborhood is urban or rural, an inspection follows paper or digital procedures, a service request falls into one of several department categories, and a fiscal year either precedes or follows a policy reform. Regression requires numerical inputs, so analysts convert categorical variables into indicator (or "dummy") variables that take the value 1 when a unit belongs to a category and 0 otherwise.

The simplest case involves a binary predictor. Consider a model of EMS response time that includes an urban-rural indicator:


$$
\text{Urban}_i =
\begin{cases}
1 & \text{if urban}\\
0 & \text{if rural}
\end{cases}
$$


In the regression $Y_i = \beta_0 + \beta_1 \text{Urban}_i + \varepsilon_i$, the intercept $\beta_0$ represents the average response time for rural units (where $\text{Urban} = 0$), and $\beta_1$ represents the average difference in response time between urban and rural units. If $\beta_1 = -3.2$, urban stations respond 3.2 minutes faster on average. When additional predictors are included in a multiple regression, $\beta_1$ becomes the urban-rural difference *holding those other variables constant*---a critical distinction for equity analysis.

When a categorical variable has more than two levels, analysts create one dummy variable for each category except one, which serves as the reference group. For example, if service requests fall into four categories---infrastructure, animal control, code compliance, and parks---the analyst creates three dummy variables and omits one category (say, infrastructure) as the baseline. Each coefficient then represents the average difference between that category and the reference category, controlling for other predictors. The choice of reference group does not affect the model's overall fit or predictions, but it does determine how coefficients are interpreted, so analysts should choose a reference group that provides the most meaningful comparisons for the policy question at hand.

Dummy variables are essential for equity analysis in public administration. By including neighborhood demographic indicators as categorical predictors, analysts can estimate whether service delivery differs across community types after accounting for workload, staffing, and other operational factors---an approach consistent with the frameworks developed by Sampson and Chetty for studying structural inequities across neighborhoods (Sampson 2012; Chetty et al. 2016). In Excel, dummy variables are created by adding columns of 0s and 1s to the dataset before running Data Analysis $>$ Regression.


## Interactions

In a standard multiple regression, each predictor has the same effect on the outcome regardless of the values of the other predictors. But in many public-sector settings, the effect of one variable depends on the level of another. Interactions allow the analyst to model this dependence explicitly.

An interaction term is constructed by multiplying two predictors together and including the product as an additional variable in the regression:


$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_1X_2 + \varepsilon.
$$


In this model, the effect of $X_1$ on $Y$ is no longer simply $\beta_1$; it is $\beta_1 + \beta_3 X_2$, which changes depending on the value of $X_2$. Similarly, the effect of $X_2$ on $Y$ is $\beta_2 + \beta_3 X_1$. The coefficient $\beta_3$ captures how much the effect of one predictor changes per unit increase in the other.

Consider a concrete example. Suppose an EMS analyst models response time as a function of staffing level and call volume, with an interaction between the two. The model might yield $\beta_{\text{staffing}} = -2.0$, $\beta_{\text{volume}} = 0.8$, and $\beta_{\text{staffing} \times \text{volume}} = -0.15$. The interpretation is that each additional staff member reduces response time by 2.0 minutes at average call volume, but the reduction is even larger during high-volume periods (because $-0.15$ is negative, higher volume amplifies the benefit of staffing). This finding would be invisible in a model without the interaction term, which would estimate a single, averaged staffing effect regardless of demand conditions.

Interactions can also involve categorical predictors. If the analyst includes a dummy variable for whether a department has adopted digital recordkeeping and interacts it with workload, the model estimates separate workload slopes for digitally equipped and non-digital departments. This directly answers the question: does digital adoption change how workload affects processing time?

Interpreting interactions requires care. The individual coefficients $\beta_1$ and $\beta_2$ no longer represent "main effects" in the usual sense; they represent the effect of each variable when the other variable equals zero. If zero is not a meaningful value for the interacted variable (for example, if no station has zero call volume), the individual coefficients may not have a useful substantive interpretation on their own. Analysts should center continuous variables (subtract the mean) before creating interaction terms to make the individual coefficients more interpretable. In Excel, create the interaction by adding a new column that multiplies the two predictor columns, then include all three columns---the two original predictors and the product---in the regression.


## Model Fit and Evaluation

Standard metrics:

### 1. $R^2$

Proportion of variance explained by the model.  
But $R^2$ always rises with additional predictors.

### 2. Adjusted $R^2$

Penalizes unnecessary predictors—more appropriate for comparing models.

### 3. Information Criteria

AIC, BIC—useful for model comparison.

### 4. Prediction Error

Cross-validation methods (introduced in Hastie et al. 2009) help assess
generalizability.


> 
**Briefing:** A good model explains the data without memorizing it.


## Diagnostics in Multiple Regression

Regression output is only as trustworthy as the assumptions behind it. Diagnostics are the tools analysts use to check whether those assumptions hold---and to determine what to do when they do not. Skipping diagnostics is one of the most common and consequential errors in applied work (Freedman 2007; Wooldridge 2019). The following subsections describe each major diagnostic, explain what a good result looks like versus a problematic one, and offer practical guidance for administrative data.

### Residual Plots and Heteroskedasticity

After fitting a regression, the analyst should plot the residuals (observed $y$ minus predicted $\hat{y}$) against the predicted values. In a well-specified model, this plot shows a random scatter of points around zero with roughly constant vertical spread. If the spread of residuals increases or decreases systematically as the predicted value changes---a pattern called heteroskedasticity---then the standard errors are unreliable, and confidence intervals and $p$-values may be misleading. In administrative data, heteroskedasticity is common: larger cities generate more variable outcomes than smaller ones, and high-volume departments show more spread in completion times than low-volume ones. When heteroskedasticity is present, the analyst should use robust (heteroskedasticity-consistent) standard errors, which are available in Excel's regression output by using add-ins or computing them manually (Stock & Watson 2019). In the credit rating example, one would expect residuals to be larger for mid-range cities (where fiscal characteristics vary widely) than for the strongest or weakest performers.


*Figure: Residuals-versus-fitted plot illustrating a fan-shaped pattern characteristic of heteroskedasticity.*


### QQ-Plots for Normality

A quantile-quantile (QQ) plot compares the distribution of residuals to the theoretical normal distribution. If residuals are approximately normal, the points fall close to a 45-degree line. Departures at the tails---points curving away from the line at the extremes---indicate heavy tails or skewness. While regression coefficients remain unbiased even when residuals are non-normal (provided the sample is large enough for the Central Limit Theorem to apply), confidence intervals and hypothesis tests based on the $t$-distribution assume approximate normality. In administrative data, non-normality is common because operational processes produce right-skewed distributions with occasional extreme values. When the QQ-plot reveals substantial departures, the analyst might consider transforming the dependent variable (e.g., using the natural logarithm of response time rather than response time itself) or relying on bootstrapped standard errors (Agresti 2018).

### Variance Inflation Factors (VIF)

Multicollinearity arises when two or more predictors are highly correlated, making it difficult to isolate the independent effect of each. The VIF quantifies this problem: a VIF of 1 indicates no collinearity, values between 1 and 5 are generally acceptable, and values above 10 signal serious concern (Wooldridge 2019). In the credit rating model, debt-to-revenue ratio and fund balance are negatively correlated (cities with high debt often have low reserves), which inflates both variables' VIFs and widens their confidence intervals. When VIF is high, the analyst should consider dropping one of the correlated predictors, combining them into an index, or accepting that the individual coefficients are imprecise while the overall model fit ($R^2$) remains valid. In Excel, VIF can be computed by regressing each predictor on all other predictors and calculating $\text{VIF}_j = \frac{1}{1 - R_j^2}$.

### Outliers and Leverage Points

Not all observations exert equal influence on the regression line. An outlier has an unusual $y$-value given its $x$-values; a high-leverage point has an unusual combination of $x$-values. A point that is both an outlier and high-leverage can disproportionately pull the regression line toward itself, distorting coefficients for the entire model (Anscombe 1973). In the credit rating analysis, Houston (the largest city by population) may exert substantial leverage simply because its fiscal characteristics are far from the average Texas city's. The analyst should examine Cook's distance (a combined measure of outlier status and leverage) and consider whether influential observations reflect genuine data or errors. Removing an observation should be a last resort, justified by substantive reasoning rather than statistical convenience.

### Nonlinearity

OLS regression assumes a linear relationship between each predictor and the outcome. Scatterplots of $y$ against each $x$ (and of residuals against each $x$) help detect nonlinear patterns (Cleveland 1993). If the relationship between debt ratio and credit score is not linear---for example, if credit scores decline slowly at low debt but rapidly at high debt---then a linear model will systematically over-predict at the extremes and under-predict in the middle. Remedies include adding polynomial terms (e.g., debt-ratio-squared), using logarithmic transformations, or fitting a piecewise linear model with different slopes above and below a threshold.

### Clustering and Dependence

Administrative datasets often have hierarchical structure: schools within districts, neighborhoods within cities, months within years. When observations within a cluster are more similar to each other than to observations in other clusters, standard errors from OLS are too small, producing misleadingly narrow confidence intervals and artificially significant $p$-values (Gelman & Hill 2007). Clustered standard errors (available in statistical software, though not directly in Excel's Data Analysis ToolPak) adjust for this dependence. At minimum, the analyst should acknowledge the clustering structure and note that standard errors may be underestimated.


> **Returning to the Case:** In the credit rating model, a comprehensive diagnostic review would proceed as follows. First, plot residuals against predicted credit scores to check for heteroskedasticity---expect wider residuals for mid-range cities. Second, examine the QQ-plot; credit scores are bounded, so residuals may show light tails. Third, compute VIF for debt ratio and fund balance; if VIF exceeds 5, consider an index combining both. Fourth, check Cook's distance for Houston, Dallas, and San Antonio, which may dominate the regression. Each diagnostic informs whether the model's conclusions about fiscal predictors can be trusted---and what adjustments to make when they cannot.


## Applications in Public Administration

### 1. Modeling 311 Delays

A city's 311 system generates thousands of service requests per month, and regression provides the framework for understanding why some requests take days while others take weeks. An analyst might regress completion time on call volume per department, staffing levels during the relevant shift, time of day, request category, and neighborhood characteristics such as population density or housing age. The resulting model can reveal, for example, that each additional 50 requests in a department's weekly queue is associated with a 1.4-day increase in average completion time, holding staffing constant. Such a finding gives a department director a concrete basis for requesting temporary staff during high-volume periods. Without regression, the director would be left arguing from anecdote rather than evidence (City of Austin open data).

### 2. EMS Response Time Models

Emergency medical services operate under strict time constraints where minutes can determine patient outcomes, making regression an essential tool for identifying which operational factors drive performance. A multiple regression model might include distance from the nearest station to the incident, the number of paramedics on duty, call severity (as classified by the dispatcher), time of day, and day of week. Results from such a model could show that distance is the dominant predictor in rural counties while staffing levels matter more in urban settings where distances are short but call volumes are high. These findings inform resource allocation decisions: a county that discovers staffing is the binding constraint can focus on hiring, while one where distance dominates may benefit more from adding a satellite station (Texas DSHS EMS data).

### 3. Equity Evaluation

Regression is one of the most powerful tools available for detecting and documenting structural inequities in public service delivery. An analyst examining whether neighborhoods with higher poverty rates experience longer 311 completion times can regress completion time on poverty rate while controlling for request type, department workload, and seasonal demand. If the poverty-rate coefficient remains positive and statistically significant after these controls, the finding suggests that the disparity is not simply a byproduct of request mix or staffing cycles but may reflect deeper structural or operational patterns that warrant further investigation. Sampson's research on neighborhood effects and Chetty's work on spatial inequality both demonstrate that such disparities tend to persist across time and policy regimes, making regression-based equity audits a recurring need rather than a one-time exercise (Sampson 2012; Chetty et al. 2016).

### 4. Budget Forecasting

Municipal revenue depends on a web of economic indicators that interact in complex ways, and multiple regression allows budget analysts to model these relationships simultaneously. A forecasting model for sales tax revenue might include regional employment levels, consumer confidence indices, population growth, inflation rates, and seasonal indicators. By estimating how each predictor contributes to revenue while holding the others constant, the model produces forecasts that are more accurate and more transparent than single-indicator projections. A budget office that relies on population growth alone, for example, might overestimate revenue during a recession when employment drops even as the population continues to grow. The multiple regression approach forces the analyst to account for these competing forces explicitly (BLS).

### 5. Administrative Process Improvement

Regression helps administrators identify which operational changes actually improve efficiency and which are merely correlated with improvement. Consider an agency that recently adopted digital recordkeeping for building inspections. A regression of inspection duration on digital adoption (coded as a dummy variable), inspector experience, workload per inspector, building complexity, and shift schedule can isolate the effect of digital tools from confounding factors. If experienced inspectors adopted digital tools first, a simple before-and-after comparison would overstate the technology's benefit by conflating it with inspector skill. The regression model separates these effects, potentially revealing that digital tools reduce inspection time by 12 minutes on average but that inspector experience has an even larger effect. Such findings help an agency decide whether to invest further in technology, in training, or in both (Einav & Levin 2014; GAO).


## Common Pitfalls

### 1. Overinterpreting Coefficients

A regression coefficient describes an association between a predictor and an outcome, not a causal effect. When an analyst reports that higher neighborhood poverty rates are associated with longer 311 completion times, this does not mean that poverty *causes* delays; poverty may be correlated with infrastructure age, staffing patterns, or reporting behavior, any of which could be the actual driver. Freedman emphasizes that causal claims require design-based arguments---randomization, natural experiments, or instrumental variables---that go well beyond what OLS regression alone provides (Freedman 2007). Analysts should use language such as "is associated with" or "predicts" rather than "causes" or "leads to" unless the research design supports stronger claims.

### 2. Multicollinearity

When two or more predictors are highly correlated, the regression has difficulty separating their individual contributions, resulting in inflated standard errors and unstable coefficients. In the credit rating model, for example, debt-to-revenue ratio and fund balance ratio are strongly negatively correlated; including both in the model may produce large standard errors for each, even though the model as a whole fits well. Analysts should check VIFs and consider whether combining correlated predictors into an index or dropping one is more appropriate than retaining both with imprecise estimates.

### 3. OVB

When a relevant predictor is left out of the model, the coefficients on the included variables absorb its effect, producing biased estimates. This is not a minor technical concern; it can reverse the apparent direction of a relationship. If an analyst models EMS response time as a function of call volume alone but omits distance (which is correlated with both volume and response time), the call-volume coefficient will be biased in the direction of distance's effect (Angrist & Imbens 1996). The OVB formula introduced earlier in this chapter provides a way to anticipate the direction and magnitude of this distortion, and analysts should always ask what important variables their data do not contain.

### 4. Incorrect Functional Form

OLS assumes a linear relationship between each predictor and the outcome, but many administrative relationships are nonlinear. The effect of staffing on response time, for instance, may diminish at high staffing levels (adding the 20th paramedic helps less than adding the 5th), producing a curved relationship that a linear model will misrepresent. Tukey's emphasis on exploratory data analysis---plotting residuals, examining scatterplots of each predictor against the outcome---helps detect such misspecification before it distorts conclusions (Tukey 1977). Remedies include logarithmic transformations, polynomial terms, or piecewise linear models.

### 5. Ignoring Design Effects

When regression models use data from complex survey designs---such as the ACS or BLS surveys---standard OLS standard errors are typically too small because they ignore the clustering, stratification, and weighting built into the survey design. An analyst who treats ACS tract-level estimates as simple observations without accounting for their margins of error will produce artificially narrow confidence intervals and overstate the precision of regression coefficients (U.S. Census ACS; BLS). At minimum, analysts should report the margins of error associated with their data sources and discuss how survey design limitations affect the reliability of their regression results.


## Practice and Application


    - Fit a simple regression of 311 delay on call volume.  
          Extend to multiple regression with neighborhood disadvantage and staffing 
          (City of Austin open data; Sampson 2012).

    - Model EMS response times using distance, staffing, and call severity.  
          Conduct diagnostic checks (Texas DSHS EMS data; Tukey 1977).

    - Use ACS data to model tract-level income using education, unemployment, and housing 
          characteristics (U.S. Census ACS).  
          Interpret coefficients in light of margins of error.

    - Evaluate whether digital reforms reduce inspection time after adjusting for workload and 
          staff experience (Einav & Levin 2014; GAO).

    - Compare models using adjusted $R^2$ and discuss uncertainty using Manski’s framework
          (Manski 2019).
    - Download the voter turnout dataset from the [Course Datasets page](../datasets). In Excel, use Data Analysis $>$ Regression to regress county-level turnout rate on population size. Record the coefficient, $R^2$, and $p$-value. Then add a second predictor (election type, coded as 1 = general, 0 = primary). Compare the two models: How does the population coefficient change? What does this tell you about OVB?


## Transition to Chapter Nine

Multiple regression allows analysts to model complex relationships among many variables.  
But public-sector data often exhibit nested structures—residents in neighborhoods, officers in 
precincts, units in districts.  
Chapter 9 integrates all the tools developed in this course, which extend 
regression to these rich administrative contexts.