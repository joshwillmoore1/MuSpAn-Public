.. glossary::
Glossary
========

.. toctree::
   :maxdepth: 2
    :caption: Contents:

MuSpAn is built on mathematical prinicples in design and practise, making it a very general framework for spatial data analysis. 
With generality comes the need for a common language to describe the various components of the package.
To this end, we have provided a glossary of terms used in our package.

.. list-table:: Glossary
    :widths: 20 80
    :header-rows: 1

    * - **Keyword**
      - **Definition**
    * - Domain
      - A domain is the base class for MuSpAn that represents a spatial region. All spatial data and metadata is stored in a domain.
    * - Vertices
      - Verices are lowest level of data in MuSpAn which are defined by (x, y) coordinates in 2D space.
        Vertices are the basic building blocks of all spatial data in MuSpAn. 
    * - Object
      - An object is a generic representation of spatial data. 
        Objects can be points, lines or shapes and that could represent biological entities such as cells, neighbourhoods or regions of tissue.
        Objects are constructed from vertices and are the primary data structure in MuSpAn. 
        Each object has a unique identifier called Object ID.   
    * - Point
      - A point is a 0-dimensional object that represents a single location in space. 
    * - Line
      - A line is a 1-dimensional object that represents a sequence of points in space. 
    * - Shape
      - A shape is a 2-dimensional object that represents a region in space. Shapes can be simple polygons or contain internal voids. 
    * - Collection
      - A collection is a group of objects in a domain. 
    * - Label
      - Labels are used to assign metadata to objects in a domain. Labels can be used to filter objects in a domain based on their metadata. Labels values can be categorical or continuous.
    * - Query
      - A query is a set of conditions that are used to filter objects in a domain. 
    * - Population
      - A population is a subset of objects in a domain. A populations are usually defined by a query.
    * - Boundary
      - A boundary represents a region within the domain. Objects can be filtered by their inclusion or exclusion from a boundary in analysis.
    * - Parent
      - A parent object is an object that was used to create another object.
    * - Child
      - A child object is an object that was created from another object.

    
    

