import os
import s3fs

## this shold work if mc cp don't

def upload_to_s3(server, username, password, bucket, object, rfile):
    """Upload a file to an S3 object store."""
    s3_fs = s3fs.S3FileSystem(key=username, secret=password, client_kwargs={'endpoint_url': server})
    # Make sure s3 bucket exists
    try:
        s3_fs.mkdir(bucket)
    except FileExistsError:
        pass

    print(f"S3 putting file {rfile}")
    s3_fs.put_file(rfile, os.path.join(bucket, object))


S3_BUCKET = "bnl"
# S3_URL = "https://uor-aces-o.ext.proxy.jc.rl.ac.uk"  ## new proxy
# only the OLD proxy (here below) allows for put or mc cp
S3_URL = "https://uor-aces-o.s3-ext.jc.rl.ac.uk" 
S3_ACCESS_KEY = "f2d55c6dcfc7618b2c34e00b58df3cef"
S3_SECRET_KEY = "$/'#M{0{/4rVhp%n^(XeX$q@y#&(NM3W1->~N.Q6VP.5[@bLpi='nt]AfH)>78pT"

file_object = "tos_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc"
rfile = "/home/valeriu/tos_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc"

upload_to_s3(S3_URL, S3_ACCESS_KEY, S3_SECRET_KEY,
             S3_BUCKET, file_object, rfile)
