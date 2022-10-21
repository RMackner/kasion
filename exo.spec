Name:           exo
Version:        4.17.2
Release:        %autorelease
Summary:        exo
License:        GPL-2.0
URL:            https://archive.xfce.org/src/xfce
Source0:        %{url}/%{name}/4.17/%{name}-%{version}.tar.bz2
Conflicts:      exo


BuildRequires:  make
BuildRequires:  gtk3-devel
BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  glib-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  xfce4-dev-tools
BuildRequires:  libxfce4util-devel

%description
%{summary}

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
