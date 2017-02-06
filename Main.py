#!path/to/interpretter
import sys
import zipfile

def unzip(zipfile_path, tofolder_path):
    zip_ref = zipfile.ZipFile(zipfile_path, 'r')
    zip_ref.extractall(tofolder_path)
    zip_ref.close()

def main():
    if len(sys.argv) != 3:
        raise Exception('Must be 3 arguments')
    else:
        zipfile_path, tofolder_path = sys.argv[1:]
        unzip(zipfile_path, tofolder_path)

if __name__ == '__main__':
    main()