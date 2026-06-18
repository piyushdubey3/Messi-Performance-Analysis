import numpy as np
import matplotlib.pyplot as plt

# International data
intl_matches = np.array([10,13,9,7,14,8,11,7,5,10,4,16,14,8,11])
intl_assists = np.array([2,9,1,4,2,3,6,0,3,2,0,5,6,1,5])

# ----- CALCULATE SLOPE (b) & INTERCEPT (a) USING YOUR FORMULA -----
x = intl_matches
y = intl_assists

xbar = np.mean(x)
ybar = np.mean(y)

b_intl = np.sum((x - xbar)*(y - ybar)) / np.sum((x - xbar)**2)
a_intl = ybar - b_intl*xbar

print("International Slope (b):", b_intl)
print("International Intercept (a):", a_intl)

# Regression line
predicted_intl_assists = a_intl + b_intl*x

# Plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, color='orange', s=80, label="Actual Assists")
plt.plot(x, predicted_intl_assists, "r--",
         label=f"y = {a_intl:.2f} + {b_intl:.2f}x")

plt.title("Messi: Matches vs Assists (International)")
plt.xlabel("Matches Played")
plt.ylabel("Assists")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
