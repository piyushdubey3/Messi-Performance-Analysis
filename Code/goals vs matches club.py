import numpy as np
import matplotlib.pyplot as plt

# Club data
club_matches = np.array([55,60,50,46,57,49,52,54,50,44,47,34,41,29,39])
club_goals   = np.array([53,73,60,41,58,41,54,45,51,31,38,11,21,25,33])
# ---- CALCULATE SLOPE (b) AND INTERCEPT (a) USING YOUR FORMULA ----
x = club_matches
y = club_goals

xbar = np.mean(x)
ybar = np.mean(y)

b_club = np.sum((x - xbar) * (y - ybar)) / np.sum((x - xbar)**2)
a_club = ybar - b_club * xbar

print("Club Slope (b):", b_club)
print("Club Intercept (a):", a_club)

# Regression line values
predicted_club_goals = a_club + b_club * x

# Plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, color='blue', s=80, label="Actual Goals")
plt.plot(x, predicted_club_goals, "b--", label=f"y = {a_club:.2f} + {b_club:.2f}x")

plt.title("Messi: Goals vs Matches (Club)")
plt.xlabel("Matches Played")
plt.ylabel("Goals Scored")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()

