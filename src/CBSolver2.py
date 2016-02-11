"""
CBMPy: CBSolver2 module
=======================
PySCeS Constraint Based Modelling (http://cbmpy.sourceforge.net)
Copyright (C) 2009-2015 Brett G. Olivier, VU University Amsterdam, Amsterdam, The Netherlands

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

Author: Brett G. Olivier
Contact email: bgoli@users.sourceforge.net
Last edit: $Author: bgoli $ ($Id: CBSolver.py 305 2015-04-23 15:18:31Z bgoli $)

"""

# preparing for Python 3 port
from __future__ import division, print_function
from __future__ import absolute_import
#from __future__ import unicode_literals

from .CBConfig import __CBCONFIG__ as __CBCONFIG__
__DEBUG__ = __CBCONFIG__['DEBUG']
__version__ = __CBCONFIG__['VERSION']
SOLVER_PREF = __CBCONFIG__['SOLVER_PREF']

__AVAILABLE_SOLVERS__ = []

__CBCONFIG__['SOLVER_ACTIVE'] = None