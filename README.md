# A/B Testing Experiment Analysis

## Project Overview

This project analyses the results of a product A/B test designed to evaluate whether a new website feature increases user conversion rates.

A/B testing is widely used in product-led companies to test product improvements and measure their impact on user behaviour.

The goal of this project was to determine whether the experimental version of a landing page resulted in a statistically significant improvement in conversion rate.

---

## Business Problem

A product team introduced a redesigned landing page and wanted to determine whether the change improved conversion rates.

Users were randomly assigned to:

- Control group – original landing page
- Treatment group – new landing page design

The objective was to determine whether the treatment improved conversion.

---

## Dataset

The dataset contains user-level experiment data including:

- User ID
- Experiment group (control or treatment)
- Page viewed
- Conversion status

---

## Tools Used

- Python
- Pandas
- SciPy
- Matplotlib
- Jupyter Notebook

---

## Experiment Design

Users were randomly split between two groups:

Control Group – Existing product experience  
Treatment Group – New feature implementation

The main metric evaluated was:

Conversion Rate

---

## Analysis

The following steps were performed:

1. Data cleaning and validation
2. Conversion rate calculation for both groups
3. Statistical significance testing using a two-proportion z-test
4. Visualisation of experiment results

---

## Key Results

- Control conversion rate: 12.1%
- Treatment conversion rate: 13.8%
- Relative improvement: 14%

The statistical test showed the difference to be statistically significant at the 95% confidence level.

---

## Business Recommendation

The new landing page design improves user conversion and should be rolled out to all users.

---

## Future Improvements

Future analysis could include:

- Segment-level analysis (e.g. device type, geography)
- Long-term retention impact
- Revenue impact analysis
