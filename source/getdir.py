import os
from pathlib import Path

directory_base = str(os.getcwdb())[2:-1]

if os.name == 'nt':
    directory_data = Path(directory_base + '/data')
    directory_source = Path(directory_base + '/source')
    print(f"Data directory  : {directory_data}")
    print(f"Source directory: {directory_source}")
else:
    directory_data = directory_base + '/data'
    directory_source = directory_base + '/source'
    print(f"Data directory  : {directory_data}")
    print(f"Source directory: {directory_source}")