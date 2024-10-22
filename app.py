import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def GeneratePathsGBMABM(NoOfPaths, NoOfSteps, T, r, sigma, S_0):    
    np.random.seed(1)
    
    Z = np.random.normal(0.0, 1.0, [NoOfPaths, NoOfSteps])
    X = np.zeros([NoOfPaths, NoOfSteps+1])
    S = np.zeros([NoOfPaths, NoOfSteps+1])
    time = np.zeros([NoOfSteps+1])
    
    X[:,0] = np.log(S_0)
    
    dt = T / float(NoOfSteps)
    for i in range(0, NoOfSteps):
        if NoOfPaths > 1:
            Z[:,i] = (Z[:,i] - np.mean(Z[:,i])) / np.std(Z[:,i])
        
        X[:,i+1] = X[:,i] + (r - 0.5 * sigma**2) * dt + sigma * np.power(dt, 0.5) * Z[:,i]
        time[i+1] = time[i] + dt
    
    S = np.exp(X)
    paths = {"time": time, "X": X, "S": S}
    return paths

def main():
    st.title("Geometric and Arithmetic Brownian Motion Simulation")

    st.sidebar.header("Parameters")
    NoOfPaths = st.sidebar.slider("Number of Paths", 1, 100, 25)
    NoOfSteps = st.sidebar.slider("Number of Steps", 100, 1000, 500)
    T = st.sidebar.slider("Time Period (years)", 0.1, 5.0, 1.0)
    r = st.sidebar.slider("Risk-free Rate", 0.0, 0.2, 0.05)
    sigma = st.sidebar.slider("Volatility", 0.1, 1.0, 0.4)
    S_0 = st.sidebar.slider("Initial Stock Price", 10, 200, 100)

    Paths = GeneratePathsGBMABM(NoOfPaths, NoOfSteps, T, r, sigma, S_0)
    timeGrid = Paths["time"]
    X = Paths["X"]
    S = Paths["S"]

    fig1, ax1 = plt.subplots()
    for i in range(NoOfPaths):
        ax1.plot(timeGrid, X[i,:])
    ax1.set_xlabel("Time")
    ax1.set_ylabel("X(t)")
    ax1.set_title("Arithmetic Brownian Motion")
    ax1.grid(True)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    for i in range(NoOfPaths):
        ax2.plot(timeGrid, S[i,:])
    ax2.set_xlabel("Time")
    ax2.set_ylabel("S(t)")
    ax2.set_title("Geometric Brownian Motion")
    ax2.grid(True)
    st.pyplot(fig2)

if __name__ == "__main__":
    main()
