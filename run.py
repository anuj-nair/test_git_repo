import os
from datetime import datetime
import sys
print(f'File path: {os.path.abspath(__file__)}')
print(f'Time: {datetime.now()}')
print(f'PATH: {sys.path}')
