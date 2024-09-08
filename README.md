# CBMPy
PySCeS Constraint Based Modelling (https://systemsbioinformatics.github.io/cbmpy/)
Copyright (C) 2010-2024 Brett G. Olivier, Vrije Universiteit Amsterdam, Amsterdam, The Netherlands

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

Author: Brett G. Olivier (@bgoli)

## Fork by Maxime Mahout

This fork proposes an implementation of the encoding of gene protein reaction associations into the SBML FBC V2 format. Indeed, until now there was no way of adding gene products to the model and having them appear in the SBML FBC V2.

The code uses Python library `pyeda` for formatting the logical relations into the standardized DNF form (Disjunctive Normal Form, resulting in a list of isofunctional enzymatic complexes for each reaction).

Other works of interest that might be done in this fork: - implementing the global variable `METAPREFIX = 'meta_'` into a parameter of the conversion functions to SBML. The automatically added `'meta_'` prefix is incompatible with some versions of cobrapy, and was removed for the analysis of <https://github.com/maxm4/paSAmcs>. Code needs more testing before pull request.

## About
CBMPy (https://systemsbioinformatics.github.io/cbmpy/) is a new platform for constraint
based modelling and analysis. It has been designed using principles developed
in the PySCeS simulation software project: usability, flexibility and accessibility.
Its architecture is both extensible and flexible using data structures that are intuitive
to  the biologist (metabolites, reactions, compartments) while transparently translating
these into the underlying mathematical structures used in advanced analysis (LP's, MILP's).

CBMPy fully supports all the SBML Flux Balance Constraints (FBC) interoperability standards.

CBMPy implements popular analyses such as FBA, FVA, element/charge
balancing, network analysis and model editing as well as advanced methods
developed specifically for the ecosystem modelling: minimal distance methods,
flux minimization and input selection. To cater for a diverse range of modelling
needs CBMPy supports user interaction via:

- interactive console, scripting for advanced use or as a library for software development
- GUI, for quick access to a visual representation of the model, analysis methods and annotation tools
- SOAP based web services: using the Mariner framework much high level functionality is exposed for integration into web tools

For more information on the development and use of CBMPy (https://systemsbioinformatics.github.io/cbmpy/)

CBMPy has been tested on Windows 7 and 8.1, 10, 11, Mac OSX and Ubuntu Linux 12.04, 14.04, 16.04, 20.04, 22.04
CBMPy is currently developed on Python 3.10 and Python 3.8 or newer is highly recommended

## Install
The best way to get the basic CBMPy running is to install from **PyPI** or create an Anaconda environment. CBMPy is developed on GitHub (https://systemsbioinformatics.github.io/cbmpy/)

### Install with pip using requirements.txt
From a terrminal or command prompt try to install the required packages

`pip install -r requirements.txt`

### Then install CBMPy
`pip install cbmpy`

### Install by creating an Anaconda environment using environment.yml
From a terminal or command prompt try:

`conda env create -f=environment.yml`

This creates an environment **cbmpy3** that can be accessed from the command line using `conda activate cbmpy3`

### Check the basic installation
To check you installation follow the installation try the following in a Python shell:

```
import cbmpy
cmod = cbmpy.readSBML3FBC('cbmpy_test_core')
cbmpy.doFBA(cmod)
```
## Updating CBMPy
Once you have installed CBMPy it can be easily upgraded.

### Pip update
`pip install --upgrade cbmpy`

### Anaconda update
`conda update cbmpy`

(c) Brett G. Olivier, Amsterdam, 2014-2024
