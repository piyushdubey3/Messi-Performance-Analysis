import numpy as np
import matplotlib.pyplot as plt

# Club data
club_matches = np.array([55,60,50,46,57,49,52,54,50,44,47,34,41,29,39])
club_minutes = np.array([4574,5221,4067,3743,5061,4229,4452,4471,4024,3812,4192,2871,3630,2321,3202])

# ----- CALCULATE SLOPE (b) & INTERCEPT (a) -----
x = club_matches
y = club_minutes

xbar = np.mean(x)
ybar = np.mean(y)

b_club = np.sum((x - xbar)*(y - ybar)) / np.sum((x - xbar)**2)
a_club = ybar - b_club*xbar

print("Club Slope (b):", b_club)
print("Club Intercept (a):", a_club)

# Regression line
predicted_club_minutes = a_club + b_club*x

# Plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, color='navy', s=80, label="Actual Minutes Played")
plt.plot(x, predicted_club_minutes, "b--",
         label=f"y = {a_club:.2f} + {b_club:.2f}x")

plt.title("Messi: Minutes Played vs Matches (Club)")
plt.xlabel("Matches Played")
plt.ylabel("Minutes Played")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
