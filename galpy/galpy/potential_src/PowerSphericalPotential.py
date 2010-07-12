###############################################################################
#   PowerSphericalPotential.py: General class for potentials derived from 
#                               densities with two power-laws
#
#                                     amp
#                          rho(r)= ---------
#                                   r^\alpha
###############################################################################
import math as m
from scipy import special, integrate
from Potential import Potential
class PowerSphericalPotential(Potential):
    """Class that implements spherical potentials that are derived from 
    power-law density models

                A
    rho(r)= ---------
             r^\alpha
    """
    def __init__(self,amp=1.,alpha=1.,normalize=False):
        """
        NAME:
           __init__
        PURPOSE:
           initialize a power-law-density potential
        INPUT:
           amp - amplitude to be applied to the potential (default: 1)
           alpha - inner power
           normalize - if True, normalize such that vc(1.,0.)=1.
        OUTPUT:
           (none)
        HISTORY:
           2010-07-10 - Written - Bovy (NYU)
        """
        Potential.__init__(self,amp=amp)
        self.alpha= alpha

    def _evaluate(self,R,z):
        """
        NAME:
           _evaluate
        PURPOSE:
           evaluate the potential at R,z
        INPUT:
           R - Galactocentric cylindrical radius
           z - vertical height
        OUTPUT:
           Phi(R,z)
        HISTORY:
           2010-07-10 - Started - Bovy (NYU)
        """
        if self.alpha == 2.:
            return m.log(R**2.+z**2.)/2. 
        else:
            return (R**2.+z**2.)**(1.-self.alpha/2.)

    def _Rforce(self,R,z):
        """
        NAME:
           _Rforce
        PURPOSE:
           evaluate the radial force for this potential
        INPUT:
           R - Galactocentric cylindrical radius
           z - vertical height
        OUTPUT:
           the radial force
        HISTORY:
           2010-07-10 - Written - Bovy (NYU)
        """
        return -R/(R**2.+z**2.)**(self.alpha/2.)

    def _zforce(self,R,z):
        """
        NAME:
           _zforce
        PURPOSE:
           evaluate the vertical force for this potential
        INPUT:
           R - Galactocentric cylindrical radius
           z - vertical height
        OUTPUT:
           the vertical force
        HISTORY:
           2010-07-10 - Written - Bovy (NYU)
        """
        return -z/(R**2.+z**2.)**(self.alpha/2.)