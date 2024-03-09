# pydrc: Python Dose-Response Curves

![Python_project_logo](https://github.com/Mr-Mathias-F/pydrc/assets/74455376/47543590-e776-43cd-a53f-c150eb495069)


pydrc is a powerful Python package specially designed for the analysis and visualization of dose-response data in fields like toxicology, pharmacology, and environmental sciences. 

The package simplifies the process of implementing various dose-response models, offering a uniform interface for a wide range of common models, including but not limited to Hill, Logistic, Gompertz models, and more.

## Key Features
- **Wide Range of Models**: Implementation of a broad selection of dose-response models.
- **Robust Estimation**: Parameter estimation using state-of-the-art optimization algorithms.
- **Model Evaluation**: Tools for the evaluation of model performance and selection.
- **Data Visualization**: Aesthetic and intuitive visualization of dose-response curves using Matplotlib and Seaborn.
- **Flexibility**: Capability to handle user-defined models.

Built for the scientific community, pydrc bridges the gap between intricate dose-response analyses and Python's ease of use, empowering researchers to concentrate on interpreting results instead of wrestling with the coding of analyses.

Contributions are welcome.

## Example

The four-parameter model can be represented as:

\[
y = a + \frac{{b - a}}{{1 + (x / c)^d}}
\]

where:
- \( y \) is the response variable,
- \( x \) is the predictor variable,
- \( a \) is the lower asymptote,
- \( b \) is the upper asymptote,
- \( c \) is the half-maximum value of \( x \),
- \( d \) is the slope parameter.




## Todo

- Implemention of multiple optimization algorithms for existing functions 
- Summary tables for parameter estimates
- Early implementation for dose-response curve visualization in Matplotlib and Seaborn 

