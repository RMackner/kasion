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
   /usr/bin/xfce4-kiosk-query
   /usr/include/xfce4/libxfce4util/libxfce4util-config.h
   /usr/include/xfce4/libxfce4util/libxfce4util.h
   /usr/include/xfce4/libxfce4util/xfce-debug.h
   /usr/include/xfce4/libxfce4util/xfce-fileutils.h
   /usr/include/xfce4/libxfce4util/xfce-generics.h
   /usr/include/xfce4/libxfce4util/xfce-gio-extensions.h
   /usr/include/xfce4/libxfce4util/xfce-i18n.h
   /usr/include/xfce4/libxfce4util/xfce-kiosk.h
   /usr/include/xfce4/libxfce4util/xfce-license.h
   /usr/include/xfce4/libxfce4util/xfce-miscutils.h
   /usr/include/xfce4/libxfce4util/xfce-posix-signal-handler.h
   /usr/include/xfce4/libxfce4util/xfce-rc.h
   /usr/include/xfce4/libxfce4util/xfce-resource.h
   /usr/include/xfce4/libxfce4util/xfce-string.h
   /usr/include/xfce4/libxfce4util/xfce-utf8.h
   /usr/lib/debug/usr/bin/xfce4-kiosk-query-4.17.2-1.fc3*
   /usr/lib/debug/usr/lib/libxfce4util.so.7.0.0-4.17.2-1.fc3*
   /usr/lib/libxfce4util.so
   /usr/lib/libxfce4util.so.7
   /usr/lib/libxfce4util.so.7.0.0
   /usr/lib/pkgconfig/libxfce4util-1.0.pc
   /usr/share/gtk-doc/html/libxfce4util/annotation-glossary.html
   /usr/share/gtk-doc/html/libxfce4util/home.png
   /usr/share/gtk-doc/html/libxfce4util/index.html
   /usr/share/gtk-doc/html/libxfce4util/left-insensitive.png
   /usr/share/gtk-doc/html/libxfce4util/left.png
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-File-Utilities.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-GIO-Extensions.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-Internationalisation.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-Miscellaneous-Utilities.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-POSIX-Signal-Handling.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-Resource-Config-File-Support.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-Resource-lookup-functions.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-Software-Licenses.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-Unicode-Support-Functions.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-Version-Information.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-Xfce-Generics.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-Xfce-Kiosk-functions.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-Xfce-String-Functions.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-core.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-datatypes.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-fundamentals.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util-utilities.html
   /usr/share/gtk-doc/html/libxfce4util/libxfce4util.devhelp2
   /usr/share/gtk-doc/html/libxfce4util/reference.html
   /usr/share/gtk-doc/html/libxfce4util/right-insensitive.png
   /usr/share/gtk-doc/html/libxfce4util/right.png
   /usr/share/gtk-doc/html/libxfce4util/style.css
   /usr/share/gtk-doc/html/libxfce4util/up-insensitive.png
   /usr/share/gtk-doc/html/libxfce4util/up.png
   /usr/share/locale/am/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ar/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ast/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/be/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/bg/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/bn/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ca/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/cs/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/cy/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/da/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/de/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/el/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/en_AU/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/en_GB/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/es/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/et/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/eu/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/fi/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/fr/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/gl/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/he/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/hi/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/hr/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/hu/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/hy/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/hy_AM/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/hye/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/id/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ie/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/is/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/it/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ja/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/kk/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ko/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/lt/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/lv/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ms/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/nb/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/nl/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/nn/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/oc/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/pa/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/pl/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/pt/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/pt_BR/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ro/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ru/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/si/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/sk/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/sl/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/sq/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/sr/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/sv/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/th/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/tr/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ug/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/uk/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ur/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/ur_PK/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/uz/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/zh_CN/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/zh_HK/LC_MESSAGES/libxfce4util.mo
   /usr/share/locale/zh_TW/LC_MESSAGES/libxfce4util.mo

%changelog
%autochangelog
