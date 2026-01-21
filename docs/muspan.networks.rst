.. _networks:
muspan.networks
===============


.. currentmodule:: muspan.networks

The muspan.networks module provides tools for working with networks in the MuSpAn package. This module includes the following submodules:

.. rubric:: Network generation and manipulation


.. autosummary::
   :toctree: generated/
   :template: custom-function-template.rst
   :nosignatures:

   generate_network
   add_similarity_weight_to_edges
   add_dissimilarity_weight_to_edges


.. rubric:: Neighbourhood analysis methods


.. autosummary::
   :toctree: generated/
   :template: custom-function-template.rst
   :nosignatures:

   cluster_neighbourhoods
   khop_neighbourhood
   knn_label_count




.. rubric:: Network-based point pattern analysis


.. autosummary::
   :toctree: generated/
   :template: custom-function-template.rst
   :nosignatures:

   adjacency_permutation_test

.. rubric:: Network metrics


.. autosummary::
   :toctree: generated/
   :template: custom-function-template.rst
   :nosignatures:

   alpha_index
   centrality
   compactness
   cyclomatic_number
   edge_orientation_distribution
   gamma_index
   node_degree


.. rubric:: Network clustering


.. autosummary::
   :toctree: generated/
   :template: custom-function-template.rst
   :nosignatures:

   community_detection


.. rubric:: Network comparison methods

.. autosummary::
   :toctree: generated/
   :template: custom-function-template.rst
   :nosignatures:

   network_distance