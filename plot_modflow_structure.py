import os
import numpy as np
import matplotlib.pyplot as plt

def plot_modflow_structure(x_number, y_number, csv_dir, point_size=50):
    """
    x_number: the number of grids along the x-axis
    y_number: the number of grids along the y-axis
    csv_dir: the path to the directory containing .csv files
    point_size: the size of boundary points in the scatter plot
    """

    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 12

    csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]

    markers = ['o', 's', 'p', '^', 'H', 'd', '*', '8', 'P']

    # Create the grid
    # x = np.arange(0, x_number+1, 1) # +1 because there is one more gridline than grid
    # y = np.arange(0, y_number+1, 1)
    grid_number = max(x_number, y_number)
    grid = np.arange(0, grid_number+1, 1)
    X, Y = np.meshgrid(grid, grid)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)

    # Plot the grid
    ax.plot(X, Y, linestyle=':', color='black', linewidth=0.8)
    ax.plot(Y, X, linestyle=':', color='black', linewidth=0.8)
    # only display one legend for all gridlines
    ax.plot([], linestyle=':', color='black', linewidth=0.8, label="Gridlines")

    # Loop through the list of csv files
    for i, file_name in enumerate(csv_files):
        # Load the data from the .csv file
        data = np.loadtxt(os.path.join(csv_dir, file_name), delimiter=',', encoding='utf-8-sig')
        # Extract the x and y coordinates
        x_coords = data[:, 2].astype(int) - 0.5
        y_coords = data[:, 1].astype(int) - 0.5
        # Plot the scatter plot
        marker = markers[i % len(markers)]
        ax.scatter(x_coords, y_coords, edgecolor="black", s=point_size,
                   marker=marker, label=os.path.splitext(file_name)[0])

    ax.set_xlim(0, x_number)
    ax.set_ylim(0, y_number)
    ax.invert_yaxis()
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.tick_params(bottom=True, top=True, left=True, right=True,
                   labelbottom=True, labeltop=True, labelleft=True, labelright=True)