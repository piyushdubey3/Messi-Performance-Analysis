import numpy as np
import matplotlib.pyplot as plt

# International data
intl_matches = np.array([10,13,9,7,14,8,11,7,5,10,4,16,14,8,11])
intl_minutes = np.array([866,1200,810,491,1161,685,888,630,450,802,360,1364,1263,652,909])

# ----- CALCULATE SLOPE (b) & INTERCEPT (a) -----
x = intl_matches
y = intl_minutes

xbar = np.mean(x)
ybar = np.mean(y)

b_intl = np.sum((x - xbar)*(y - ybar)) / np.sum((x - xbar)**2)
a_intl = ybar - b_intl*xbar

print("International Slope (b):", b_intl)
print("International Intercept (a):", a_intl)

# Regression line
predicted_intl_minutes = a_intl + b_intl*x

plt.figure(figsize=(10,6))
plt.scatter(x, y, color='crimson', s=80, label="Actual Minutes Played")
plt.plot(x, predicted_intl_minutes, "r--",
         label=f"y = {a_intl:.2f} + {b_intl:.2f}x")

plt.title("Messi: Minutes Played vs Matches (International)")
plt.xlabel("Matches Played")
plt.ylabel("Minutes Played")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
