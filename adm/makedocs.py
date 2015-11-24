#! /usr/bin/env python
#
# runsvm.py
# 
#    Runs the Sedona VM in current directory with supplied options (or defaults).
#
# Author:    Elizabeth McKenney
# Creation:  27 Oct 2011
#                 

import sys
import os
import subprocess
import optparse 
import shutil
import fileutil
import env


#
# initParser
#   Initializes the options parser
#
def initParser():
  global parser

  parser = optparse.OptionParser(add_help_option=False, usage="""
  makedocs [opts] 
""")

  parser.add_option("-h", "--help", action="help", 
                    help="Show this help message and exit")


#
# usage
#  Print usage (e.g. on error condition)
#
def usage():
  global parser

  # Just print the help generated by the parser for --help
  print ""
  parser.parse_args( ["--help"] )  



#
# Main
#
def main():
  global parser, options

  (options, args) = parser.parse_args()

  buildsrcdocs = env.sedonacExe + " -doc -outDir " + env.build + " " + env.kits
  docOut = os.path.join(env.build, "doc")
  fileutil.cpdir(env.doc, docOut)
  buildpubdocs = env.sedonacExe + " -doc " + os.path.join(docOut, "toc.xml")

  #print "\n\n   Executing cmd = { " + cmd + " }\n\n"
  
  if subprocess.call(buildsrcdocs, shell=True):
    raise Exception, "\n *** Failed:\n" + buildsrcdocs

  if subprocess.call(buildpubdocs, shell=True):
    raise Exception, "\n *** Failed:\n" + buildpubdocs


# 
# Main 
#
if __name__ == '__main__':

  # Initialize the options parser
  initParser()

  # Call the main function
  main()
