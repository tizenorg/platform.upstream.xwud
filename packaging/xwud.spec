%bcond_with x

Summary: image displayer for X
Name: xwud
# NOTE: The package version should be set to the X11 major release from which
# the OS release is based upon.
Version: 1.0.4
Release: 1
License: MIT
Group: User Interface/X
URL: http://www.x.org

Source: %{name}-%{version}.tar.gz

#Source3:  ftp://ftp.x.org/pub/individual/app/xwud-1.0.3.tar.bz2

BuildRequires: autoconf automake

#BuildRequires: xorg-x11-xutils-dev
# xfd needs gettext
BuildRequires: gettext
BuildRequires: zlib-devel
BuildRequires: libfontenc-devel
BuildRequires: libX11-devel
BuildRequires: libXmu-devel
BuildRequires: libXext-devel
BuildRequires: libXt-devel
BuildRequires: libXaw-devel
BuildRequires: libXpm-devel
BuildRequires: libXft-devel
BuildRequires: libXrender-devel
BuildRequires: libxkbfile-devel
BuildRequires: libXcursor-devel
BuildRequires: libpng-devel
BuildRequires: libXfixes-devel
BuildRequires: libXi-devel >= 1.2
BuildRequires: libXxf86vm-devel
BuildRequires: pkgconfig(xbitmaps)

Provides: xwud

# NOTE: xwd, xwud, luit used to be in these.
#Obsoletes: XFree86, xorg-x11
# NOTE: x11perf, xclipboard used to be in these.
#Obsoletes: XFree86-tools, xorg-x11-tools
# Xaw app moves
#Conflicts: xorg-x11-utils < 7.4-5.fc12
#Conflicts: xorg-x11-server-utils < 7.4-8.fc12

%if !%{with x}
ExclusiveArch:
%endif

%description
Xwud  is  an  X Window System image undumping utility.  Xwud allows X users to
display in a window an image saved in a specially formatted dump file, such as
produced by xwd(1).

#%define xwud

%prep
%setup -q

%build
%autogen --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}

{
	make install DESTDIR=$RPM_BUILD_ROOT
}

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
/usr/share/license/%{name}
#%{_bindir}/xwud
