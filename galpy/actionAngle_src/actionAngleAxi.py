###############################################################################
#   actionAngle: a Python module to calculate  actions, angles, and frequencies
#
#      class: actionAngleAxi
#
#      methods:
#              JR
#              Jphi
#              angleR
#              TR
#              Tphi
#              I
#              calcRapRperi
#              calcEL
###############################################################################
import math as m
import numpy as nu
from scipy import optimize, integrate
from actionAngle import *
from galpy.potential_src.planarPotential import evaluateplanarRforces,\
    planarPotential, evaluateplanarPotentials
class actionAngleAxi(actionAngle):
    """Action-angle formalism for axisymmetric potentials"""
    def __init__(self,*args,**kwargs):
        """
        NAME:
           __init__
        PURPOSE:
           initialize an actionAngleAxi object
        INPUT:
           Either:
              a) R,vR,vT
              b) Orbit instance: initial condition used if that's it, orbit(t)
                 if there is a time given as well
              pot= potential or list of potentials (planarPotentials)
        OUTPUT:
        HISTORY:
           2010-12-01 - Written - Bovy (NYU)
        """
        actionAngle.__init__(self,*args,**kwargs)
        if not kwargs.has_key('pot'):
            raise IOError("Must specify pot= for actionAngleAxi")
        self._pot= kwargs['pot']
        return None
    
    def angleR(self,**kwargs):
        """
        NAME:
           AngleR
        PURPOSE:
           Calculate the radial angle
        INPUT:
           scipy.integrate.quadrature keywords
        OUTPUT:
           w_R(R,vT,vT) in radians + 
           estimate of the error (does not include TR error)
        HISTORY:
           2010-12-01 - Written - Bovy (NYU)
        """
        if hasattr(self,'_angleR'):
            return self._angleR
        (rperi,rap)= self.calcRapRperi()
        if rap == rperi:
            return 0.
        TR= self.TR(**kwargs)[0]
        EL= calcELAxi(self._R,self._vR,self._vT,self._pot)
        E, L= EL
        Rmean= m.exp((m.log(rperi)+m.log(rap))/2.)
        if self._R < Rmean:
            if self._R > rperi:
                wR= (2.*m.pi/TR*
                     nu.array(integrate.quadrature(_TRAxiIntegrandSmall,
                                                   0.,m.sqrt(self._R-rperi),
                                                   args=(E,L,self._pot)
                                                   **kwargs)))\
                                                   +nu.array([m.pi,0.])
            else:
                wR= nu.array([m.pi,0.])
        else:
            if self._R < rap:
                wR= -(2.*m.pi/TR*
                      nu.array(integrate.quadrature(_TRAxiIntegrandLarge,
                                                    0.,m.sqrt(rap--self._R),
                                                    args=(E,L,self._pot)
                                                    **kwargs)))
            else:
                wR= nu.array([0.,0.])
        if self._vR < 0.:
            wR[0]+= m.pi
        self._angleR= nu.array([wR[0] % (2.*m.pi),wR[1]])
        return self._angleR

    def TR(self,**kwargs):
        """
        NAME:
           TR
        PURPOSE:
           Calculate the radial period for a power-law rotation curve
        INPUT:
           scipy.integrate.quadrature keywords
        OUTPUT:
           T_R(R,vT,vT)*vc/ro + estimate of the error
        HISTORY:
           2010-12-01 - Written - Bovy (NYU)
        """
        if hasattr(self,'_TR'):
            return self._TR
        (rperi,rap)= self.calcRapRperi()
        if rap == rperi: #Rough limit
            raise AttributeError("Not implemented yet")
            #TR=kappa
            gamma= m.sqrt(2./(1.+self._beta))
            kappa= 2.*self._R**(self._beta-1.)/gamma
            self._TR= nu.array([2.*m.pi/kappa,0.])
            return self._TR
        Rmean= m.exp((m.log(rperi)+m.log(rap))/2.)
        EL= calcELAxi(self._R,self._vR,self._vT,self._pot)
        E, L= EL
        TR= 0.
        if Rmean > rperi:
            TR+= nu.array(integrate.quadrature(_TRAxiIntegrandSmall,
                                               0.,m.sqrt(Rmean-rperi),
                                               args=(E,L,self._pot,rperi),
                                               **kwargs))
        if Rmean < rap:
            TR+= nu.array(integrate.quadrature(_TRAxiIntegrandLarge,
                                               0.,m.sqrt(rap-Rmean),
                                               args=(E,L,self._pot,rap),
                                               **kwargs))
        self._TR= 2.*TR
        return self._TR

    def Tphi(self,**kwargs):
        """
        NAME:
           Tphi
        PURPOSE:
           Calculate the azimuthal period
        INPUT:
           +scipy.integrate.quadrature keywords
        OUTPUT:
           T_phi(R,vT,vT)/ro/vc + estimate of the error
        HISTORY:
           2010-12-01 - Written - Bovy (NYU)
        """
        if hasattr(self,'_Tphi'):
            return self._Tphi
        (rperi,rap)= self.calcRapRperi()
        if rap == rperi:#Circular orbit
            return nu.array([2.*m.pi*self._R/self._vT,0.])
        TR= self.TR(**kwargs)
        I= self.I(**kwargs)
        Tphi= nu.zeros(2)
        Tphi[0]= TR[0]/I[0]*m.pi
        Tphi[1]= Tphi[0]*m.sqrt((I[1]/I[0])**2.+(TR[1]/TR[0])**2.)
        self._Tphi= Tphi
        return self._Tphi

    def I(self,**kwargs):
        """
        NAME:
           I
        PURPOSE:
           Calculate I, the 'ratio' between the radial and azimutha period
        INPUT:
           +scipy.integrate.quadrature keywords
        OUTPUT:
           I(R,vT,vT) + estimate of the error
        HISTORY:
           2010-12-01 - Written - Bovy (NYU)
        """
        if hasattr(self,'_I'):
            return self._I
        (rperi,rap)= self.calcRapRperi()
        Rmean= m.exp((m.log(rperi)+m.log(rap))/2.)
        if rap == rperi: #Rough limit
            TR= self.TR()[0]
            Tphi= self.Tphi()[0]
            self._I= nu.array([TR/Tphi,0.])
            return self._I
        EL= calcELAxi(self._R,self._vR,self._vT,self._pot)
        E, L= EL
        I= 0.
        if Rmean > rperi:
            I+= nu.array(integrate.quadrature(_IAxiIntegrandSmall,
                                              0.,m.sqrt(Rmean-rperi),
                                              args=(E,L,self._pot,rperi),
                                              **kwargs))
        if Rmean < rap:
            I+= nu.array(integrate.quadrature(_IAxiIntegrandLarge,
                                               0.,m.sqrt(rap-Rmean),
                                               args=(E,L,self._pot,rap),
                                               **kwargs))
        self._I= I*self._R*self._vT
        return self._I

    def Jphi(self):
        """
        NAME:
           Jphi
        PURPOSE:
           Calculate the azimuthal action
        INPUT:
        OUTPUT:
           J_R(R,vT,vT)/ro/vc
        HISTORY:
           2010-12-01 - Written - Bovy (NYU)
        """
        return nu.array([self._R*self._vT,0.])

    def JR(self,**kwargs):
        """
        NAME:
           JR
        PURPOSE:
           Calculate the radial action for a power-law rotation curve
        INPUT:
           +scipy.integrate.quad keywords
        OUTPUT:
           J_R(R,vT,vT)/ro/vc + estimate of the error
        HISTORY:
           2010-12-01 - Written - Bovy (NYU)
        """
        if hasattr(self,'_JR'):
            return self._JR
        (rperi,rap)= self.calcRapRperi()
        EL= calcELAxi(self._R,self._vR,self._vT,self._pot)
        E, L= EL
        self._JR= (2.*nu.array(integrate.quad(_JRAxiIntegrand,rperi,rap,
                                              args=(E,L,self._pot),
                                              **kwargs)))
        return self._JR

    def calcRapRperi(self):
        """
        NAME:
           calcRapRperi
        PURPOSE:
           calculate the apocenter and pericenter radii for a power-law 
           rotation curve
        INPUT:
        OUTPUT:
           (rperi,rap)
        HISTORY:
           2010-12-01 - Written - Bovy (NYU)
        """
        if hasattr(self,'_rperirap'):
            return self._rperirap
        EL= calcELAxi(self._R,self._vR,self._vT,self._pot,vc=1.,ro=1.)
        E, L= EL
        if self._vR == 0. and self._vT > 1.: #We are exactly at pericenter
            rperi= self._R
            rend= _rapRperiAxiFindStart(self._R,E,L,self._pot,rap=True)
            rap= optimize.newton(_rapRperiAxiEq,rend,args=(E,L,self._pot),
                                 fprime=_rapRperiAxiDeriv)
        elif self._vR == 0. and self._vT < 1.: #We are exactly at apocenter
            rap= self._R
            rstart= _rapRperiAxiFindStart(self._R,E,L,self._pot)
            rperi= optimize.newton(_rapRperiAxiEq,rstart,
                                   args=(E,L,self._pot),
                                   fprime=_rapRperiAxiDeriv)
        elif self._vR == 0. and self._vT == 1.: #We are on a circular orbit
            rperi= self._R
            rap = self._R
        else:
            rstart= _rapRperiAxiFindStart(self._R,E,L,self._pot)
            rperi= optimize.brentq(_rapRperiAxiEq,rstart,self._R,
                                   (E,L,self._pot))
            rend= _rapRperiAxiFindStart(self._R,E,L,self._pot,rap=True)
            rap= optimize.brentq(_rapRperiAxiEq,self._R,rend,
                                 (E,L,self._pot))
        self._rperirap= (rperi,rap)
        return self._rperirap

def calcRapRperiFromELAxi(E,L,pot,vc=1.,ro=1.):
    """
    NAME:
       calcRapRperiFromELAxi
    PURPOSE:
       calculate the apocenter and pericenter radii
    INPUT:
       E - energy
       L - angular momemtum
       pot - potential
       vc - circular velocity
       ro - reference radius
    OUTPUT:
       (rperi,rap)
    HISTORY:
       2010-12-01 - Written - Bovy (NYU)
    """
    rstart= _rapRperiAxiFindStart(L,E,L)
    rperi= optimize.brentq(_rapRperiAxiEq,rstart,L,(E,L,pot))
    rend= _rapRperiAxiFindStart(L,E,L,rap=True)
    rap= optimize.brentq(_rapRperiAxiEq,L,rend,(E,L,pot))
    return (rperi,rap)

def calcELAxi(R,vR,vT,pot,vc=1.,ro=1.):
    """
    NAME:
       calcELAxi
    PURPOSE:
       calculate the energy and angular momentum
    INPUT:
       R - Galactocentric radius (/ro)
       vR - radial part of the velocity (/vc)
       vT - azimuthal part of the velocity (/vc)
       vc - circular velocity
       ro - reference radius
    OUTPUT:
       (E,L)
    HISTORY:
       2010-11-30 - Written - Bovy (NYU)
    """                           
    return (potentialAxi(R,pot)+vR**2./2.+vT**2./2.,R*vT)

def potentialAxi(R,pot,vc=1.,ro=1.):
    """
    NAME:
       potentialAxi
    PURPOSE:
       return the potential
    INPUT:
       R - Galactocentric radius (/ro)
       pot - potential
       vc - circular velocity
       ro - reference radius
    OUTPUT:
       Phi(R)
    HISTORY:
       2010-11-30 - Written - Bovy (NYU)
    """
    return evaluateplanarPotentials(R,pot)

def _JRAxiIntegrand(r,E,L,pot):
    """The J_R integrand"""
    return nu.sqrt(2.*(E-potentialAxi(r,pot))-L**2./r**2.)

def _TRAxiIntegrandSmall(t,E,L,pot,rperi):
    r= rperi+t**2.#part of the transformation
    return 2.*t/_JRAxiIntegrand(r,E,L,pot)

def _TRAxiIntegrandLarge(t,E,L,pot,rap):
    r= rap-t**2.#part of the transformation
    return 2.*t/_JRAxiIntegrand(r,E,L,pot)

def _IAxiIntegrandSmall(t,E,L,pot,rperi):
    r= rperi+t**2.#part of the transformation
    return 2.*t/_JRAxiIntegrand(r,E,L,pot)/r**2.

def _IAxiIntegrandLarge(t,E,L,pot,rap):
    r= rap-t**2.#part of the transformation
    return 2.*t/_JRAxiIntegrand(r,E,L,pot)/r**2.

def _rapRperiAxiEq(R,E,L,pot):
    """The vr=0 equation that needs to be solved to find apo- and pericenter"""
    return E-potentialAxi(R,pot)-L**2./2./R**2.

def _rapRperiAxiDeriv(R,E,L,pot):
    """The derivative of the vr=0 equation that needs to be solved to find 
    apo- and pericenter"""
    return evaluateplanarRforces(R,pot)+L**2./R**3.

def _rapRperiAxiFindStart(R,E,L,pot,rap=False):
    """
    NAME:
       _rapRperiAxiFindStart
    PURPOSE:
       Find adequate start or end points to solve for rap and rperi
    INPUT:
       R - Galactocentric radius
       E - energy
       L - angular momentum
       pot - potential
       rap - if True, find the rap end-point
    OUTPUT:
       rstart or rend
    HISTORY:
       2010-12-01 - Written - Bovy (NYU)
    """
    if rap:
        rtry= 2.*R
    else:
        rtry= R/2.
    while (E-potentialAxi(rtry,pot)-L**2./2./rtry**2) > 0.:
        if rap:
            rtry*= 2.
        else:
            rtry/= 2.
    return rtry
