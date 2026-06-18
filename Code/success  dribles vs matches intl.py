import numpy as np
import matplotlib.pyplot as plt

# ---- International data ----
intl_matches = np.array([10,13,9,7,14,8,11,7,5,10,4,16,14,8,11])
intl_dribbles = np.array([28,36,40,22,42,25,30,20,15,28,9,45,48,26,33])

# ----- SLOPE (b) & INTERCEPT (a) -----
x = intl_matches
y = intl_dribbles

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
plt.scatter(x, y, color='darkgreen', s=80, label="Successful Dribbles")
plt.plot(x, pred, "r--", label=f"y = {a:.2f} + {b:.2f}x")

plt.title("Messi: Successful Dribbles vs Matches (International)")
plt.xlabel("Matches Played")
plt.ylabel("Successful Dribbles")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
