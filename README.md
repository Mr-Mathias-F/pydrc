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

## Todo

- Implementation of multiple optimization algorithms for existing functions (Current: Levenberg–Marquardt algorithm for unconstrained optimization; Trust Region Reflective for constrained optimization)
- Implement superfunction for data input, variable arguments and specified function to be optimized (built-in functions for now)
- Introduce functions for effective dose estimation and benchmark dosing
- Curve ID argument for summary table and visualization of multiple treatment groups
- Automatic and customizable dose-response curve visualization in Matplotlib and Seaborn with ****kwargs**
- Integrating and testing each function

