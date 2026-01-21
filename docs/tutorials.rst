.. _tutorials:
Tutorials
=========

A solid understanding of MuSpAn is crucial to fully leveraging its capabilities in spatial data analysis.
To build a good foundational understanding of MuSpAn, we recommend starting with the Getting Started and Queries tutorial sets. 
Beyond this, each tutorial is largely self-contained, so you can dive into specific topics independently as needed. 
This flexible approach ensures you can learn at your own pace while focusing on the areas most relevant to your project.

.. carousel::
    :show_controls:
    :show_indicators:
    :show_dark:
    :show_fade:
    :show_shadows:

    .. image:: images/carousel_images/comm_1.png
       :target: _collections/network_analysis/Network%20methods%20-%202%20-%20community_detection.html
       :alt: Conversion of communities of contiguous cells into shape objects using MuSpAn

          
    .. image:: images/carousel_images/tcm_1.png
       :target: _collections/paper_tutorials/MuSpAn%20-%20Figure_6.html
       :alt: Computation of the Topographical Correlation Map between fibroblasts and macrophages in a colorectal tumour with regions annotated by carcinoma

    .. image:: images/carousel_images/rip_1.png
       :target: _collections/spatial_analysis_methods/Spatial%20stats%20-%205%20-%20RipleysK.html
       :alt: Demonstration of the discs about transcripts used to compute cross-Ripley's function within a cell, correcting for boundaries

    .. image:: images/carousel_images/ph_1.png
       :target: _collections/topology/Topology%201%20-%20persistent%20homology.html
       :alt: Demonstration of the stages of the underlying connectivity in a Vietoris-Rips filteration (topological data analysis) in colorectal epithelium

    .. image:: images/carousel_images/crop_1.png
       :target: _collections/workflows/Workflows%20-%201%20-%20Cropping%20a%20domain.html
       :alt: Demonstration of a workflow of generating a cropped MuSpAn domain from an existing domain using a hexagonal lattice

    .. image:: images/carousel_images/pcf_1.png
       :target: _collections/spatial_analysis_methods/Spatial%20stats%20-%201%20-%20pcf.html
       :alt: Demonstration of the annuli about cells used to compute cross-Pair Correlation Function within a region of colon, correcting for boundaries

    .. image:: images/carousel_images/art_1.png
       :target: _collections/misc/2025%20Math%20Onco%20Art.html
       :alt: A creatative MuSpAn domain with points and networks filtered by a large MuSpAn logo demonstration the control of interactions between point objects, shape objects, networks and labels

    .. image:: images/carousel_images/dist_1.png
       :target: _collections/paper_tutorials/MuSpAn%20-%20Figure_3.html
       :alt: Visual demonstration of the true shape-shape distance computations implemented in MuSpAn, showing nearest neighbourhoods from orange cells to purple cells.

    .. image:: images/carousel_images/lattice_1.png
       :target: _collections/spatial_analysis_methods/Spatial%20stats%20-%204%20-%20Spatial%20autocorrelation.html
       :alt: Visualisation of a hexagonal lattice overlaid on a MuSpAn domain with individual hexagons colored by density of neutrophils and Getis Ord of macrophages
     

While the MuSpAn tutorials are presented within the context of cellular biology, the methods and tools are broadly applicable to any form of spatial data. 
We hope these examples not only guide you through the software but also spark ideas for using MuSpAn in your own research—whatever your field may be!


.. note::
     MuSpAn is a broad framework for spatial analysis and these tutorials only cover a small subset of the available functionality. 
     We're working hard to expand the tutorial collection, so if you have a specific topic in mind that you'd like to see covered, `please let us know! <https://app.gitter.im/#/room/#muspan-community:gitter.im>`_
     

Getting Started
---------------
.. nbgallery::
     _collections/getting_started/Getting Started - 1 - Domains
     _collections/getting_started/Getting Started - 2 - Introducing labels
     _collections/getting_started/Getting Started - 3 - Shapes
     _collections/getting_started/Getting Started - 4 - Saving and loading domains
     _collections/getting_started/Getting Started - 5 - Estimating boundaries

Queries
------- 
.. nbgallery::
     _collections/queries/Queries - 1 - What is a query
     _collections/queries/Queries - 2 - understanding a query
     _collections/queries/Queries - 3 - combining queries
     _collections/queries/Queries - 4 - Containing query
     _collections/queries/Queries - 5 - Distance-based query

Working with Objects
--------------------
.. nbgallery::
     _collections/working_with_objects/WWO - 1 - shapes to points
     _collections/working_with_objects/WWO - 2 - shapes to points 2
     _collections/working_with_objects/WWO - 3 - points to shape 3
     _collections/working_with_objects/WWO - 4 - points to shape 1
     _collections/working_with_objects/WWO - 5 - points to shape 2


Spatial Networks
----------------
.. nbgallery::
     _collections/spatial_networks/Spatial net - Creating networks 1
     _collections/spatial_networks/Spatial net - Creating networks 2
     _collections/spatial_networks/Spatial net - Creating networks 3
     _collections/spatial_networks/Spatial net - Subnetworks from queries

Spatial Statistics
------------------
.. nbgallery::
     _collections/spatial_analysis_methods/Spatial stats - 1 - pcf
     _collections/spatial_analysis_methods/Spatial stats - 2 - boundary corrections
     _collections/spatial_analysis_methods/Spatial stats - 3 - wPCF
     _collections/spatial_analysis_methods/Spatial stats - 4 - Spatial autocorrelation
     _collections/spatial_analysis_methods/Spatial stats - 5 - RipleysK



Spatial Network Analysis
------------------------
.. nbgallery::
     _collections/network_analysis/Network methods - 1 - neighbourhood_analysis
     _collections/network_analysis/Network methods - 4 - neighbourhood_analysis_continuous
     _collections/network_analysis/Network methods - 5 - visualising_neighbourhood_clusters
     _collections/network_analysis/Network methods - 3 - graph_filtrations
     _collections/network_analysis/Network methods - 2 - community_detection
     _collections/spatial_networks/Spatial net - Comparing networks


Topological Data Analysis
-------------------------
.. nbgallery::
     _collections/topology/Topology 1 - persistent homology
     _collections/topology/Topology 2 - level set filtration
     _collections/topology/Topology 3 - persistence vectorisation

Region-based Analysis
---------------------

.. nbgallery::
     _collections/region_based_analysis/generating_hexgrids
     _collections/region_based_analysis/generating_quadrats
     _collections/region_based_analysis/quadrat_correlation

Distribution Analysis
---------------------
.. nbgallery::
     _collections/distribution_analysis/Distribution 1 - KDE
     _collections/distribution_analysis/Distribution 2 - Distributions in shapes
     _collections/distribution_analysis/Distribution 3 - Comparing distributions

Quantifying Morphology
----------------------
.. nbgallery::
     _collections/geometry/geometry - 1 - standard metrics
     _collections/geometry/geometry - 2 - principle axis


Workflows
---------
.. nbgallery::
     _collections/workflows/Workflows - 1 - Cropping a domain
     _collections/workflows/Workflows - 2 - Domain to csv


Importing Data from Specific Platforms
--------------------------------------
.. nbgallery::
     _collections/importing_data/Importing data from QuPath
     _collections/importing_data/Importing a spatialData dataset
     _collections/importing_data/Importing a Xenium dataset
     _collections/importing_data/Importing a Visium dataset

Extras
------
.. nbgallery::
     _collections/misc/2025 Math Onco Art

