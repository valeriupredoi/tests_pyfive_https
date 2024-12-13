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

### V Laptop

| Run Id | HTTP-Pyfive | HTTP-NetCDF4 | S3-Pyfive | LOCAL-NetCDF4 |
|-|-|-|-|-|
| 1 | 54 | 35 | 68 | 21 |
| 2 | 31 | 32 | 69 | 13 |
| 3 | 31 | 37 | 56 | 15 |

`systemctl suspend`
