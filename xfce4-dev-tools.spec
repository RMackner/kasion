%global __brp_check_rpaths %{nil}

Name:           xfce4-dev-tools
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
   /usr/lib/debug/usr/local/bin/xdt-csource-4.17.0-1.fc3*
   /usr/local/bin/xdt-autogen
   /usr/local/bin/xdt-csource
   /usr/local/bin/xfce-build
   /usr/local/bin/xfce-do-release
   /usr/local/bin/xfce-get-release-notes
   /usr/local/bin/xfce-get-translations
   /usr/local/bin/xfce-update-news
   /usr/local/share/aclocal/xdt-depends.m4
   /usr/local/share/aclocal/xdt-features.m4
   /usr/local/share/aclocal/xdt-i18n.m4
   /usr/local/share/aclocal/xdt-version.m4
   /usr/local/share/man/man1/xdt-csource.1

%changelog
%autochangelog
