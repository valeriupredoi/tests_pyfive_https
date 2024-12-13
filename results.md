## Test Set 1

- file: `cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc`
- file dimensions:
```
dimensions:
	time = UNLIMITED ; // (600 currently)
	bnds = 2 ;
	lev = 85 ;
	lat = 144 ;
	lon = 192 ;
```
- getrange: `ds["cl"][0:100]`

### V Laptop

| Run Id | HTTP-Pyfive | HTTP-NetCDF4 | S3-Pyfive | LOCAL-NetCDF4 |
|-|-|-|-|-|
| 1 | 54 | 35 | 68 | 21 |
| 2 | 31 | 32 | 69 | 13 |
| 3 | 31 | 37 | 56 | 15 |

`systemctl suspend` (wipe interpreter and OS cache - actually, I checked, this doesn't clear **any** cache, neither kernel nor RAM, so a bit futile)

| Run Id | HTTP-Pyfive | HTTP-NetCDF4 | S3-Pyfive | LOCAL-NetCDF4 |
|-|-|-|-|-|
| 1 | 34 | 40 | 59 | 12 |
| 2 | 31 | 34 | 58 | 13 |
| 3 | 36 | 33 | 66 | 12 |

### JASMIN (sci-vm-02)

- note: `LOCAL` here is BADC: `/badc/cmip6/data/CMIP6/AerChemMIP/MOHC/UKESM1-0-LL/ssp370SST-lowNTCF/r1i1p1f2/Amon/cl/gn/latest/cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc`
- note2: environment perfectly mirrored via lockfile `environ.yml` + pip installs (`pyfive/https_compat` GH branch)

| Run Id | HTTP-Pyfive | HTTP-NetCDF4 | S3-Pyfive | LOCAL-NetCDF4 |
|-|-|-|-|-|
| 1 | 23 | 24 | 59 | 13 |
| 2 | 21 | 26 | 47 | 12 |
| 3 | 24 | 26 | 47 | 11 |
| 4 | 23 | 23 | 45 | 10 |
