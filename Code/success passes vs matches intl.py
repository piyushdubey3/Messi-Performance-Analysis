import numpy as np
import matplotlib.pyplot as plt

# ---- International data ----
intl_matches = np.array([10,13,9,7,14,8,11,7,5,10,4,16,14,8,11])
intl_success = np.array([290,310,335,350,365,375,315,330,260,310,355,300,325,270,290])

# ----- SLOPE (b) & INTERCEPT (a) -----
x = intl_matches
y = intl_success

xbar = np.mean(x)
ybar = np.mean(y)

b = np.sum((x - xbar)*(y - ybar)) / np.sum((x - xbar)**2)
a = ybar - b*xbar

print("International Slope (b):", b)
print("International Intercept (a):", a)

# Regression line
pred = a + b*x

# Plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, color='darkred', s=80, label="Successful Passes")
plt.plot(x, pred, "r--", label=f"y = {a:.2f} + {b:.2f}x")

plt.title("Messi: Successful Passes vs Matches (International)")
plt.xlabel("Matches Played")
plt.ylabel("Successful Passes")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
