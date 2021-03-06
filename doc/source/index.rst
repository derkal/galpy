.. galpy documentation master file, created by
   sphinx-quickstart on Sun Jul 11 15:58:27 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to galpy's documentation
=================================

galpy is a python package for galactic dynamics. It supports orbit
integration in a variety of potentials, evaluating and sampling
various distribution functions, and the calculation of action-angle
coordinates for all static potentials.

Quick-start guide
-----------------

.. toctree::
   :maxdepth: 2

   installation.rst

   getting_started.rst

   potential.rst

   basic_df.rst

   orbit.rst

   actionAngle.rst

   diskdf.rst

Library reference
-----------------

.. toctree::
   :maxdepth: 2

   reference/orbit.rst

   reference/potential.rst

   reference/df.rst

   reference/aa.rst

   reference/util.rst


Tutorials
---------

.. toctree::
   :maxdepth: 1

   streamdf.rst

Papers using galpy
--------------------

Please let me (bovy -at- ias.edu) know if you make use of ``galpy`` in a publication.

* *Tracing the Hercules stream around the Galaxy*, Jo Bovy (2010), *Astrophys. J.* **725**, 1676 (`2010ApJ...725.1676B <http://adsabs.harvard.edu/abs/2010ApJ...725.1676B>`_): 
  	   Uses what later became the orbit integration routines and Dehnen and Shu disk distribution functions.
* *The spatial structure of mono-abundance sub-populations of the Milky Way disk*, Jo Bovy, Hans-Walter Rix, Chao Liu, et al. (2012), *Astrophys. J.* **753**, 148 (`2012ApJ...753..148B <http://adsabs.harvard.edu/abs/2012ApJ...753..148B>`_):
       Employs galpy orbit integration in ``galpy.potential.MWPotential`` to characterize the orbits in the SEGUE G dwarf sample.
* *On the local dark matter density*, Jo Bovy & Scott Tremaine (2012), *Astrophys. J.* **756**, 89 (`2012ApJ...756...89B <http://adsabs.harvard.edu/abs/2012ApJ...756...89B>`_):
      Uses ``galpy.potential`` force and density routines to characterize the difference between the vertical force and the surface density at large heights above the MW midplane.
* *The Milky Way's circular velocity curve between 4 and 14 kpc from APOGEE data*, Jo Bovy, Carlos Allende Prieto, Timothy C. Beers, et al. (2012), *Astrophys. J.* **759**, 131 (`2012ApJ...759..131B <http://adsabs.harvard.edu/abs/2012ApJ...759..131B>`_):
       Utilizes the Dehnen distribution function to inform a simple model of the velocity distribution of APOGEE stars in the Milky Way disk and to create mock data.
* *A direct dynamical measurement of the Milky Way's disk surface density profile, disk scale length, and dark matter profile at 4 kpc < R < 9 kpc*, Jo Bovy & Hans-Walter Rix (2013), *Astrophys. J.* **779**, 115 (`2013ApJ...779..115B <http://adsabs.harvard.edu/abs/2013ApJ...779..115B>`_):
     Makes use of potential models, the adiabatic and Staeckel actionAngle modules, and the quasiisothermal DF to model the dynamics of the SEGUE G dwarf sample in mono-abundance bins.
* *The peculiar pulsar population of the central parsec*, Jason Dexter & Ryan M. O'Leary (2013), *Astrophys. J. Lett.*, submitted (`arXiv/1310.7022 <http://arxiv.org/abs/1310.7022>`_):
     Uses galpy for orbit integration of pulsars kicked out of the Galactic center.
* *Chemodynamics of the Milky Way. I. The first year of APOGEE data*, Friedrich Anders, Christina Chiappini, Basilio X. Santiago, et al. (2013), *Astron. & Astrophys.* submitted (`arXiv/1311.4549 <http://arxiv.org/abs/1311.4549>`_):
  		 Employs galpy to perform orbit integrations in ``galpy.potential.MWPotential`` to characterize the orbits of stars in the APOGEE sample.

* *Dynamical modeling of tidal streams*, Jo Bovy (2014), *Astrophys. J*, submitted (`arXiv/1401.2985 <http://arxiv.org/abs/1401.2985>`_):
    Introduces ``galpy.df.streamdf`` and ``galpy.actionAngle.actionAngleIsochroneApprox`` for modeling tidal streams using simple models formulated in action-angle space (see the tutorial above).

Acknowledging galpy
--------------------

Please link back to ``http://github.com/jobovy/galpy`` . When using the ``galpy.actionAngle.actionAngleAdiabatic`` and ``galpy.actionAngle.actionAngleStaeckel`` modules, please cite `2013ApJ...779..115B <http://adsabs.harvard.edu/abs/2013ApJ...779..115B>`_ in addition to the papers describing the algorithm used. When using ``galpy.actionAngle.actionAngleIsochroneApprox``, please cite `arXiv/1401.2985 <http://arxiv.org/abs/1401.2985>`_, which introduced this technique. When orbit integrations are used, you could cite `2010ApJ...725.1676B <http://adsabs.harvard.edu/abs/2010ApJ...725.1676B>`_ (first galpy paper).


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

