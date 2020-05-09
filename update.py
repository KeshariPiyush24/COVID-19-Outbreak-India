import os
from scripts import replicate
import shutil
import runipy

replicate.writedata()
os.system('runipy -o analysis.ipynb')
os.system('jupyter nbconvert --output index.html --to html analysis.ipynb')
shutil.rmtree('scripts/__pycache__')
