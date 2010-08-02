import math as m
import numpy as nu
from scipy import integrate
from galpy.potential_src.Potential import evaluateRforces, evaluatezforces,\
    evaluatePotentials, evaluatephiforces
import galpy.util.bovy_plot as plot
from OrbitTop import OrbitTop
class FullOrbit(OrbitTop):
    """Class that holds and integrates orbits in full 3D potentials"""
    def __init__(self,vxvv=[1.,0.,0.9,0.,0.1]):
        """
        NAME:
           __init__
        PURPOSE:
           intialize a full orbit
        INPUT:
           vxvv - initial condition [R,vR,vT,z,vz,phi]
        OUTPUT:
           (none)
        HISTORY:
           2010-08-01 - Written - Bovy (NYU)
        """
        self.vxvv= vxvv
        return None

    def integrate(self,t,pot):
        """
        NAME:
           integrate
        PURPOSE:
           integrate the orbit
        INPUT:
           t - list of times at which to output (0 has to be in this!)
           pot - potential instance or list of instances
        OUTPUT:
           (none) (get the actual orbit using getOrbit()
        HISTORY:
           2010-08-01 - Written - Bovy (NYU)
        """
        self.t= nu.array(t)
        self.orbit= _integrateFullOrbit(self.vxvv,pot,t)

    def plot(self,*args,**kwargs):
        """
        NAME:
           plot
        PURPOSE:
           plot a previously calculated orbit
        INPUT:
           matplotlib.plot inputs+bovy_plot.plot inputs
        OUTPUT:
           sends plot to output device
        HISTORY:
           2010-07-10 - Written - Bovy (NYU)
        """
        plot.bovy_plot(self.orbit[:,0],self.orbit[:,3],*args,**kwargs)

    def plotEt(self,pot,*args,**kwargs):
        """
        NAME:
           plotEt
        PURPOSE:
           plot E(t) along the orbit
        INPUT:
           pot - Potential instance or list of instances in which the orbit was
                 integrated
           +bovy_plot.bovy_plot inputs
        OUTPUT:
           figure to output device
        HISTORY:
           2010-07-10 - Written - Bovy (NYU)
        """
        self.E= [evaluatePotentials(self.orbit[ii,0],self.orbit[ii,3],
                                    self.orbit[ii,5],pot)+
                 self.orbit[ii,1]**2./2.+self.orbit[ii,2]**2./2.+
                 self.orbit[ii,4]**2./2. for ii in range(len(self.t))]
        plot.bovy_plot(nu.array(self.t),nu.array(self.E)/self.E[0],
                       *args,**kwargs)

    def plotEzt(self,pot,*args,**kwargs):
        """
        NAME:
           plotEzt
        PURPOSE:
           plot E_z(t) along the orbit
        INPUT:
           pot - Potential instance or list of instances in which the orbit was
                 integrated
           +bovy_plot.bovy_plot inputs
        OUTPUT:
           figure to output device
        HISTORY:
           2010-07-10 - Written - Bovy (NYU)
        """
        self.Ez= [evaluatePotentials(self.orbit[ii,0],self.orbit[ii,3],
                                     self.orbit[ii,5],pot)-
                  evaluatePotentials(self.orbit[ii,0],0.,self.orbit[ii,5],pot)+
                  self.orbit[ii,4]**2./2. for ii in range(len(self.t))]
        plot.bovy_plot(nu.array(self.t),nu.array(self.Ez)/self.Ez[0],
                       *args,**kwargs)

    def _callRect(self,*args):
        kwargs['rect']= False
        vxvv= self.__call__(*args,**kwargs)
        x= vxvv[0]*m.cos(vxvv[5])
        y= vxvv[0]*m.sin(vxvv[5])
        vx= vxvv[1]*m.cos(vxvv[5])-vxvv[2]*m.sin(vxvv[5])
        vy= -vxvv[1]*m.sin(vxvv[5])-vxvv[2]*m.cos(vxvv[5])
        return nu.array([x,y,vxvv[3],vx,vy,vxvv[4]])

def _integrateFullOrbit(vxvv,pot,t):
    """
    NAME:
       _integrateFullOrbit
    PURPOSE:
       integrate an orbit in a Phi(R,z,phi) potential
    INPUT:
       vxvv - array with the initial conditions stacked like
              [R,vR,vT,z,vz,phi]; vR outward!
       pot - Potential instance
       t - list of times at which to output (0 has to be in this!)
    OUTPUT:
       [:,5] array of [R,vR,vT,z,vz,phi] at each t
    HISTORY:
       2010-08-01 - Written - Bovy (NYU)
    """
    vphi= vxvv[2]/vxvv[0]
    init= [vxvv[0],vxvv[1],vxvv[5],vphi,vxvv[3],vxvv[4]]
    intOut= integrate.odeint(_FullEOM,init,t,args=(pot,),
                             rtol=10.**-8.)#,mxstep=100000000)
    out= nu.zeros((len(t),6))
    out[:,0]= intOut[:,0]
    out[:,1]= intOut[:,1]
    out[:,2]= out[:,0]*intOut[:,3]
    out[:,3]= intOut[:,4]
    out[:,4]= intOut[:,5]
    out[:,5]= intOut[:,2]
    return out

def _FullEOM(y,t,pot):
    """
    NAME:
       _FullEOM
    PURPOSE:
       implements the EOM, i.e., the right-hand side of the differential 
       equation
    INPUT:
       y - current phase-space position
       t - current time
       pot - (list of) Potential instance(s)
    OUTPUT:
       dy/dt
    HISTORY:
       2010-04-16 - Written - Bovy (NYU)
    """
    l2= (y[0]**2.*y[3])**2.
    return [y[1],
            l2/y[0]**3.+evaluateRforces(y[0],y[4],y[2],pot),
            y[3],
            1./y[0]**2.*(evaluatephiforces(y[0],y[4],y[2],pot)-
                         2.*y[0]*y[1]*y[3]),
            y[5],
            evaluatezforces(y[0],y[4],y[2],pot)]