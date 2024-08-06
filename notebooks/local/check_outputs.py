import os
from glob import glob
import json

nb_files = [y for x in os.walk(".") for y in glob(os.path.join(x[0], "*.ipynb"))]
for nb_file in nb_files:
    nb = json.load(open(nb_file))
    for cell in nb["cells"]:
        if len(cell["outputs"]) > 0:
            raise Exception(
                "One or more cell outputs are not empty. Please clear them using `poetry run invoke verify`."
            )
print("All cell outputs are empty!")
