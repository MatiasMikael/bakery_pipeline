import kaggle

# Download dataset
kaggle.api.dataset_download_files("akashdeepkuila/bakery", path="data/", unzip=True)

print("Dataset downloaded and unzipped to the 'data/' directory")