
import numpy as np

def load_flow(bus_data, branch_data):
    """
    Perform Newton-Raphson power flow analysis.

    Parameters:
        bus_data: dict
            Bus system data containing bus types, loads, and generation.
        branch_data: list of dicts
            Transmission line data containing line impedances and connections.

    Returns:
        dict
            Voltage magnitudes and angles at each bus.
    """
    # Extract data
    num_buses = len(bus_data["bus_type"])
    bus_type = bus_data["bus_type"]
    Pd = bus_data["Pd"]
    Qd = bus_data["Qd"]
    Pg = bus_data["Pg"]
    Qg = bus_data["Qg"]
    Y_bus = calculate_admittance_matrix(num_buses, branch_data)

    # Initial guesses
    V = np.ones(num_buses, dtype=complex)  # Flat start
    for i in range(num_buses):
        if bus_type[i] == "PV":
            V[i] = np.abs(bus_data["Vm"][i])
        elif bus_type[i] == "Slack":
            V[i] = bus_data["Vm"][i] * np.exp(1j * np.radians(bus_data["Va"][i]))

    tolerance = 1e-6
    max_iterations = 50
    for iteration in range(max_iterations):
        # Calculate power mismatches
        P_calc = np.real(V * np.conj(Y_bus @ V))
        Q_calc = np.imag(V * np.conj(Y_bus @ V))

        dP = Pd - P_calc
        dQ = Qd - Q_calc

        mismatches = []
        for i in range(num_buses):
            if bus_type[i] == "PQ":
                mismatches.extend([dP[i], dQ[i]])
            elif bus_type[i] == "PV":
                mismatches.append(dP[i])

        if np.linalg.norm(mismatches) < tolerance:
            print(f"Converged in {iteration} iterations")
            break

        # Jacobian matrix
        J = calculate_jacobian(V, Y_bus, num_buses, bus_type)
        corrections = np.linalg.solve(J, mismatches)

        # Update voltage magnitudes and angles
        idx = 0
        for i in range(num_buses):
            if bus_type[i] != "Slack":
                V[i] *= np.exp(1j * corrections[idx])  # Update angle
                idx += 1
                if bus_type[i] == "PQ":
                    V[i] = np.abs(V[i]) + corrections[idx]  # Update magnitude
                    idx += 1

    return {
        "Vm": np.abs(V),
        "Va": np.degrees(np.angle(V)),
    }


def calculate_admittance_matrix(num_buses, branch_data):
    """
    Build the admittance matrix from branch data.

    Parameters:
        num_buses: int
            Number of buses in the system.
        branch_data: list of dicts
            Transmission line data.

    Returns:
        np.ndarray
            N x N admittance matrix.
    """
    Y_bus = np.zeros((num_buses, num_buses), dtype=complex)
    for branch in branch_data:
        from_bus = branch["from_bus"] - 1
        to_bus = branch["to_bus"] - 1
        Z = branch["z"]
        Y_shunt = branch["y_shunt"]
        Y_line = 1 / Z

        Y_bus[from_bus, from_bus] += Y_line + Y_shunt
        Y_bus[to_bus, to_bus] += Y_line + Y_shunt
        Y_bus[from_bus, to_bus] -= Y_line
        Y_bus[to_bus, from_bus] -= Y_line

    return Y_bus


def calculate_jacobian(V, Y_bus, num_buses, bus_type):
    """
    Calculate the Jacobian matrix for the Newton-Raphson power flow method.

    Parameters:
        V: np.ndarray
            Voltage vector.
        Y_bus: np.ndarray
            Admittance matrix.
        num_buses: int
            Number of buses.
        bus_type: list of str
            Types of buses.

    Returns:
        np.ndarray
            Jacobian matrix.
    """
    J = np.zeros((2 * num_buses, 2 * num_buses), dtype=float)
    for i in range(num_buses):
        for k in range(num_buses):
            if i == k:
                J[i, k] = np.sum(np.abs(Y_bus[i, :]) * np.abs(V) * np.sin(np.angle(Y_bus[i, :]) - np.angle(V[i]) + np.angle(V)))
                J[i + num_buses, k + num_buses] = -np.sum(np.abs(Y_bus[i, :]) * np.abs(V) * np.cos(np.angle(Y_bus[i, :]) - np.angle(V[i]) + np.angle(V)))
            else:
                J[i, k] = -np.abs(Y_bus[i, k]) * np.abs(V[i]) * np.abs(V[k]) * np.sin(np.angle(Y_bus[i, k]) - np.angle(V[i]) + np.angle(V[k]))
                J[i + num_buses, k + num_buses] = np.abs(Y_bus[i, k]) * np.abs(V[i]) * np.abs(V[k]) * np.cos(np.angle(Y_bus[i, k]) - np.angle(V[i]) + np.angle(V[k]))

    return J
