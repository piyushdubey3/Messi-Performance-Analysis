import numpy as np
import matplotlib.pyplot as plt

# ---- Club data ----
club_matches = np.array([55,60,50,46,57,49,52,54,50,44,47,34,41,29,39])
club_success = np.array([1670,1865,1540,1430,1934,1505,1320,1529,1487,1629,1918,1393,1613,1250,1300])

# ----- SLOPE (b) & INTERCEPT (a) -----
x = club_matches
y = club_success

xbar = np.mean(x)
ybar = np.mean(y)

b = np.sum((x - xbar)*(y - ybar)) / np.sum((x - xbar)**2)
a = ybar - b*xbar

print("Club Slope (b):", b)
print("Club Intercept (a):", a)

# Regression line
pred = a + b*x

# Plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, color='seagreen', s=80, label="Successful Passes")
plt.plot(x, pred, "g--", label=f"y = {a:.2f} + {b:.2f}x")

plt.title("Messi: Successful Passes vs Matches (Club)")
plt.xlabel("Matches Played")
plt.ylabel("Successful Passes")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
