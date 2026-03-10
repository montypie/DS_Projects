import kaggle
import os

# Create data directory if it doesn't exist
data_dir = "data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Download the flight prices dataset
kaggle.api.dataset_download_files(
    'dilwong/flightprices',
    path=data_dir, 
    unzip=True
)

print(f"Dataset downloaded successfully to {data_dir} directory")
