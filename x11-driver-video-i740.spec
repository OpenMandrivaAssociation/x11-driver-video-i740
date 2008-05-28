Name: x11-driver-video-i740
Version: 1.2.0
Release: %mkrel 1
Summary: X.org driver for Intel i740
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-i740-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Intel i740.

%prep
%setup -q -n xf86-video-i740-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/i740_drv.la
%{_libdir}/xorg/modules/drivers/i740_drv.so
%{_mandir}/man4/i740.*
