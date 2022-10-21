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
   /usr/lib/debug/usr/local/lib/libxfce4util.so.7.0.0-4.17.2-1.fc3*
   /usr/lib/debug/usr/local/sbin/xfce4-kiosk-query-4.17.2-1.fc3*
   /usr/local/include/xfce4/libxfce4util/libxfce4util-config.h
   /usr/local/include/xfce4/libxfce4util/libxfce4util.h
   /usr/local/include/xfce4/libxfce4util/xfce-debug.h
   /usr/local/include/xfce4/libxfce4util/xfce-fileutils.h
   /usr/local/include/xfce4/libxfce4util/xfce-generics.h
   /usr/local/include/xfce4/libxfce4util/xfce-gio-extensions.h
   /usr/local/include/xfce4/libxfce4util/xfce-i18n.h
   /usr/local/include/xfce4/libxfce4util/xfce-kiosk.h
   /usr/local/include/xfce4/libxfce4util/xfce-license.h
   /usr/local/include/xfce4/libxfce4util/xfce-miscutils.h
   /usr/local/include/xfce4/libxfce4util/xfce-posix-signal-handler.h
   /usr/local/include/xfce4/libxfce4util/xfce-rc.h
   /usr/local/include/xfce4/libxfce4util/xfce-resource.h
   /usr/local/include/xfce4/libxfce4util/xfce-string.h
   /usr/local/include/xfce4/libxfce4util/xfce-utf8.h
   /usr/local/lib/libxfce4util.so
   /usr/local/lib/libxfce4util.so.7
   /usr/local/lib/libxfce4util.so.7.0.0
   /usr/local/lib/pkgconfig/libxfce4util-1.0.pc
   /usr/local/sbin/xfce4-kiosk-query
   /usr/local/share/locale/am/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ar/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ast/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/be/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/bg/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/bn/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ca/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/cs/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/cy/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/da/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/de/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/el/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/en_AU/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/en_GB/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/es/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/et/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/eu/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/fi/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/fr/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/gl/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/he/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/hi/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/hr/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/hu/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/hy/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/hy_AM/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/hye/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/id/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ie/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/is/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/it/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ja/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/kk/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ko/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/lt/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/lv/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ms/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/nb/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/nl/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/nn/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/oc/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/pa/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/pl/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/pt/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/pt_BR/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ro/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ru/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/si/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/sk/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/sl/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/sq/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/sr/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/sv/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/th/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/tr/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ug/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/uk/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ur/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/ur_PK/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/uz/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/zh_CN/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/zh_HK/LC_MESSAGES/libxfce4util.mo
   /usr/local/share/locale/zh_TW/LC_MESSAGES/libxfce4util.mo

%changelog
%autochangelog
