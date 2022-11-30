import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import itertools

sns.set_theme(style="whitegrid", font_scale=1.2)

df = pd.read_csv("GTFS.csv")

# Draw a nested barplot by species and sex
# g = sns.catplot(
ax = sns.barplot(
    data=df,
    #kind="bar",
    x="Data Scaling Factor", y="Time Elapsed (seconds)", hue="Tool",
    # errorbar="sd",  alpha=.6, height=6,
    # palette="dark",
    # palette="mako",
    palette="mako",
    # pallette="Spectral"
)

ax.set_yscale("log")

hatches = ["-", "\\\\", "||"]
# Loop over the bars
for bars, hatch in zip(ax.containers, hatches):
    # Set a different hatch for each group of bars
    for bar in bars:
        bar.set_hatch(hatch)
        bar.set_edgecolor([1, 1, 1])

ax.legend(loc='upper left', fancybox=True)


# hatches = itertools.cycle(['/', '.', '-', 'x', '\\', '*', 'o', 'O', '.'])
# for i, bar in enumerate(g.patches):
#     if i % 3 == 0:
#         hatch = next(hatches)
#     bar.set_hatch(hatch)

# g.despine(left=True)
# g.set_axis_labels("", "Body mass (g)")
# g.legend.set_title("")

ax.figure.savefig("GTFS.svg")
ax.figure.savefig("GTFS.eps")
plt.show()