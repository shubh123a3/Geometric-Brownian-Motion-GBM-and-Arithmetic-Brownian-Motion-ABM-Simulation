# Geometric Brownian Motion (GBM) and Arithmetic Brownian Motion (ABM) Simulation

## Overview

This project provides an interactive Streamlit application for simulating and visualizing both Geometric Brownian Motion (GBM) and Arithmetic Brownian Motion (ABM). It's a powerful tool for understanding and exploring key concepts in financial modeling, particularly in asset price movement simulation.

Live Demo: [abm-gbm.streamlit.app](https://abm-gbm.streamlit.app/)


https://github.com/user-attachments/assets/2f2b1e7a-8524-4b49-aa02-e1d4bb71ac11


## Features

- Monte Carlo simulation of asset price paths using both GBM and ABM
- Interactive parameter adjustment via Streamlit interface
- Real-time visualization of simulation results
- Adjustable parameters include:
  - Number of paths
  - Number of time steps
  - Volatility
  - Initial price
- Educational tool for understanding stochastic processes in finance

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/shubh123a3/Geometric-Brownian-Motion-GBM-and-Arithmetic-Brownian-Motion-ABM-Simulation.git
   cd Geometric-Brownian-Motion-GBM-and-Arithmetic-Brownian-Motion-ABM-Simulation
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:


This will open the application in your default web browser. Use the sidebar to adjust simulation parameters and observe the real-time changes in the visualizations.

## Files in the Repository

- `ABM_GBM.ipynb`: Jupyter notebook containing the core simulation logic and initial development
- `app.py`: Streamlit application script
- `requirements.txt`: List of Python dependencies
- `results/`: Directory containing output images or data (if any)

## Theory

The application simulates two types of Brownian motion:

1. **Geometric Brownian Motion (GBM)**: 
   Commonly used to model stock prices in financial markets.

2. **Arithmetic Brownian Motion (ABM)**:
   A simpler model that allows for negative values, less commonly used for asset prices but useful in other contexts.

Both models are crucial in understanding random walks and stochastic processes in finance and other fields.

## Contributing

Contributions to improve the application or extend its functionality are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source. Please check the repository for license details.

## Acknowledgments

- Streamlit for providing an excellent framework for interactive Python applications
- The quantitative finance community for ongoing research and development in stochastic modeling

## Contact

For any queries or discussions related to this project, please open an issue in the GitHub repository.

