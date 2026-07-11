# Climate-Data-Downloader

Python scripts for downloading ERA5-Land, CHIRPS v2.0, and SARAH-3 climate datasets, developed as part of a PhD research pipeline on climate variability and fossil fuel energy intensity in West African Craton (WAC) gold mining operations.

## Overview

This repository provides reproducible download workflows for three climate data sources used to characterize temperature, precipitation, and solar irradiance across 21 gold mine sites in Burkina Faso, Côte d'Ivoire, Ghana, and Mali:

| Source | Variable | Access method | Resolution |
|---|---|---|---|
| **ERA5-Land** | Temperature, precipitation | Copernicus CDS API | 0.1° |
| **CHIRPS v2.0** | Precipitation | FTP (UCSB Climate Hazards Group) | 0.05° |
| **SARAH-3** | Solar irradiance | EUMETSAT Data Store (Metalink XML + API) | ~0.05° |

## Repository Structure

```
Climate_Data_Downloader/
├── Downloader/
│   └── Output/
│       └── NetCDF/
│           ├── ERA5_Land/     # local only, not tracked by Git
│           ├── sarah3/        # local only, not tracked by Git
│           └── Chirp/         # local only, not tracked by Git
├── Notebook/
│   ├── era5_land.ipynb
│   └── Sarah3.ipynb
├── Scripts/
│   ├── era5_land.py
│   └── Sarah3.py
├── .gitignore
└── README.md
```

> **Note:** Downloaded NetCDF files are not version-controlled (see `.gitignore`). This repository contains only the code required to reproduce the downloads, not the datasets themselves.

## Requirements

- Python 3.10+
- Jupyter Notebook (workflows are developed and tested in Jupyter, using `Path.cwd()` for path resolution; no `argparse`, to remain compatible with the Jupyter kernel)
- Key libraries: `xarray`, `netCDF4`, `h5py`, `ftplib`, `pathlib`, `cdsapi`

Install dependencies:

```bash
pip install xarray netCDF4 h5py cdsapi
```

## Data Sources & Access Setup

### ERA5-Land (Copernicus CDS API)

1. Create a free account at https://cds.climate.copernicus.eu
2. Set up your API credentials in a `.cdsapirc` file in your home directory (this file is excluded from version control — never commit it)
3. Run `Scripts/era5_land.py` or `Notebook/era5_land.ipynb`

### CHIRPS v2.0 (FTP)

Downloaded manually via FTP from:
`ftp://ftp.chc.ucsb.edu/pub/org/chc/products/CHIRPS-2.0/global_monthly/netcdf/`

> Automated FTP download may fail on networks blocking port 21; in that case, connect via a standard FTP client (e.g., Windows File Explorer: `ftp://...`) instead.

### SARAH-3 (EUMETSAT Data Store)

1. Create an account at the EUMETSAT Data Store
2. Export a Metalink XML file for the desired product/date range
3. Run `Scripts/Sarah3.py` or `Notebook/Sarah3.ipynb`, which authenticates via the EUMETSAT API and parses the Metalink file to download files following the pattern `SISmm{YYYYMMDD}{HHMMSS}42310001I1MA.nc`

## Known Issues & Fixes

- **CHIRPS latitude order:** data is stored in descending latitude order; use `slice(16, 3)`, not `slice(3, 16)`.
- **CHIRPS time axis:** float32 precision loss causes all time values to read as `0.0`; dates must be reconstructed manually from step position (step 0 = January 1981).
- **CHIRPS reading on Windows:** large files can raise `RuntimeError: NetCDF: HDF error` with `netCDF4` due to HDF5 file locking; use `h5py` instead.
- **Jupyter compatibility:** scripts avoid `__file__` (use `Path.cwd()`) and `argparse` (causes `SystemExit` in Jupyter kernels). Load scripts in a notebook with:
  ```python
  exec(open("script_name.py", encoding="utf-8").read())
  ```

## Author

**TOURE Seydou**
PhD Candidate — Climate Variability and Fossil Fuel Energy Intensity in WAC Gold Mining

## License

For academic and research use. Please cite appropriately if reused.
