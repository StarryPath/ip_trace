## 
## Copyright (C) 2011-2018 The Regents of the University of California.
## 
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
## 

# lib/Makefile.  Generated from Makefile.in by configure.
# $Id: Makefile.in,v 1.4 2012/01/03 20:49:25 kkeys Exp $

CXX=g++
CPPFLAGS =  -I/home/fuyao/scamper-cvs-20191102b
CXXFLAGS = -g -O2 --std=c++11 -I/home/fuyao/scamper-cvs-20191102b
# LDFLAGS = 
# LIBS = -lz 

all: infile.o PathLoader.o MemoryInfo.o

clean:
	rm -f *.o *.core

.cc.o:
	$(CXX) -c $(CPPFLAGS) $(CXXFLAGS) -o $@ $*.cc

infile.o: infile.cc infile.h

PathLoader.o: PathLoader.cc PathLoader.h ScamperInput.h

MemoryInfo.o: MemoryInfo.cc MemoryInfo.h
