import numpy as np
import sys

if len(sys.argv) < 2:
    print("Usage: python view_npy.py <file.npy>")
    sys.exit(1)

file_path = sys.argv[1]
try:
    data = np.load(file_path)
    print(f"Shape: {data.shape}")
    print(f"Data type: {data.dtype}")
    print("Data:")
    print(data)
except Exception as e:
    print(f"Error loading file: {e}")