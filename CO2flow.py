import math as mt
import matplotlib.pyplot as plt

# Constants and Initial States
V1 = 35 * (10**-6)           # m^3 (volume of CO2 cartridge)
p1 = 5.861 * (10**6)         # Pa (initial pressure inside cartridge)
A = mt.pi * (.000254)**2  # m^2 (new ordfice area)
C = 0.89                     # Discharge coefficient
m1 = 20                      # grams of CO₂
patm = 101325                # Pa (atmospheric pressure)
gamma = 1.3                  # Adiabatic index for CO₂
M = 44.01                    # g/mol (molar mass of CO₂)
R = 8.314                    # J/mol·K
Rs = R / M                   # ≈ 0.1889 J/g·K (specific gas constant for CO₂)
T1 = 273                     # K (initial temperature)

# Pressure from ideal gas law
def p0(T, V, m):
    return m * Rs * T / V

# Temperature from ideal gas law
def T0(p, V, m):
    return p * V / (m * Rs)

# Choked flow equation 
def mcdot(a, p, gamma, T):
    term = (2 / (gamma + 1)) ** ((gamma + 1) / (2 * (gamma - 1)))
    return a * p * mt.sqrt(gamma / (Rs * T)) * term  # g/s

# Unchoked flow equation 
def mudot(c, a, p, pe, gamma, T):
    ratio = pe / p
    term1 = (2 * gamma) / (Rs * (gamma - 1) * T)
    term2 = (ratio ** (2 / gamma)) - (ratio ** ((gamma + 1) / gamma))

    if term2 <= 0:
        return 0  # flow not physically meaningful

    return c * a * p * mt.sqrt(term1 * term2)  # g/s

# Flow simulation using mass (grams) for two minutes currently
def flow(m, V, p, A, C, gamma, pe, T):
    tL = []
    t=0
    p1 = p
    T1 = T
    flowrate = []
    mtire=0 
    Ttire= 273 #new tire variables

    while t<120:
        t+=1
        tL.append(t)
        print(t)
        critical_ratio = (2 / (gamma + 1)) ** (gamma / (gamma - 1))
        if (pe / p1) <= critical_ratio:
            mdot = mcdot(A, p1, gamma, T1)
        else:
            mdot = mudot(C, A, p1, pe, gamma, T1)

        # Limit flow to available mass
        if mdot > m:
            mdot = m

        flowrate.append(mdot)
        m -= mdot
        mtire+= mdot
        
        p1 = p0(T1, V, m)
        T1 = T0(p1, V, m)
        pe= (1/.0035)*(mtire/M)*R*Ttire
        Ttire= (pe*.0035)/((mtire/M)*R)
       
    flowavg = sum(flowrate) / len(flowrate)
    
    #Data visualization
    plt.plot(tL,flowrate,label="flowrate over time")
    plt.xlabel("time in seconds")
    plt.ylabel("mass flow rate in kg/s")
    plt.show()

    return f"Average flow rate: {flowavg:.4f} g/s\nFlow values over time:\n{flowrate}"
    

# Run the simulation
print(flow(m1, V1, p1, A, C, gamma, patm, T1))

