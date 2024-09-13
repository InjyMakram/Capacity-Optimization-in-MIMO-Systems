# MIMO System Capacity and Simulation

This repository contains the code and analysis for a project on MIMO (Multiple-Input, Multiple-Output) systems, focusing on calculating channel capacity and simulating MIMO systems with Rayleigh fading.

This project is divided into two main parts:

### Part I: MIMO Channel Capacity and SVD
1. **Singular Value Decomposition (SVD) Calculation**:
   - Hand-derived and implemented code to compute the SVD of a 3x3 MIMO channel matrix.
2. **Water-Filling Algorithm**:
   - Code implementation of the water-filling algorithm to optimize transmit power allocation and maximize channel capacity.
3. **Channel Capacity Calculation**:
   - Computed the capacity of a MIMO channel for both multiplexing and diversity, with and without channel knowledge.

### Part II: MIMO System Simulation with Rayleigh Fading
1. **MIMO Simulation**:
   - Simulated a MIMO system assuming channel state information (CSI) is available at the receiver.
   - Generated channel matrices with Rayleigh fading for multiple realizations.
2. **Ergodic Capacity Calculation**:
   - Used the water-filling solution to compute the ergodic capacity for different numbers of antennas and SNR values.
   - Plotted curves showing the relationship between capacity, SNR, and the number of antennas.

## Features
- **SVD Calculation**: Generalized to work for any channel matrix dimensions and noise power.
- **Water-Filling Algorithm**: Optimizes power allocation across MIMO channels.
- **Rayleigh Fading Channel Simulation**: Models real-world MIMO environments and computes ergodic capacity.
- **Capacity vs SNR Plots**: Visualization of system performance under various conditions.

