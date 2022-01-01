# mondrian-maker/tests/test/mondrian_maker.py

import sys

from matplotlib.pyplot import savefig

# sys.path.append('/Users/andrewbowen/sideProjects/mondrian-maker/')

from mondrian_maker.mondrianMaker import mondrian
import numpy as np

# Call the class
m = mondrian()


def test_mondrian():
    m.make_mondrian()

def test_mondrian_title():
    m.make_mondrian(title='test title')

def test_mondrian_title_bool():
    m.make_mondrian(title=True)

def test_mondrian_xarray():
    x = np.random.random(m.array_size)
    m.make_mondrian(x=x)

def test_mondrian_yarray():
    y = np.random.random(m.array_size)
    m.make_mondrian(y=y)

def test_mondrian_savefig():
    m.make_mondrian(savefig=True)

def test_mondrian_gridlines():
    m.make_mondrian(gridlines=False)

    


if __name__ == "__main__":
    print('testing mondrian')