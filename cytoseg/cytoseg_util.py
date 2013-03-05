#This software is Copyright 2012 The Regents of the University of California. All Rights Reserved.
#Permission to use, copy, modify, and distribute this software and its documentation for educational, research and non-profit purposes for non-profit institutions, without fee, and without a written agreement is hereby granted, provided that the above copyright notice, this paragraph and the following three paragraphs appear in all copies.
#Permission to make commercial use of this software may be obtained by contacting:
#Technology Transfer Office
#9500 Gilman Drive, Mail Code 0910
#University of California
#La Jolla, CA 92093-0910
#(858) 534-5815
#invent@ucsd.edu
#This software program and documentation are copyrighted by The Regents of the University of California. The software program and documentation are supplied "as is", without any accompanying services from The Regents. The Regents does not warrant that the operation of the program will be uninterrupted or error-free. The end-user understands that the program was developed for research purposes and is advised not to rely exclusively on the program for any reason.
#IN NO EVENT SHALL THE UNIVERSITY OF CALIFORNIA BE LIABLE TO
#ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR
#CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING
#OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION,
#EVEN IF THE UNIVERSITY OF CALIFORNIA HAS BEEN ADVISED OF
#THE POSSIBILITY OF SUCH DAMAGE. THE UNIVERSITY OF
#CALIFORNIA SPECIFICALLY DISCLAIMS ANY WARRANTIES,
#INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#THE SOFTWARE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND THE UNIVERSITY OF CALIFORNIA HAS NO OBLIGATIONS TO
#PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR
#MODIFICATIONS.

# Utility functions


from ctypes import *
from ctypes.wintypes import *

def subtractDictionary(d1, d2):
    """Subtract dictionary, subtracts each element from corresponding element"""

    result = odict()
    for key in d1.keys():
        result[key] = d1[key] - d2[key]
    return result


def flatten(inputList):
    """Flatten tree"""
    
    resultList = []
    flattenHelper(inputList, resultList)
    return resultList


def flattenHelper(object, resultList):

    if isinstance(object, list):
        for o in object:
            flattenHelper(o, resultList)
    else:
        resultList.append(object)

#print "test"
#def test1():
#    print "test1"


#http://bytes.com/forum/thread20586.html
class MEMORYSTATUS(Structure):
    _fields_ = [
                ('dwLength', DWORD),
                ('dwMemoryLoad', DWORD),
                ('dwTotalPhys', DWORD),
                ('dwAvailPhys', DWORD),
                ('dwTotalPageFile', DWORD),
                ('dwAvailPageFile', DWORD),
                ('dwTotalVirtual', DWORD),
                ('dwAvailVirtual', DWORD),
                ]

def winmem():
    """Output memory status"""
    x = MEMORYSTATUS()
    windll.kernel32.GlobalMemoryStatus(byref(x))
    return x
