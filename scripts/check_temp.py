import rasterio
import matplotlib.pyplot as plt

# Select a file
file = 'temp_test_data_collect/claytile_59GLM_20181223_v02_0200.tif'

# Open the file:
with rasterio.open(file) as src:
    print(f"number of channels: {src.count}")
    # Show each channel as a different subplot, there are 13 channels
    fig, axes = plt.subplots(3, 5, figsize=(15, 10))
    for i, ax in enumerate(axes.flatten()):
        if i < src.count:
            data = src.read([i+1])
            print(f"data type: {data.dtype}")
            # Prep the uint16 geotiff data for display
            try:
                data = data[0,:,:] / (data.max() + 1e-12)
                ax.imshow(data)
                ax.set_title(f"channel {i+1}")
            except:
                print(f"failed to plot channel {i+1}")
        else:
            ax.axis("off")
    plt.show()
