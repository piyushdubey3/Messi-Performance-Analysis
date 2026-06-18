import numpy as np
import matplotlib.pyplot as plt

# ---- International data ----
intl_goals   = np.array([2,4,12,6,8,4,8,4,4,5,1,9,17,8,6])
intl_minutes = np.array([866,1200,810,491,1161,685,888,630,450,802,360,1364,1263,652,909])

# ----- SLOPE (b) & INTERCEPT (a) -----
x = intl_goals
y = intl_minutes

xbar = np.mean(x)
ybar = np.mean(y)

b = np.sum((x-xbar)*(y-ybar)) / np.sum((x-xbar)**2)
a = ybar - b*xbar

print("International Slope (b):", b)
print("International Intercept (a):", a)

# Regression line
pred = a + b*x

# Plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, color='crimson', s=80, label="Minutes Played")
plt.plot(x, pred, "r--", label=f"y = {a:.2f} + {b:.2f}x")

plt.title("Messi: Goals vs Minutes Played (International)")
plt.xlabel("Goals")
plt.ylabel("Minutes Played")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
