import numpy as np

import pandas as pd



# Parameters

initial_eth_price = 1500  # Initial price of ETH in USD

yield_rate = 0.10  # 10%

discount_rate = 0.15  # 15%

time_horizon = 5  # 5 years

eth_price_growth = 0.20  # 20%



# Initialize arrays to store calculated values

years = np.arange(1, time_horizon + 1)

eth_price_at_t = np.zeros(time_horizon)

cash_flow_at_t = np.zeros(time_horizon)

discounted_cash_flow_at_t = np.zeros(time_horizon)



# Perform calculations

for t in years:

    eth_price_at_t[t - 1] = initial_eth_price * (1 + eth_price_growth) ** t

    cash_flow_at_t[t - 1] = eth_price_at_t[t - 1] * yield_rate

    discounted_cash_flow_at_t[t - 1] = cash_flow_at_t[t - 1] / ((1 + discount_rate) ** t)



# Calculate the total present value

total_present_value = np.sum(discounted_cash_flow_at_t)



# Create a DataFrame to display the results

df = pd.DataFrame({

    'Year': years,

    'ETH Price at t': eth_price_at_t,

    'Cash Flow at t': cash_flow_at_t,

    'Discounted Cash Flow at t': discounted_cash_flow_at_t

})



df, total_present_value
