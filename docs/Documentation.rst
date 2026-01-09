.. _documentation:
Documentation
=============
MuSpAn is organised into several modules, each of which provides tools for working with different aspects of spatial data and analysis.
The organisation of the package is designed to group tools and spatial analysis methods that are closely related in terms of their functionality and mathematical underpinnings. 

.. list-table::
  :header-rows: 1

  * - Subpackage
    - Description
  * - :ref:`domain<domain>`
    - A container for spatial data
  * - :ref:`objects<objects>`
    - Objects that can be used to represent spatial data
  * - :ref:`query<query>`
    - Querying and filtering domain objects
  * - :ref:`shape_operations<shape_operations>`
    - Manipulating shape objects
  * - :ref:`spatial_statistics<spatial_statistics>`
    - Spatial statistics for spatial data
  * - :ref:`region_based<region_based>`
    - Region-based analysis of spatial data
  * - :ref:`networks<networks>`
    - Network analysis for spatial data
  * - :ref:`geometry<geometry>`
    - Geometric descriptors of shape-like objects
  * - :ref:`topology<topology>`
    - Topological data analysis of spatial data
  * - :ref:`distribution<distribution>`
    - Distribution analysis of spatial data
  * - :ref:`summary_statistics<summary_statistics>`
    - Non-spatial summary statistics 
  * - :ref:`visualise<visualise>`
    - Visualisation of spatial data and analysis results
  * - :ref:`io<io>`
    - Data input and output helper operations 
  * - :ref:`datasets<datasets>`
    - Datasets for testing and demonstration
  * - :ref:`helpers<helpers>`
    - Helper functions for spatial analysis and data manipulation


Overall, the MuSpAn package can conveniently be divided into three main categories of submodules: 

1. **Core functionality**: This includes the core classes and functions that are used to generate, manipulate, view and filter the spatial data contained within a spatial domain.

2. **Spatial analysis**:  These modules provide a range of tools for analysing spatial data subcategorised by type of mathematical underpinnings.

3. **Extra features**: These modules provide extra features that are not strictly necessary for the core functionality of the package, but are useful for specific applications or use cases. This includes modules data input and output, helper functions and example datasets for demonstration and method development.

.. image:: images/ms_overview.png
    :align: center

.. raw:: html

  <div style="margin-bottom: 0.5em;"></div>
Most important of these is a MuSpAn domain object, which is a container for all the spatial data. The domain object is the main entry point for working with the MuSpAn package, and it provides a convenient way to access all of the functionality of the package.

.. raw:: html

  <div style="display: flex; gap: 2em; align-items: center; text-align:justify;">

    <div style="flex: 1;">
      <p>
        In a typical workflow, the user begins by creating a MuSpAn domain object and adding spatial data to it. Metadata is linked to objects via labels. All objects and their associated metadata are stored within the MuSpAn domain. 
        From there, subsets of the data can be filtered using the query module, and visualised through the visualisation module. These filtered subsets can then undergo spatial analysis, with the results also available for visualisation and further downstream analysis.
        All outputs can be saved either through standard Python methods or via the MuSpAn IO module.      
      </p>

    </div>

    <div style="flex: 1; text-align: center;">
      <img src="_static/static_images/ms_workflow.png" alt="MuSpAn Workflow" style="display: block; margin: 0 auto; width: 100%;">
    </div>

  </div>
    
.. raw:: html

  <div style="margin-bottom: 0.5em;"></div>

With the support of detailed documentation, tutorials, and paper examples, the MuSpAn package empowers users to thoroughly explore and analyse spatial data—from initial investigation to the integration and development of high-throughput pipelines. We encourage the use of MuSpAn in existing and new data analysis pipelines.

Import functions from MuSpAn
----------------------------

All of the functions and classes in the MuSpAn package are publically available and can be imported using the following import statement:
::

    import muspan

Or alternatively, you can import specific functions or classes from the package. For example, if we only wanted use a specific function, say ``network_distance`` from the networks module, we could import it as follows:
::

    from muspan.networks import network_distance
    distance = network_distance(...)



MuSpAn reference list
---------------------

All of the modules are listed below, and each module has its own documentation page that provides a detailed description of the functions and classes that are available in that module.



.. toctree::
   :maxdepth: 4
   
   muspan.domain
   muspan.objects
   muspan.visualise
   muspan.shape_operations
   muspan.shape_operation.helpers
   muspan.networks
   muspan.query
   muspan.geometry
   muspan.spatial_statistics
   muspan.summary_statistics
   muspan.topology
   muspan.distribution
   muspan.region_based
   muspan.io
   muspan.datasets
   muspan.helpers
