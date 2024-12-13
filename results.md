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
