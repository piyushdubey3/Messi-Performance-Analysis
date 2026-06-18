import numpy as np
import matplotlib.pyplot as plt

# ---- Club data ----
club_goals   = np.array([53,73,60,41,58,41,54,45,51,31,38,11,21,25,33])
club_minutes = np.array([4574,5221,4067,3743,5061,4229,4452,4471,4024,3812,4192,2871,3630,2321,3202])

# ----- SLOPE (b) & INTERCEPT (a) -----
x = club_goals
y = club_minutes

xbar = np.mean(x)
ybar = np.mean(y)

b = np.sum((x-xbar)*(y-ybar)) / np.sum((x-xbar)**2)
a = ybar - b*xbar

print("Club Slope (b):", b)
print("Club Intercept (a):", a)

# Regression line
pred = a + b*x

# Plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, color='blue', s=80, label="Minutes Played")
plt.plot(x, pred, "b--", label=f"y = {a:.2f} + {b:.2f}x")

plt.title("Messi: Goals vs Minutes Played (Club)")
plt.xlabel("Goals")
plt.ylabel("Minutes Played")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
