import matplotlib.pyplot as plt

#B. Flyvbjerg, "What You Should Know About Megaprojects and Why: An Overview", Project Management Journal, vol. 45 iss 2

project_overrun_percents = [1900, 1600, 1400, 1300, 1100, 900, 650, 590, 560, 560, 440, 300, 280, 220, 200, 200, 190, 180, 160, 160, 150, 130, 120, 110, 100, 100, 80, 80, 80, 70, 60, 60, 50]

plt.loglog(range(len(project_overrun_percents)), project_overrun_percents)
plt.savefig("project_delays.png")
