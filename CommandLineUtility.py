import argparse
import requests
def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()

# Add Command line Arguments
parser.add_argument("URL", help = "Url of the file to download")
# parser.add_argument("Output", help = "by which name you want to save your file")
parser.add_argument("-o", "--Output", help="Name of the file", default=None)

# parse the arguments
args = parser.parse_args()

# use the arguments in your code
print(args.URL)
print(args.Output)
download_file(args.URL, args.Output)

# python CommandLineUtility.py https://imagej.net/images/AuPbSn40.jpg -o ndh.jpg (to get output we have to wrote this in shell)
#  or
# python CommandLineUtility.py https://imagej.net/images/AuPbSn40.jpg 