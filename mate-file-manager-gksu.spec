%define major		1
%define girmajor	2.0
%define libname	%mklibname caja-extension %{major}
%define girname %mklibname caja-gir %{girmajor}
%define devname	%mklibname -d caja-extension

Summary:	Gksu addon for caja
Name:		mate-file-manager-gksu
Version:	1.2.0
Release:	1
Group:		File tools
License:	GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz
Patch0:		mate-file-manager-gksu-1.2.0_glib.patch

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(libgksu2)

%description
Gksu addon for caja.

%package -n %{libname}
Summary:	Libraries for Mate File manager
Group:		System/Libraries

%description -n %{libname}
This package contains library used by %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for developing mate-file-manager components
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n %{devname}
This package provides the necessary development libraries and include 
files to allow you to develop mate-file-manager components.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std


%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%{_libdir}/caja/extensions-2.0/libcaja-gksu.so
