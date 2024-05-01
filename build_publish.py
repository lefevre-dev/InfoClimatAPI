from shutil import rmtree
import os

# script de publication
here = os.path.abspath(os.path.dirname(__file__))
rmtree(os.path.join(here, "dist"))
os.system("py -m build")

os.system("py -m twine upload dist/*")