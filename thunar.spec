%global _hardened_build 1
	
%global xfceversion 4.17


%define githash 274f43f939462d5d1991627214a6275b501b57a5

%define shorthash %(c=%{githash}; echo ${c:0:10})

%define version2 4.17.10
	
 
	
Name:           Thunar
	
Version:        4.17.10.git.%{shorthash}
	
Release:        %autorelease
	
Summary:        Thunar File Manager
	
 
	
License:        GPLv2+
	
URL:            http://thunar.xfce.org/
	
#VCS git:git://git.xfce.org/xfce/thunar
	
Source0:        https://gitlab.xfce.org/xfce/thunar/-/archive/%{githash}/thunar-%{githash}.tar.gz
	
 
	
BuildRequires:  make
	
BuildRequires:  gcc-c++
	
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.34
	
BuildRequires:  pkgconfig(exo-2) >= %{xfceversion}
	
BuildRequires:  pkgconfig(gudev-1.0) >= 145
	
BuildRequires:  pkgconfig(libexif) >= 0.6.0
	
BuildRequires:  pkgconfig(libpcre) >= 6.0
	
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.4
	
BuildRequires:  pkgconfig(libnotify) >= 0.4.0
	
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
	
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfceversion}

BuildRequires:  xfce4-dev-tools
	
BuildRequires:  libSM-devel
	
BuildRequires:  freetype-devel
	
BuildRequires:  libpng-devel >= 2:1.2.2-16
	
BuildRequires:  libICE-devel
	
BuildRequires:  pkgconfig
	
BuildRequires:  intltool gettext
	
BuildRequires:  desktop-file-utils >= 0.7
	
BuildRequires:  libappstream-glib
	
BuildRequires:  gobject-introspection-devel

BuildRequires:  gtk-doc
	
Requires:       shared-mime-info
	
Requires:       dbus
	
Requires:       gvfs
	
 
	
Obsoletes:     thunar-vcs-plugin <= 0.2.0-24
	

	
%description
	
Thunar is a new modern file manager for the Xfce Desktop Environment. It has 
	
been designed from the ground up to be fast and easy-to-use. Its user interface 
	
is clean and intuitive, and does not include any confusing or useless options. 
	
Thunar is fast and responsive with a good start up time and directory load time.
	
 
	
%package devel
	
Summary: Development tools for Thunar file manager
	
Requires: %{name} = %{version2}-%{release}
	
Requires: pkgconfig
	
Requires: exo-devel
	
 
	
%description devel
	
libraries and header files for the Thunar file manager.
	
 
	
%package docs
	
Summary: GTK docs for Thunar file manager
	
Requires: %{name} = %{version2}-%{release}
	
 
	
%description docs
	
Thunarx GTK documentation files for the Thunar file manager.
	
 
	
%prep
	
%autosetup -n thunar-%{githash}
	

	
%build
	
./autogen.sh
	
# Remove rpaths
	
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
	
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
	
export LD_LIBRARY_PATH="`pwd`/thunarx/.libs"
	
%make_build
	
	
 
	
%install
	
%make_install
 
	
make -C examples distclean
	
 
	
# 2 of the example files need to not be executable 
	
# so they don't pull in dependencies. 
	
chmod 644 examples/thunar-file-manager.py
	
chmod 644 examples/xfce-file-manager.py
	
 
	
find %{buildroot} -name '*.la' -exec rm -f {} ';'
 
	
 
	
%pre
	
for target in %{_defaultdocdir}/Thunar/html/*/images
	
do
	
       if [ -d $target ]
	
       then
	
               rm -rf $target
	
       fi
	
done
	
 
	
%ldconfig_scriptlets
	
	
%files
	
   /usr/lib/debug/usr/local/bin/thunar*
   /usr/lib/debug/usr/local/lib/Thunar/*
   /usr/lib/debug/usr/local/lib/libthunarx*
   /usr/lib/debug/usr/local/lib/thunarx-3/*
   /usr/lib/debug/usr/local/lib/xfce4/panel/plugins/*
   /usr/local/bin/Thunar
   /usr/local/bin/thunar
   /usr/local/bin/thunar-settings
   /usr/local/etc/xdg/Thunar/uca.xml
   /usr/local/lib/Thunar/*
   /usr/local/lib/girepository-1.0/*
   /usr/local/lib/libthunarx-3.*
   /usr/local/lib/systemd/user/thunar.service
   /usr/local/lib/thunarx-3/*
   /usr/local/lib/xfce4/panel/plugins/libthunar-tpa.so
   /usr/local/share/Thunar/sendto/thunar-sendto-email.desktop
   /usr/local/share/applications/thunar*
   /usr/local/share/dbus-1/services/org.xfce.*
   /usr/local/share/doc/thunar/README.gtkrc
   /usr/local/share/icons/hicolor/*
   /usr/local/share/locale/*
   /usr/local/share/man/man1/Thunar.1
   /usr/local/share/metainfo/org.xfce.thunar.appdata.xml
   /usr/local/share/polkit-1/actions/org.xfce.thunar.policy
   /usr/local/share/xfce4/panel/plugins/thunar-tpa.desktop
	
 
	
%files devel
	
%{_includedir}/thunarx-3/thunarx/*
	
%{_libdir}/libthunarx-*
	
%{_libdir}/pkgconfig/thunarx-3.pc
	
%{_datadir}/gir-1.0/Thunarx-3.0.gir
	
	
	
 
	
%changelog
	
%autochangelog
