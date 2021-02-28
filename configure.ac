dnl Process this file with autoconf to produce a configure script.
AC_INIT([efax], [0.9a])

AM_INIT_AUTOMAKE(AC_PACKAGE_NAME,AC_PACKAGE_VERSION)

AM_CONFIG_HEADER(config.h)

dnl check for working c and c++ compilers
AC_CHECK_COMPILERS
dnl Checks for programs.
AC_PROG_INSTALL

dnl Checks for libraries.
PKG_CHECK_MODULES(GLIB, glib-2.0 >= 2.0.0)

dnl Checks for typedefs, structures, and compiler characteristics.
AC_TYPE_SIZE_T
AC_CHECK_TYPES(ssize_t)

dnl GNU Gettext
AM_GNU_GETTEXT([external])
AM_GNU_GETTEXT_VERSION([0.14.1])


dnl now check out the install directory
AC_INSTALL_DIRS

dnl enable source in subdirectories to be compiled
AC_PROG_RANLIB

dnl define MAKE for subdirectories
AC_PROG_MAKE_SET

AC_CONFIG_FILES([ Makefile efax/Makefile ])
AC_OUTPUT

AC_CLOSING_MESSAGE
