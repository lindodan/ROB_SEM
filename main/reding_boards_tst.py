from ctu_crs import CRS93
import pandas as pd
import numpy as np


# Read csv
file_path = "/Users/danli/ROB_SEM/ctu_crs/plate_configs/positions_plate_01-02.csv"

data = pd.read_csv(file_path, header=None) # header none so i read the first row

# aruco ids
aruco_ids = data.iloc[0].values
# coords
coordinates = data.iloc[1:].values

print("ArUco IDs:", aruco_ids)
print("Coordinates:", coordinates)

output_data = pd.DataFrame(coordinates, columns=['X (mm)', 'Y (mm)'])
output_data.index.name = 'ID Otvoru'
print(output_data)
