# PyCalc

A python interpreter with a bunch of mathy and other stuff imported.  
Helps me save 0.0035 seconds when I want to know if 6 is prime.

Probably *not* on the [XKCD automation chart](https://xkcd.com/1205/), especially after making this repo.



## Usage

I have added the following function to my `.bashrc` file.

Then I can run `pycalc` to spin up the REPL.

```bash
pycalc() {
  # Create new python REPL which imports pycalc
  PYCALC_PATH=$HOME/.config/pycalc/

  # We use fancy import function so that `sys` is not necessarily imported
  python -i -c "__import__('sys').path.append('$PYCALC_PATH');from pycalc import *"
 }
```
