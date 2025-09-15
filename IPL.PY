# 📊 IPL Data Analysis Mini Project (using NumPy + Matplotlib only)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ✅ Load datasets (update the paths if needed)
matches = pd.read_csv(r"C:\Users\Prerana\OneDrive\Desktop\5 Day Python\Project\matches.csv")
deliveries = pd.read_csv(r"C:\Users\Prerana\OneDrive\Desktop\5 Day Python\Project\deliveries.csv")

# 1️⃣ Matches per season
matches_per_season = matches.groupby('season').id.count()
x = np.array(matches_per_season.index)
y = np.array(matches_per_season.values)

plt.figure(figsize=(10,6))
plt.bar(x, y, color="skyblue", edgecolor="black")
plt.title("Number of Matches per IPL Season", fontsize=16)
plt.xlabel("Season")
plt.ylabel("Matches")
plt.show()

# 2️⃣ Most successful teams
team_wins = matches['winner'].value_counts().head(10)
x = np.arange(len(team_wins))
y = team_wins.values
labels = team_wins.index

plt.figure(figsize=(10,6))
plt.barh(x, y, color="orange", edgecolor="black")
plt.yticks(x, labels)
plt.title("Most Successful IPL Teams", fontsize=16)
plt.xlabel("Wins")
plt.ylabel("Team")
plt.show()

# 3️⃣ Toss decision trends
toss_decision = matches['toss_decision'].value_counts()
sizes = toss_decision.values
labels = toss_decision.index

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=["lightcoral", "lightgreen"])
plt.title("Toss Decision Trends (Bat vs Field)", fontsize=16)
plt.show()

# 4️⃣ Top 10 Run Scorers
top_scorers = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
x = np.arange(len(top_scorers))
y = top_scorers.values
labels = top_scorers.index

plt.figure(figsize=(10,6))
plt.barh(x, y, color="steelblue", edgecolor="black")
plt.yticks(x, labels)
plt.title("Top 10 Run Scorers in IPL", fontsize=16)
plt.xlabel("Runs")
plt.ylabel("Batsman")
plt.show()

# 5️⃣ Top 10 Wicket Takers

