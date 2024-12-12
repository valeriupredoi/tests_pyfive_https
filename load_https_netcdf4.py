import os
import pyfive
import fsspec
import netCDF4
import time
import s3fs

from netCDF4 import Dataset


url4 = "https://esgf.ceda.ac.uk/thredds/fileServer/esg_cmip6/CMIP6/AerChemMIP/MOHC/UKESM1-0-LL/ssp370SST-lowNTCF/r1i1p1f2/Amon/cl/gn/latest/cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc"
url4nc = "https://esgf.ceda.ac.uk/thredds/fileServer/esg_cmip6/CMIP6/AerChemMIP/MOHC/UKESM1-0-LL/ssp370SST-lowNTCF/r1i1p1f2/Amon/cl/gn/latest/cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc#mode=bytes"
url4s3 = "ch330a.pc19790301-bnl.nc"  # 18GB 3400 HDF5 chunks

def load_file_pyfive(uri):
    fs = fsspec.filesystem('http')
    t1=time.time()
    http_file = fs.open(uri, 'rb')
    t2=time.time()
    ds = pyfive.File(http_file)
    print(f"Dataset loaded from HTTP with Pyfive: {uri}")
    sl = ds["cl"][0:100]
    t3=time.time()
    print(f"HTTPSPyfive took {t3-t1:.2}s")


def load_file_netCDF4(uri):
    with Dataset(uri, diskless=True, persist=True) as nc:
        print(f"Dataset loaded from HTTP with netCDF4: {url4nc}")
        var = nc["cl"][0:100]


def load_file_s3(uri):
    storage_options = {
        'key': "f2d55c6dcfc7618b2c34e00b58df3cef",
        'secret': "$/'#M{0{/4rVhp%n^(XeX$q@y#&(NM3W1->~N.Q6VP.5[@bLpi='nt]AfH)>78pT",
        # 'client_kwargs': {'endpoint_url': "https://uor-aces-o.s3-ext.jc.rl.ac.uk"},  # old proxy
        'client_kwargs': {'endpoint_url': "https://uor-aces-o.ext.proxy.jc.rl.ac.uk"},  # new proxy
    }
    fs = s3fs.S3FileSystem(**storage_options)  # use passed-in dictionary

    test_file_uri = os.path.join(
        "bnl",  # bucket
        uri     # actual file uri
    )
    print("S3 Test file path:", test_file_uri)

    t1=time.time()
    s3file = fs.open(test_file_uri, 'rb')
    t2=time.time()
    ds = pyfive.File(s3file)
    t3=time.time()
    print(f"Dataset loaded from S3 with s3fs and Pyfive: {uri} ({t2-t1:.2},{t3-t2:.2})")
    sl = ds['UM_m01s16i202_vn1106'][0:100]


load_file_pyfive(url4)
print("\n")
tx = time.time()
load_file_netCDF4(url4nc)
ty = time.time()
print(f"netCDF4 took {ty-tx:.2}s")
print("\n")
tm = time.time()
load_file_s3(url4s3)
print(f"S3Pyfive took {time.time()-tm:.2}s")
