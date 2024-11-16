"""
                NAME : KODINGNEXT
                DATE : 2024-11-16
                PROJECT : Zip program

"""
# Make simple zipper software, or zip compressor

from shutil import  make_archive
import  random
# File name is randomize from 100 to 200
zip_filename = random.randrange(100,200)

folder_to_zip = input(" Where you want to save the zip file ?: ") # Copy folder directory to save zip file
make_archive(f"{zip_filename}","zip",folder_to_zip) # this function will create the zip