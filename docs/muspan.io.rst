.. _io:
muspan.io 
=========


.. currentmodule:: muspan.io
   
The muspan.io module provides tools for reading and writing data to and from the MuSpAn package. This module includes the following submodules:


.. rubric:: MuSpAn domain input/output

.. autosummary::
   :toctree: generated/
   :template: custom-function-template.rst
   :nosignatures:

   save_domain
   load_domain
   domain_to_csv
   domain_to_parquet
   domain_to_hdf


.. rubric:: Helper input methods for specific platforms

.. autosummary::
   :toctree: generated/
   :template: custom-function-template.rst
   :nosignatures:

   qupath_to_domain
   xenium_to_domain
   spatialdata_to_domain



.. rubric:: IO helpers

.. autosummary::
   :toctree: generated/
   :template: custom-function-template.rst
   :nosignatures:

   helpers.domain_to_dataframe