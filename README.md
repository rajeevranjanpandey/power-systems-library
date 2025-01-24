# Power Systems Library

## **Overview**
The **Power Systems Library** is a Python-based framework for performing various power system analyses and calculations. It is designed to support all aspects of power system studies, including power flow, stability, contingency, and fault analysis. The library provides a flexible, modular structure that allows users to easily add new IEEE standard test systems, algorithms, and functionalities.

---

## **Features**
- Support for **IEEE standard test systems**: Includes data for IEEE 14-bus, 30-bus, 57-bus, and 118-bus test systems. Extendable to other systems.
- Core analyses:
  - Power flow analysis (Newton-Raphson, Gauss-Seidel, Fast-Decoupled methods)
  - Fault analysis
  - Stability analysis
  - Contingency analysis
- Modular and reusable components: Includes buses, branches, generators, loads, and their respective attributes.
- Flexible Y-bus and admittance matrix computation.
- Extensible: Add custom algorithms, test systems, and data as needed.
- Ready-to-use example scripts and datasets for quick learning and application.

---

## **Library Structure**
The library follows a modular design to ensure ease of development and future scalability. Below is the folder structure:
power_systems/ ├── components/ # Core definitions for power system components │ ├── bus.py # Bus system models │ ├── generator.py # Generator models │ ├── load.py # Load models │ ├── branch.py # Transmission line models │ ├── algorithms/ # Power system analysis algorithms │ ├── power_flow.py # Power flow methods (Newton-Raphson, etc.) │ ├── fault_analysis.py # Fault studies │ ├── stability.py # Stability calculations │ ├── data/ # IEEE test system data │ ├── ieee_14.json # IEEE 14-bus system data │ ├── ieee_30.json # IEEE 30-bus system data │ ├── ieee_57.json # IEEE 57-bus system data │ ├── ieee_118.json # IEEE 118-bus system data │ ├── utils/ # Utility functions for calculations and operations │ ├── matrix_utils.py # Matrix operations (e.g., admittance matrix) │ ├── helpers.py # General helper functions │ ├── tests/ # Unit tests for validation │ ├── test_power_flow.py # Tests for power flow analysis │ ├── test_faults.py # Tests for fault analysis │ ├── examples/ # Demonstrations of library usage │ ├── run_power_flow.py # Example: Run power flow analysis │ ├── analyze_fault.py # Example: Perform fault analysis │ ├── README.md # Project documentation ├── setup.py # Installation script └── LICENSE # License information


