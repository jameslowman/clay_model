import geopandas as gpd
import pandas as pd
from shapely import box


mgrs = gpd.read_file("mgrs_full.fgb")
print(f"Loaded {len(mgrs)} MGRS grid cells.")
mgrs = mgrs.rename(columns={"Name": "name"})
print(mgrs)
# save the mgrs over the mgrs_full.fgb file
# mgrs.to_file("mgrs_full.fgb")

# aoi = gpd.GeoDataFrame(
#     pd.DataFrame(["Puri"], columns=["Region"]),
#     crs="EPSG:4326",
#     geometry=[box(85.0503, 19.4949, 86.1042, 20.5642)],
# )
# mgrs_aoi = mgrs.overlay(aoi)
#
# # Rename the name column to use lowercase letters for the datacube script to
# # pick upthe MGRS tile name.
# mgrs_aoi = mgrs_aoi.rename(columns={"Name": "name"})
#
# print(f"Found {len(mgrs_aoi)} matching MGRS tiles over the AOI.")
#
# mgrs_aoi.to_file("mgrs_aoi.fgb")
#
# # read the mgrs_aoi.fgb file into a geopandas dataframe
# reader = gpd.read_file("mgrs_aoi.fgb")
# # print the dataframe
# print(reader)
#
# # write only the name column to a fgb file
# reader["name"].to_file("mgrs_aoi_names.fgb")
