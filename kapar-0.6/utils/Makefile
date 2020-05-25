# utils/Makefile.  Generated from Makefile.in by configure.
# $Id: Makefile.in,v 1.7 2015/09/16 19:51:30 kkeys Exp $

CC=gcc
CXX=g++
CFLAGS = -g -Wall -pipe  -I/home/fuyao/scamper-cvs-20191102b @CORALREEF_CPPFLAGS@
CXXFLAGS = -g -Wall -pipe -g -O2 --std=c++11 -I/home/fuyao/scamper-cvs-20191102b @CORALREEF_CPPFLAGS@ -pthread
LDFLAGS = 
LIBS = -lz  

# .if defined(WITH_TRACELB)
# CFLAGS+=	-DWITH_TRACELB
# .endif


CORALREEF_FILES=addr_period link_period tab_addrs tab_links
SCAMPER_CORALREEF_FILES=list_addrs
ALSO_YES_DEV=iff-analyze iff-chain $(@CORALREEF@_FILES) $(SCAMPER_@CORALREEF@_FILES)

all:	sets-to-pairs $(ALSO_NO_DEV)

sets-to-pairs:	sets-to-pairs.cc ../lib/ip4addr.h ../lib/infile.h ../lib/infile.o
		$(CXX) $(CXXFLAGS) -o $@ $@.cc ../lib/infile.o $(LIBS)

iff-chain:	iff-chain.cc ../lib/unordered_set.h
		$(CXX) $(CXXFLAGS) -o $@ $@.cc

iff-analyze:	iff-analyze.cc ../lib/unordered_set.h
		$(CXX) $(CXXFLAGS) -o $@ $@.cc

link_period:	link_period.o
		$(CC) -o $@ $@.o \
			@CORALREEF_LDFLAGS@ -lhashtab -lm

addr_period:	addr_period.o
		$(CC) -o $@ $@.o \
			@CORALREEF_LDFLAGS@ -lhashtab -lm

tab_links:	tab_links.o
		$(CC) -o $@ $@.o \
			@CORALREEF_LDFLAGS@ -lhashtab

tab_addrs:	tab_addrs.o
		$(CC) -o $@ $@.o \
			@CORALREEF_LDFLAGS@ -lhashtab

list_addrs:	list_addrs.o ipset.o
		$(CC) -o $@ $@.o ipset.o \
			-L/home/fuyao/scamper-cvs-20191102b -lscamperfile \
			@CORALREEF_LDFLAGS@ -lhashtab

count_addrs_links:	count_addrs_links.o ipset.o
		$(CC) -o $@ $@.o ipset.o \
			-L/home/fuyao/scamper-cvs-20191102b -lscamperfile

clean:
		rm -f *.o *.core
