import pandas as pd
import matplotlib.pyplot as plt
import os


class PlotDrawer:

    def draw_plots(self, json_file):
        df = pd.read_json(json_file)

        if not os.path.exists("plots"):
            os.makedirs("plots")

        plots = []
        for column in df.columns:
            if column not in ["gt_corners", "rb_corners"]:
                plt.figure()
                plt.plot(df["gt_corners"], df[column], "o")
                plt.xlabel("Ground Truth Corners")
                plt.ylabel(column)
                plt.title(f"{column} vs Ground Truth Corners")
                plot_path = f"plots/{column}_plot.png"
                plt.savefig(plot_path)
                plots.append(plot_path)

        return plots
