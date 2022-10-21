%global __brp_check_rpaths %{nil}

Name:           libxfce4util
Version:        4.17.2
Release:        %autorelease
Summary:        libxfce4util
License:        GPL-2.0
URL:            https://archive.xfce.org/src/xfce
Source0:        https://github.com/RMackner/kasion/releases/download/4.17.2/4.17.2.tar.gz
Conflicts:      libxfce4util

Requires: gtk3

BuildRequires:  make
BuildRequires:  gtk3-devel
BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  glib-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  xfce4-dev-tools
BuildRequires:  libtool

%description
This package includes basic utility non-GUI functions for Xfce4.

%package devel
Summary: Developpment tools for libxfce4util library
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel
Requires: gtk2-devel
Requires: pkgconfig

%description devel
This package includes static libraries and header files for the
libxfce4util library.

%prep
%setup

%build
./autogen.sh
%make_build

%install
%make_install

%files


%changelog
%autochangelog
