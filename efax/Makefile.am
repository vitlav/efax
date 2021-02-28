## Process this file with automake to produce Makefile.in

SUBDIRS=

bin_PROGRAMS = efax efix

efax_SOURCES = efax.c efaxlib.c efaxio.c efaxos.c efaxmsg.c
                
efix_SOURCES = efix.c efaxlib.c efaxmsg.c

noinst_HEADERS = efaxlib.h efaxio.h efaxos.h efaxmsg.h

dist_man_MANS = efax.1 efix.1

INCLUDES = -DDATADIR=\"$(datadir)\"

AM_CFLAGS = @GLIB_CFLAGS@

efax_LDADD = @GLIB_LIBS@

efix_LDADD = @GLIB_LIBS@

EXTRA_DIST = PATCHES fax
