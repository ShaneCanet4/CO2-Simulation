# CO₂ Cartridge Compressible Flow Simulation

This notebook models the transient discharge of a fixed mass of CO₂ from a sealed cartridge through a circular orifice.
The simulation captures both choked and unchoked compressible flow regimes and continuously updates the thermodynamic
state as mass is depleted.

The objective is to provide a first-principles analytical tool for early-stage valve and orifice design prior to CFD
or experimental validation.

## Modeling Objectives

- Model transient compressible gas discharge
- Identify choked vs unchoked flow using critical pressure ratio
- Track pressure, temperature, and remaining mass over time
- Estimate mass flow rate as a function of evolving thermodynamic state
- Provide rapid, parametric insight for mechanical design decisions

## Key Assumptions

- CO₂ behaves as an ideal gas
- Isentropic expansion through the orifice
- Uniform pressure and temperature within the cartridge at each timestep
- One-dimensional flow through a sharp-edged orifice
- No heat transfer with surroundings (adiabatic discharge)
- Quasi-steady flow at each timestep
- Constant discharge coefficient
