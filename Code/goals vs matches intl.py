import numpy as np
import matplotlib.pyplot as plt

# International data
intl_matches = np.array([10,13,9,7,14,8,11,7,5,10,4,16,14,8,11])
intl_goals   = np.array([2,4,12,6,8,4,8,4,4,5,1,9,17,8,6])

# ---- CALCULATE SLOPE (b) AND INTERCEPT (a) USING YOUR FORMULA ----
x = intl_matches
y = intl_goals

xbar = np.mean(x)
ybar = np.mean(y)

b_intl = np.sum((x - xbar) * (y - ybar)) / np.sum((x - xbar)**2)
a_intl = ybar - b_intl * xbar

print("International Slope (b):", b_intl)
print("International Intercept (a):", a_intl)

# Regression line values
predicted_intl_goals = a_intl + b_intl * x

# Plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, color='red', s=80, label="Actual Goals")
plt.plot(x, predicted_intl_goals, "r--", label=f"y = {a_intl:.2f} + {b_intl:.2f}x")

plt.title("Messi: Goals vs Matches (International)")
plt.xlabel("Matches Played")
plt.ylabel("Goals Scored")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
