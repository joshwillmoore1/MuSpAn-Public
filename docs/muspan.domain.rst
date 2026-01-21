.. _domain:

muspan.domain
=============

Overview
--------

A :ref:`muspan.domain <domain_class>` represents a container for spatial data in MuSpAn. 
It acts as the central object in which geometric objects, labels, and spatial relationships are defined, updated, and queried throughout an analysis.

A domain is responsible for:

- defining the spatial extent of an analysis,
- storing pointclouds, shapeclouds, and associated labels,
- managing derived spatial structures such as boundaries and object groupings,
- maintaining visualisation attributes and other analysis state required by downstream workflows.

In typical workflows, a domain is created once at the start of an analysis, populated with geometric data, and then progressively updated as spatial relationships and derived structures are computed.

This page documents the public API of the :ref:`muspan.domain <domain_class>` class. 
The method summaries below provide a structured index of common domain operations, grouped by their role in the analysis workflow. 
Each summary entry links directly to its full documentation in the :ref:`class reference <domain_class>` section.

.. currentmodule:: muspan.domain


Adding data to the domain
------------------------

.. autosummary::
   :nosignatures:

   domain.add_points
   domain.add_lines
   domain.add_shapes
   domain.add_shapes_with_internal_holes
   domain.add_labels


Updating domain properties
--------------------------

.. autosummary::
   :nosignatures:

   domain.estimate_boundary
   domain.simplify_shape_boundaries
   domain.update_colors
   domain.convert_objects


Inspecting domain contents
--------------------------

.. autosummary::
   :nosignatures:

   domain.print_labels
   domain.print_collections


Removing data and derived structures
------------------------------------

.. autosummary::
   :nosignatures:

   domain.delete_distances
   domain.delete_network
   domain.delete_labels
   domain.delete_objects


Class reference
---------------

.. _domain_class:

.. autoclass:: muspan.domain.domain
   :members:
