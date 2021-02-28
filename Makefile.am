## Process this file with automake to produce Makefile.in

SUBDIRS = efax

release: dist
	mv @PACKAGE@-@VERSION@.tar.gz @PACKAGE@-@VERSION@.src.tgz 

snapshot: dist
	mv @PACKAGE@-@VERSION@.tar.gz @PACKAGE@2-`date +%y%m%d`.src.tgz 

EXTRA_DIST = 
