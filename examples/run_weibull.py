
import sys
import os
filePath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.split(filePath)[0])

from src.weibull.weibul import Weibull
from examples.dataset.load_data import DataLoader
