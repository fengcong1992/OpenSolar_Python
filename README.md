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

This is an R package, so you need to install [R](https://www.r-project.org/) on your computer first. In addition, [RStudio](https://www.rstudio.com/) is an integrated development environment (IDE) for R; it is highly recommended.

### Installing

Once R and RStudio are installed. Open R or RStudio and install the [devtools](https://cran.r-project.org/web/packages/devtools/index.html) package, which allows you to install R package from GitHub

```
install.packages("devtools")
```

Load the package that you just installed

```
library("devtools")
```

Now, you can install the SolMod package, using

```
install_github("UTD-DOES/OpenSolar")
```

## Running the tests

This code segment is to test if the package is sucessfully downloaded and list the functions in the package.

```
library(OpenSolar)
lsf.str('package:OpenSolar')
```

## License

This package is under the GPL-2 license.
