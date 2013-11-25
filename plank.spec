%define		snap	bzr795

Summary:	Simplest dock on the planet
Name:		plank
Version:	0.5.0
Release:	1
License:	GPL v3
Group:		X11/Applications
#Source0:	%{name}-%{version}-%{snap}.tar.xz
Source0:	https://launchpad.net/plank/1.0/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	3996a47d4c7e1c24a58ccb41a1db5678
Patch0:		%{name}-libm.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bamf-devel >= 0.4.1
BuildRequires:	intltool
BuildRequires:	libgee-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel
BuildRequires:	pkg-config
BuildRequires:	vala-vapigen
BuildRequires:	xorg-libX11-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	bamf >= 0.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plank is meant to be the simplest dock on the planet. The goal is to
provide just what a dock needs and absolutely nothing more. It is,
however, a library which can be extended to create other dock programs
with more advanced features.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sma

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/plank
%{_datadir}/plank
%{_desktopdir}/plank.desktop
%{_iconsdir}/hicolor/*/apps/plank.svg
%{_mandir}/man1/plank.1*

