.. _Installation:


Install
=======

The MuSpAn package can be installed using the Python package manager `pip`. Below are detailed instructions for installing MuSpAn. **Minimum Requirements**: Python 3.10-3.13 and pip: >=21.0.1


.. caution::
    If you are already using `conda` to manage your Python packages, you may encounter dependency conflicts when installing via `pip`. If issues occur using our `pip` installation, please follow the recommendations in the **Handling Conda and Pip Compatibility Issues** section.

.. image:: https://img.shields.io/badge/Python-3.10--3.13-blue
   :alt: Python 3.10–3.13
   

.. image:: https://img.shields.io/badge/Package-passing-brightgreen
   :alt: Package passing


.. image:: https://img.shields.io/badge/Tests-passing-brightgreen
   :alt: Tests passing
   :target: ./release_notes.html#test-summary

.. image:: https://img.shields.io/badge/DOI-10.1101/2024.12.06.627195-blue
   :alt: Package DOI
   :target: https://doi.org/10.1101/2024.12.06.627195


.. image:: https://img.shields.io/badge/Licence-Academic--Use-blue
   :alt: Licence Academic
   :target: https://docs.muspan.co.uk/MuSpAn_Academic_use_licence.pdf?_gl=1*177bju1*_ga*Njg3NjY2MDU1LjE3MzMyMjA2NDc.*_ga_NYJKGWRYPR*czE3NDg4NTU1MTUkbzM3MiRnMSR0MTc0ODg1NjU4MSRqNTckbDAkaDA 


Installing MuSpAn
------------------

Follow the steps below to install MuSpAn:

1. **Request the package**

   Visit our package request page (https://www.muspan.co.uk/get-the-code) and submit a request form.

2. **Receive credentials**

   Once your license has been approved by our team, you'll be emailed by code@muspan.co.uk with a **username** and **password** to access to the MuSpAn package (check your spam folder).

3. **Pip install the package**

   Use your terminal to download and install the package using the following command:

   .. code-block:: bash

        pip install https://docs.muspan.co.uk/code/latest.zip
   
   You'll be prompted to enter your **username** and **password**. Once entered, the package will be downloaded and installed.

4. **Verify the installation**

   Open a Python shell and try importing MuSpAn:

   .. code-block:: python

        import muspan as ms
        print("MuSpAn installed successfully!")

.. tip::
   To install a specific version of MuSpAn, replace 'latest' in the URL with an existing version number. For example, to install version 1.0.0, replace 'latest' with 'v1.0.0' as in the following command:
      
   .. code-block:: bash

      pip install https://docs.muspan.co.uk/code/v1.0.0.zip

Next Steps
----------

Once you have successfully installed MuSpAn, you can start analysing spatial data! We recommend checking out our :ref:`tutorials<tutorials>` to get started. For more information, refer to the :ref:`documentation<documentation>`. 

In addition, you can be a part of the MuSpAn discussion on our `Gitter community channel <https://app.gitter.im/#/room/#muspan-community:gitter.im>`_ which is our causal space for users to ask questions, share ideas and discuss the package. See you there!


Updating MuSpAn
----------------
We recommend updating MuSpAn regularly to access the latest features and bug fixes. To update MuSpAn, run the following command in your terminal:

.. code-block:: bash
      
      pip install https://docs.muspan.co.uk/code/latest.zip -U

You will be prompted to enter your **Username** and **password** given for your initial install. This process will update MuSpAn to the latest version. If conda environments are used, simply make a new environment with the updated version by following the **Handling Conda and Pip Compatibility Issues** procedure.


Handling Conda and Pip Compatibility Issues
-------------------------------------------

When using `conda` environments, mixing `conda` and `pip` installations can lead to dependency conflicts. 
If conflicts arise and MuSpAn installation fails, it is recommended to isolate MuSpAn in a virtual conda environment.
Follow these steps to create a fresh conda environment for MuSpAn installation:

1. **Create a fresh conda environment**

   .. code-block:: bash
    
            conda create -n muspan_env python=3.10
            conda activate muspan_env


2. **Install pip within the conda environment**

   Ensure `pip` is up to date and tied to the environment:

   .. code-block:: bash

        conda install pip
        python -m pip install --upgrade pip


3. **Install MuSpAn using pip**

   Follow the steps 1-4 in **Installing MuSpAn** outlined above to install MuSpAn.
      
The full list of dependencies is given below to reference any potential conflicts. If conflicts persist, consider isolating `MuSpAn` in a virtual environment or using a containerisation tool like Docker.

Installing MuSpAn from a local directory (legacy installation)
--------------------------------------------------------------

Follow the steps below to install MuSpAn if you have the MuSpAn.zip saved on your local machine:

1. **Extract the package**

   Unzip the folder named 'MuSpAn_vX.X.X' somewhere locally on your machine.

3. **Navigate to the directory**

   Use the terminal to navigate to the folder containing the downloaded package - named 'MuSpAn_vX.X.X'. Replace `path/to/muspan_folder` with the actual path:

   .. code-block:: bash

        cd path/to/MuSpAn_vX.X.X
   
4. **Install the package**

   Run the following command to install MuSpAn along with its dependencies:

   .. code-block:: bash
        
        pip install .
 

5. **Verify the installation**

   Open a Python shell and try importing MuSpAn:

   .. code-block:: python

        import muspan as ms
        print("MuSpAn installed successfully!")
   


Updating LLVM on macOS to Fix Clang Errors
------------------------------------------

If you encounter errors like unsupported 'fopenmp' when installing MuSpAn on macOS, you'll need to update LLVM (Low-Level Virtual Machine) on your system. Follow these simple steps:


1. **Install Homebrew**

   Homebrew is a package manager for macOS. If you don't already have it installed, run this command in the Terminal:

   .. code-block:: bash

        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. **Install LLVM Using Homebrew** 

   Once Homebrew is installed, use it to install LLVM by running in the Terminal:

   .. code-block:: bash

        brew install llvm

3. **Set clang as the Default Compiler**

   To use the updated clang provided by LLVM, set it as your default compiler by running the following commands in the Terminal:
   
   .. code-block:: bash

      export CC=/usr/local/opt/llvm/bin/clang
      export CXX=/usr/local/opt/llvm/bin/clang++


After running these commands, you should be able to install MuSpAn on your MacOS machine.

Dependencies
------------

Dependencies for MuSpAn V1.2.2 include the following packages:

* geojson>=3.1.0
* matplotlib>=3.9.0
* miniball>=1.2.0
* networkx>= 3.4
* numpy>=2.0
* pandas[parquet,feather,hdf5]>=2.2.3
* POT>=0.9.4
* ripser==0.6.14
* rust-geo-python==0.1.6
* scikit_learn>=1.5.2
* scipy>=1.14.1
* seaborn>=0.13.2
* setuptools>=72.1.0