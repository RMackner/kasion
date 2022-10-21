%global __brp_check_rpaths %{nil}

Name:           libxfce4util
Version:        4.17.0
Release:        %autorelease
Summary:        xfce4-dev-tools
License:        GPL-2.0
URL:            https://archive.xfce.org/src/xfce
Source0:        https://archive.xfce.org/src/xfce/xfce4-dev-tools/4.17/xfce4-dev-tools-4.17.0.tar.bz2
Conflicts:      xfce4-dev-tools

BuildRequires:  make
BuildRequires:  gtk3-devel
BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  glib-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  libtool

%description
This package includes basic utility non-GUI functions for Xfce4.


%prep
%setup

%build
./configure
%make_build

%install
%make_install

%files


%changelog
%autochangelog
