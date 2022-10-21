Name:           thunar
Version:        4.17.10
Release:        %autorelease
Summary:        Nwg-look is a GTK3 settings editor, designed to work properly in wlroots-based Wayland environment.
License:        GPL-2.0
URL:            https://archive.xfce.org/src/xfce
Source0:        %{url}/%{name}/4.17/%{name}-%{version}.tar.bz2
Conflicts:      thunar

Requires: gtk3

BuildRequires:  make
BuildRequires:  gtk3-devel
BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  exo-devel
BuildRequires:  glib-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  xfce4-dev-tools
BuildRequires:  libxfce4ui-devel

%description
%{summary}

%prep
%setup

%build
./configure
make

%install
make install

%files

%changelog
%autochangelog
