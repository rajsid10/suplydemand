import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to identify supply and demand zones based on momentum candles
def identify_zones(prices, momentum_threshold, consolidation_threshold, wick_threshold):
    zones = []
    i = 0
    while i < len(prices) - 2:
        # Check for three momentum candles in a row
        if prices[i] < prices[i+1] < prices[i+2]:
            # Identify the demand zone (area between the high and low of the previous candle)
            demand_zone = (min(prices[i-1], prices[i]), max(prices[i-1], prices[i]))
            zones.append(('Demand', demand_zone))
            i += 3
        # Check for three momentum candles in a row
        elif prices[i] > prices[i+1] > prices[i+2]:
            # Identify the supply zone (area between the high and low of the previous candle)
            supply_zone = (min(prices[i-1], prices[i]), max(prices[i-1], prices[i]))
            zones.append(('Supply', supply_zone))
            i += 3
        else:
            i += 1
    
    # Identify consolidation periods
    i = 0
    while i < len(prices) - 1:
        consolidation_start = i
        while i < len(prices) - 1 and abs(prices[i] - prices[i+1]) <= consolidation_threshold:
            i += 1
        if i > consolidation_start:
            # Identify the consolidation zone (area between the high and low of the consolidation period)
            consolidation_zone = (min(prices[consolidation_start:i+1]), max(prices[consolidation_start:i+1]))
            zones.append(('Consolidation', consolidation_zone))
        i += 1
    
    # Identify areas with wicks
    i = 0
    while i < len(prices) - 1:
        wick_start = i
        while i < len(prices) - 1 and abs(prices[i] - prices[i+1]) <= wick_threshold:
            i += 1
        if i > wick_start:
            # Identify the wick zone (area between the high and low of the wick period)
            wick_zone = (min(prices[wick_start:i+1]), max(prices[wick_start:i+1]))
            zones.append(('Wick', wick_zone))
        i += 1
    
    return zones

# Generate random price data for demonstration
np.random.seed(1)
prices = np.random.randint(50, 150, 100)

# Define parameters
momentum_threshold = 0.8
consolidation_threshold = 5
wick_threshold = 3

# Identify supply and demand zones
zones = identify_zones(prices, momentum_threshold, consolidation_threshold, wick_threshold)

# Plot the price data and identified zones
plt.figure(figsize=(10, 6))
plt.plot(prices, label='Price', color='black')
for zone_type, zone in zones:
    zone_start, zone_end = zone
    plt.axvspan(zone_start, zone_end, alpha=0.3, label=zone_type)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Supply and Demand Zones')
plt.grid()
plt.show()
