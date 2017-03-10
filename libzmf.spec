#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	A library for reading and converting Zoner Draw and Zebra file formats
Summary(pl.UTF-8):	Biblioteka do odczytu i importu formatów plików Zoner Draw i Zebra
Name:		libzmf
Version:	0.0.1
Release:	2
License:	MPL v2.0
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/libzmf/%{name}-%{version}.tar.xz
# Source0-md5:	5a002c50af653b67b3c2aedd979a2972
URL:		https://wiki.documentfoundation.org/DLP/Libraries/libzmf
BuildRequires:	boost-devel
BuildRequires:	cppunit-devel
BuildRequires:	doxygen
BuildRequires:	libicu-devel
BuildRequires:	libpng-devel
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	librevenge >= 0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libzmf is a library for reading and converting Zoner Draw and Zebra
file formats.

%description -l pl.UTF-8
Libzmf to biblioteka do odczytu i importu formatów plików Zoner Draw i
Zebra.

%package devel
Summary:	Development files for libzmf
Summary(pl.UTF-8):	Pliki nagłówkowe dla libzmf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel >= 6:4.7

%description devel
This package contains the header files for developing applications
that use libzmf.

%description devel -l pl.UTF-8
Pen pakiet zawiera pliki nagłówkowe do tworzenia aplikacji opartych na
libzmf.

%package static
Summary:	Static libzmf library
Summary(pl.UTF-8):	Statyczna biblioteka libzmf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libzmf library.

%description static -l pl.UTF-8
Statyczna biblioteka libzmf.

%package apidocs
Summary:	libzmf API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libzmf
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for libzmf library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libzmf.

%package tools
Summary:	Tools to transform Zoner Draw drawings into other formats
Summary(pl.UTF-8):	Programy przekształcania rysunków Zoner Draw do innych formatów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform Zoner Draw drawings into other formats. Currently
supported: SVG, raw.

%description tools -l pl.UTF-8
Narzędzia do przekształcania rysunków Zoner Draw do innych formatów.
Aktualnie obsługiwane są SVG i raw.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--disable-werror

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libzmf-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzmf-0.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzmf-0.0.so
%{_includedir}/libzmf-0.0
%{_pkgconfigdir}/libzmf-0.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libzmf-0.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/%{name}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zmf2raw
%attr(755,root,root) %{_bindir}/zmf2svg
