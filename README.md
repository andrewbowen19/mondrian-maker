# mondrian-maker
Python package that produces randomly-generated Mondrian-style plots.


## Output Samples
![*Composition with Red, Blue, and Yellow*, Piet Mondrian, 1930 ](img/mondrian_de_stijl_example.png?raw=true)

![`mondrian`-generated plot](img/mondrian_generated_example.png?raw=true)


## Installation
Dependencies for this project are listed in `requirements.txt`. This library is compatible with `python3 >= 3.7.6` and requires both `git` and `pip` to be installed locally. This repository can be installed via the following steps:

    git clone https://github.com/andrewbowen19/mondrian-maker.git

From the command-line:

    cd mondrian-maker

Then, you can install via `pip`.

    pip install .

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

