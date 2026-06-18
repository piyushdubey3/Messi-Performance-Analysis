import numpy as np
import matplotlib.pyplot as plt

# Club data
club_matches = np.array([55,60,50,46,57,49,52,54,50,44,47,34,41,29,39])
club_assists = np.array([23,30,15,14,27,23,16,18,19,25,12,14,20,16,9])

# ----- CALCULATE SLOPE (b) & INTERCEPT (a) USING YOUR FORMULA -----
x = club_matches
y = club_assists

xbar = np.mean(x)
ybar = np.mean(y)

b_club = np.sum((x - xbar)*(y - ybar)) / np.sum((x - xbar)**2)
a_club = ybar - b_club*xbar

print("Club Slope (b):", b_club)
print("Club Intercept (a):", a_club)

# Regression line
predicted_club_assists = a_club + b_club*x

# Plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, color='purple', s=80, label="Actual Assists")
plt.plot(x, predicted_club_assists, "m--",
         label=f"y = {a_club:.2f} + {b_club:.2f}x")

plt.title("Messi: Matches vs Assists (Club)")
plt.xlabel("Matches Played")
plt.ylabel("Assists")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
