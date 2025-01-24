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

---

## **Components Overview**

### `components/`
- **`bus.py`**: Defines the structure and properties of buses in the power system.
- **`generator.py`**: Implements generator models, including parameters like power output and voltage setpoints.
- **`load.py`**: Models load characteristics such as active and reactive power demand.
- **`branch.py`**: Represents transmission lines and branch properties like impedance and admittance.

### `algorithms/`
- **`power_flow.py`**: Contains power flow calculation methods (e.g., Newton-Raphson).
- **`fault_analysis.py`**: Implements algorithms for fault detection and analysis.
- **`stability.py`**: Tools for assessing the stability of the power system.

### `data/`
- Includes predefined IEEE test system data for various standard bus configurations:
  - `ieee_14.json`: IEEE 14-bus system.
  - `ieee_30.json`: IEEE 30-bus system.
  - `ieee_57.json`: IEEE 57-bus system.
  - `ieee_118.json`: IEEE 118-bus system.

### `utils/`
- **`matrix_utils.py`**: Matrix operations such as forming the admittance matrix.
- **`helpers.py`**: General utility functions for calculations.

### `tests/`
- Unit tests for validating the library functionality:
  - `test_power_flow.py`: Tests for power flow methods.
  - `test_faults.py`: Tests for fault analysis.

### `examples/`
- Demonstrative scripts for using the library:
  - `run_power_flow.py`: Example script for power flow analysis.
  - `analyze_fault.py`: Example script for fault detection.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


