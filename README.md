# pydrc: Python Dose-Response Curves

![Python_project_logo](https://github.com/Mr-Mathias-F/pydrc/assets/74455376/47543590-e776-43cd-a53f-c150eb495069)


pydrc is a powerful Python module specially designed for the analysis and visualization of dose-response data in fields like toxicology, pharmacology, and environmental sciences. 

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
toxin_mod = LogisticP4Model(data = toxin_df, x = 'Dose', y = 'Response')
# Fit the model to your data
toxin_mod.fit()
# X the the range of desired predicted values of y (response)
X = np.linspace(0.1, 10000, 10000)
toxin_mod.predict(x = X)
# Plot the final model
toxin_mod.plot() 
```

![Hello_pydrc](https://github.com/Mr-Mathias-F/pydrc/assets/74455376/dec25c93-b73a-44aa-9656-ff168fcb9f90)

| Parameter | Estimate   | Std. Error | t-value    | p-value  |
|-----------|------------|------------|------------|----------|
| b         | 1.467726   | 0.089677   | 16.366838  | 0.000000 |
| c         | 100.320987 | 0.817869   | 122.661497 | 0.000000 |
| d         | 6.261767   | 1.208848   | 5.179944   | 0.000009 |
| e         | 101.744631 | 4.820496   | 21.106674  | 0.000000 |

## Todo

- Implementation of multiple optimization algorithms for existing functions (Current: Levenberg–Marquardt algorithm for unconstrained optimization; Trust Region Reflective for constrained optimization)
- Curve ID argument for summary table and visualization of multiple treatment groups
- Automatic and customizable dose-response curve visualization in Matplotlib and Seaborn with **kwargs  

