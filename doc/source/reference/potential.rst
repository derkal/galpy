Potential
=========

3D potentials
-------------

General instance routines
+++++++++++++++++++++++++


.. toctree::
   :maxdepth: 2

   __call__ <potentialcall.rst>
   dens <potentialdens.rst>
   phiforce <potentialphiforce.rst>
   plot <potentialplot.rst>
   plotEscapecurve <potentialplotescapecurve.rst>
   plotRotcurve <potentialplotrotcurve.rst>
   Rforce <potentialrforce.rst>
   toPlanar <potentialtoplanar.rst>
   toVertical <potentialtovertical.rst>
   zforce <potentialzforce.rst>


General 3D potential routines
+++++++++++++++++++++++++++++

.. toctree::
   :maxdepth: 2

   evaluateDensities <potentialdensities.rst>
   evaluatephiforces <potentialphiforces.rst>
   evaluatePotentials <potentialevaluate.rst>
   evaluateRforces <potentialrforces.rst>
   evaluatezforces <potentialzforces.rst>
   plotEscapecurve <potentialplotescapecurves.rst>
   plotPotentials <potentialplots.rst>
   plotRotcurve <potentialplotrotcurves.rst>

Specific potentials
++++++++++++++++++++

.. toctree::
   :maxdepth: 2

   potentialdoubleexp.rst
   potentialdoublepowerspher.rst
   potentialjaffe.rst
   potentialhernquist.rst
   potentialkepler.rst
   potentialloghalo.rst
   potentialmiyamoto.rst
   potentialnfw.rst
   potentialpowerspher.rst


2D potentials
-------------

General instance routines
+++++++++++++++++++++++++

.. toctree::
   :maxdepth: 2

   __call__ <potential2dcall.rst>
   phiforce <potential2dphiforce.rst>
   Rforce <potential2drforce.rst>

General axisymmetric potential instance routines
++++++++++++++++++++++++++++++++++++++++++++++++

.. toctree::
   :maxdepth: 2

   plot <potential2dplot.rst>
   plotEscapecurve <potential2dplotescapecurve.rst>
   plotRotcurve <potential2dplotrotcurve.rst>


General 2D potential routines
+++++++++++++++++++++++++++++

.. toctree::
   :maxdepth: 2

   evaluateplanarphiforces <potential2dphiforces.rst>
   evaluateplanarPotentials <potential2devaluate.rst>
   evaluateplanarRforces <potential2drforces.rst>
   plotEscapecurve <potentialplotescapecurves.rst>
   plotplanarPotentials <potential2dplots.rst>
   plotRotcurve <potentialplotrotcurves.rst>

Specific potentials
++++++++++++++++++++

No specifically two-dimensional potentials are available at this time,
but all of the 3D potentials above can be used as two-dimensional
potentials in the mid-plane. 

.. toctree::
   :maxdepth: 2

   RZToplanarPotential <potential2dRZtoplanar.rst>



1D potentials
-------------

General instance routines
+++++++++++++++++++++++++

.. toctree::
   :maxdepth: 2

   __call__ <potential1dcall.rst>
   force <potential1dforce.rst>
   plot <potential1dplot.rst>


General 1D potential routines
+++++++++++++++++++++++++++++

.. toctree::
   :maxdepth: 2

   evaluatelinearForces <potential1dforces.rst>
   evaluatelinearPotentials <potential1devaluate.rst>
   plotlinearPotentials <potential1dplots.rst>

Specific potentials
++++++++++++++++++++

.. toctree::
   :maxdepth: 2

   KGPotential <potentialkg.rst>

One-dimensional potentials can also be derived from 3D axisymmetric potentials as the vertical potential at a certain Galactocentric radius

.. toctree::
   :maxdepth: 2

   RZToverticalPotential <potential1dRZtolinear.rst>