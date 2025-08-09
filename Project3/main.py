from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Draw and save the categorical plot
cat_plot = draw_cat_plot()
cat_plot.savefig("catplot.png")

# Draw and save the heat map
heat_map = draw_heat_map()
heat_map.savefig("heatmap.png")
