# mondrian-maker
Python package that produces randomly-generated Mondrian-style plots.

This python library allows the user to create [Mondrian-style]() plots via numpy and matplotlib. [Piet Mondrian](https://en.wikipedia.org/wiki/Piet_Mondrian) was one of the most influential artists of the 20th century. The package `mondrian-maker` seeks to recreate his style via randomly-generated (or user-defined) sets of numbers.

## Output Samples
***Composition with Red, Blue, and Yellow*, Piet Mondrian, 1930**
![](img/mondrian_de_stijl_example.png?raw=true)

**`mondrian.py`-generated plot**
![](img/mondrian_generated_example.png?raw=true)


## Installation
Dependencies for this project are listed in `requirements.txt`. This library is compatible with `python3 >= 3.7.6` and requires both `git` and `pip` to be installed locally. This repository can be installed via the following steps:

    git clone https://github.com/andrewbowen19/mondrian-maker.git

From the command-line:

    cd mondrian-maker

Then, you can install via `pip`.

    pip install .

We are also planning on publishing this package to [PyPi](https://pypi.org) to allow pip install without neeeding to clone this repo.

## Usage
If pip installed locally, the mondrian class can be imported into a python script as shown below:
```
from mondrian_maker.mondrian import mondrian

m = mondrian()
m.make_mondrian(<args>)
```

The `mondrian` class in the `mondrian_maker.mondrian` module contained the method `make_mondrian` which actually creates the plot. In addition, the `mondrian.py` module can be run directly with python command-line args

    python mondrian.py --n_plots <int> --savefig <boolean> --array_size <int> --title <str>

    
## TODO

* [ ] Add more command-line arguments to parser for direct run by user
* [ ] Make sphinx docs ([readthedocs](https://readthedocs.org))
* [ ] [Publish to PyPi](https://realpython.com/pypi-publish-python-package/)

