%define		snap	bzr754

Summary:	Simplest dock on the planet
Name:		plank
Version:	0.2.0
Release:	1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		X11/Applications
Source0:	%{name}-%{version}-%{snap}.tar.xz
# Source0-md5:	534fcdb203fa4a1ca7ccb6846552298d
BuildRequires:	bamf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	bamf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plank is meant to be the simplest dock on the planet. The goal is to
provide just what a dock needs and absolutely nothing more. It is,
however, a library which can be extended to create other dock programs
with more advanced features.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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

