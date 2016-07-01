#!/usr/bin/python

import os, sys

# Open a file
#path = "/media/ramesh/Namrata Bilurkar/Movies/2015_Oscars"
#path = "/media/ramesh/Namrata Bilurkar/Movies/BluRay Movies"
#path = "/media/ramesh/Namrata Bilurkar/Movies/Hindi"
#path = "/media/ramesh/Namrata Bilurkar/Movies/Others"
#path = "/media/ramesh/Namrata Bilurkar/Movies/English"
#path = "/media/ramesh/Namrata Bilurkar/Movies/Animated"
#path = "/media/ramesh/Namrata Bilurkar/Movies/Kannada"
path = "/media/ramesh/Namrata Bilurkar/Movies/Other languages"


dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print file

