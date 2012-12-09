Name: x11-driver-video-i740
Version: 1.3.4
Release: 2
Summary: X.org driver for Intel i740
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-i740-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-i740 is the X.org driver for Intel i740.

%prep
%setup -qn xf86-video-i740-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/i740_drv.so
%{_mandir}/man4/i740.*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.3.4-1
+ Revision: 810710
- version update 1.3.4

* Tue May 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.3.3-1
+ Revision: 798908
- version update 1.3.3

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.3.2-8
+ Revision: 787230
- Rebuild for x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.3.2-7
+ Revision: 748363
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2-6
+ Revision: 703643
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.3.2-5
+ Revision: 683576
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-4
+ Revision: 671151
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.2-3mdv2011.0
+ Revision: 595742
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.2-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 1.3.2-1mdv2010.0
+ Revision: 407726
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.1-1mdv2010.0
+ Revision: 391866
- update to version 1.3.1

* Mon Mar 23 2009 Thierry Vignaud <tv@mandriva.org> 1.3.0-3mdv2009.1
+ Revision: 360628
- new release

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.0-3mdv2009.1
+ Revision: 308217
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 265922
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194196
- Update to version 1.2.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-7mdv2008.1
+ Revision: 165565
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-6mdv2008.1
+ Revision: 156607
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-5mdv2008.1
+ Revision: 154857
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-i740-1.1.0@mandriva suggested on upstream
  Tag at git checkout 5241aee2f633bab3c22b44d6b5f907973924fcd8
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-4mdv2008.1
+ Revision: 98694
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3mdv2008.0
+ Revision: 75760
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

