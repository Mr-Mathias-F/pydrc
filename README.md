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


```
# Include your DataFrame, dose- or concentration variable, and response variable
toxin_mod = LogisticP4Model(data = toxin_df, x = 'Dose', y = 'Response)
# Fit the model to your data
toxin_mod.fit()
# X the the range of desired predicted values of y (response)
toxin_mod.predict(x = X)
# Plot the final model
toxin_mod.plot() 
```
![Hello_pydrc](https://github.com/Mr-Mathias-F/pydrc/assets/74455376/4610b5f6-7592-44fa-bf13-e5342ae90761)


## Todo

- Implemention of multiple optimization algorithms for existing functions 
- Summary tables for parameter estimates
- Early implementation for dose-response curve visualization in Matplotlib and Seaborn 

