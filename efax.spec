Name: efax
Version: 0.9a001114
Release: alt1

Summary: A program for faxing using a Class 1, 2 or 2.0 fax modem
Summary(ru_RU.KOI8-R): ��������� ��� �������� � ��ɣ�� ������ ����� ����-�����

License: GPL
Group: Communications
Url: http://www.cce.com/efax/

Source: http://www.cce.com/efax/download/%name-%version.tar.bz2
Source1: %name-%version.config
Patch1: %name-%version.patch

%description
Efax is a small ANSI C/POSIX program that sends and receives faxes using
any Class 1, 2 or 2.0 fax modem.

You need to install efax if you want to send faxes and you have a
Class 1, 2 or 2.0 fax modem.

Please check /etc/efax.rc for your parameters (telephon number and machine id)

%description -l ru_RU.KOI8-R
Efax -- ��� ��������� ���������, ���������� �� ANSI C/POSIX, ������� ���������
��������� � ���������� ����� ����� ����� ����-����� ����� 1, 2 ��� 2.0.

�� �������� ��������� ��������� � /etc/efax.rc (����� �������� � �������� �������)

%prep
%setup -q
%patch1 -p1

%build
%make LDFLAGS="-s"
%__subst "s|logfile=|logfile=\${LOGDIR}/|g" fax

%install
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_mandir/man1
mkdir -p $RPM_BUILD_ROOT/var/spool/fax

make BINDIR=$RPM_BUILD_ROOT%_bindir MANDIR=$RPM_BUILD_ROOT%_mandir install

%__install -D -m644 %SOURCE1 $RPM_BUILD_ROOT%_sysconfdir/%name.rc

%files
%doc README PATCHES
%config(noreplace) %_sysconfdir/%name.rc
%_bindir/fax
%_bindir/%name
%_bindir/efix
%_mandir/man1/*
%attr(775, lp, lp) /var/spool/fax

%changelog
* Wed Jun 16 2004 Vitaly Lipatov <lav@altlinux.ru> 0.9a001114-alt1
- updated version with better support some Linmodems
- patches from efax-gtk project
- spec cleanup
- move config file to original place - /etc/efax.rc
- make good default configuration in efax.rc
- logfiles created in LOGDIR only
 
* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9-ipl10mdk
- Rebuilt in new environment

* Mon May 06 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9-ipl9mdk
- Some spec cleanup
- Fixed requires to make
- Added RH patches
- Removed COPYING GPL License

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE adaptation

* Wed Jul 26 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9-6mdk
- BM + macroszification

* Tue Apr 18 2000 Daouda Lo <daouda@mandrakesoft.com> 0.9-5mdk
- fix group

* Mon Jan 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.9-4mdk
- Compile with egcs on alpha.

* Sun Nov 28 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Redo config patch
- /usr/bin/fax no longer a %%config file, now sources /etc/fax.config
	instead

* Sun Jul 18 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 0.9
- adapt patches
- s/RedHat/Mandrake/ in sender config...

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 11)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Feb 02 1999 Preston Brown <pbrown@redhat.com>
- patch to fix null ptr dereference
- added -ansi flag; fixes efix problem (produced bad tiff files)

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- cleaned spec file to new standard, confirmed package is up to date

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Added efax-08a-64bit.patch from David Mosberger
