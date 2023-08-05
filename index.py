import pickle
import time
import pandas as pd
import geopandas as gpd
from libpysal.weights import Kernel
from shapely.geometry import Point

#Import dataframe

print ("Importing dataframe")
df = pd.read_csv("LdnListings_Proc.csv")

#Set coordinates

print ("Setting coordinates")
xys = df[['longitude', 'latitude']]\
        .apply(lambda row: Point(*row), axis=1)
gdb = gpd.GeoDataFrame(df.assign(geometry=xys),
                       crs="epsg:4326")

#Run kernel weight matrix

start = time.time()
print ("Running kernel weight matrix")

w_kernel = Kernel.from_dataframe(gdb)

# Save the Kernel object
with open('kernel.pkl', 'wb') as f:
    pickle.dump(w_kernel, f)

end = time.time()
print(f'Time taken: {end - start} seconds')
