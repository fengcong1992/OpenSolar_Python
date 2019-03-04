# OpenSolar_Python: Promoting the Openness and Accessibility of Diverse Public Solar Datasets - Python version

Solar data is the foundation of data-driven research in solar power grid integration and power system operations. Compared to other fields in data science, the openness and accessibility of solar data fall behind, which prevents solar data science from catching up with the emerging trend of data science (e.g., deep learning). In this repository, OpenSolar, an R package, is developed to enhance the openness and accessibility of publicly available solar datasets. The OpenSolar package provides access to multiple formats of data with diverse measurements in 4 datasets, which are:
- the National Renewable Energy Laboratory (NREL) [Solar Power Data for Integration Studies (SPDIS)](https://www.nrel.gov/grid/solar-power-data.html) dataset
- the NREL [Solar Radiation Research Laboratory (SRRL)](https://midcdmz.nrel.gov/apps/go2url.pl?site=BMS) dataset
- the [Sheffield Solar-Microgen](https://www.solar.sheffield.ac.uk/all-projects/microgen-database/) database
- the [Dataport](https://dataport.cloud) database. 

Different from other open solar datasets that only contain meteorological data, the 4 datasets in the OpenSolar package also consists of behind-the-meter data, sky images, and solar power data with satisfactory temporal and spatial resolution and coverage. The overview, quality control methods, and potential usage of the datasets, in conjunction with the sample code of implementing the OpenSolar functions, are described. The package is expected to assist in bridging the gaps among solar energy, power systems, and machine/deep learning research.			

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

This is an Python package, so you need to install [Python](https://www.python.org) on your computer first.

### Installing

Once Python is installed, please make sure [pip](https://pypi.org/project/pip/), the Python package installer, is also installed. Then the OpenSolar package (named OpenSolar_Python) can be downloaded from the [Github repository](https://github.com/fengcong1992/OpenSolar_Python)

```
pip install git+https://github.com/fengcong1992/OpenSolar_Python
```
