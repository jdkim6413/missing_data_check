import missingno as msno
import pandas as pd
import matplotlib.pyplot as plt


csv_file_name = "test.csv"

# skiprows=range(1, 305281)
plot_df = pd.read_csv(csv_file_name)

coll = pd.read_csv("https://raw.githubusercontent.com/ResidentMario/missingno-data/master/nyc_collision_factors.csv")
coll_sample = coll.sample(250)

test = plot_df.iloc[:, 0:30]

msno.matrix(test)
plt.show()

# msno.bar(self.weather, figsize=[12, 7], fontsize=8)
# plt.show()