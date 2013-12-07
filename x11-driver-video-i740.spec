%define _disable_ld_no_undefined 1

Summary:	X.org driver for Intel i740
Name:		x11-driver-video-i740
Version:	1.3.4
Release:	6
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-i740-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-i740 is the X.org driver for Intel i740.

%prep
%setup -qn xf86-video-i740-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/i740_drv.so
%{_mandir}/man4/i740.*

