%global _hardened_build 1
	
%global xfceversion 4.17
	
 
	
Name:           Thunar
	
Version:        4.17.10
	
Release:        %autorelease
	
Summary:        Thunar File Manager
	
 
	
License:        GPLv2+
	
URL:            http://thunar.xfce.org/
	
#VCS git:git://git.xfce.org/xfce/thunar
	
Source0:        https://archive.xfce.org/src/xfce/thunar/%{xfceversion}/thunar-%{version}.tar.bz2
	
 
	
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
	
BuildRequires:  libSM-devel
	
BuildRequires:  freetype-devel
	
BuildRequires:  libpng-devel >= 2:1.2.2-16
	
BuildRequires:  libICE-devel
	
BuildRequires:  pkgconfig
	
BuildRequires:  intltool gettext
	
BuildRequires:  desktop-file-utils >= 0.7
	
BuildRequires:  libappstream-glib
	
BuildRequires:  gobject-introspection-devel
	
Requires:       shared-mime-info
	
Requires:       dbus
	
Requires:       gvfs
	
 
	
Obsoletes:     thunar-vcs-plugin <= 0.2.0-24
	
 
	
# Provide lowercase name to help people find the package. 
	
Provides:       thunar = %{version}-%{release}
	
 
	
%description
	
Thunar is a new modern file manager for the Xfce Desktop Environment. It has 
	
been designed from the ground up to be fast and easy-to-use. Its user interface 
	
is clean and intuitive, and does not include any confusing or useless options. 
	
Thunar is fast and responsive with a good start up time and directory load time.
	
 
	
%package devel
	
Summary: Development tools for Thunar file manager
	
Requires: %{name} = %{version}-%{release}
	
Requires: pkgconfig
	
Requires: exo-devel
	
 
	
%description devel
	
libraries and header files for the Thunar file manager.
	
 
	
%package docs
	
Summary: GTK docs for Thunar file manager
	
Requires: %{name} = %{version}-%{release}
	
 
	
%description docs
	
Thunarx GTK documentation files for the Thunar file manager.
	
 
	
%prep
	
%autosetup -n thunar-%{version}
	
 
	
# fix icon in thunar-sendto-email.desktop
	
sed -i 's!internet-mail!mail-message-new!' \
	
        plugins/thunar-sendto-email/thunar-sendto-email.desktop.in.in
	
 
	
%build
	
%configure --enable-dbus
	
# Remove rpaths
	
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
	
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
	
export LD_LIBRARY_PATH="`pwd`/thunarx/.libs"
	
%make_build
	
	
 
	
%install
	
%make_install
	
	
# fixes wrong library permissions
	
chmod 755 %{buildroot}/%{_libdir}/*.so
	
 
	
make -C examples distclean
	
 
	
# 2 of the example files need to not be executable 
	
# so they don't pull in dependencies. 
	
chmod 644 examples/thunar-file-manager.py
	
chmod 644 examples/xfce-file-manager.py
	
 
	
find %{buildroot} -name '*.la' -exec rm -f {} ';'
	
 
	
%find_lang thunar
	
 
	
desktop-file-install --delete-original          \
	
        --dir %{buildroot}/%{_datadir}/applications         \
	
        %{buildroot}/%{_datadir}/applications/thunar-settings.desktop
	
 
	
desktop-file-install --delete-original          \
	
        --dir %{buildroot}/%{_datadir}/applications          \
	
        %{buildroot}/%{_datadir}/applications/thunar-bulk-rename.desktop
	
 
	
desktop-file-install --delete-original          \
	
        --dir %{buildroot}/%{_datadir}/applications         \
	
        %{buildroot}/%{_datadir}/applications/thunar.desktop
	
 
	
# appdata
	
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
	
 
	
 
	
%pre
	
for target in %{_defaultdocdir}/Thunar/html/*/images
	
do
	
       if [ -d $target ]
	
       then
	
               rm -rf $target
	
       fi
	
done
	
 
	
%ldconfig_scriptlets
	
	
%files -f thunar.lang
	
%license COPYING
	
%doc ChangeLog NEWS INSTALL AUTHORS HACKING THANKS
	
%doc docs/README.gtkrc
	
# exclude docs that we have moved to the above
	
%exclude %{_datadir}/doc/thunar/README.gtkrc
	
%{_bindir}/Thunar
	
%{_bindir}/thunar
	
%{_bindir}/thunar-settings
	
%{_libdir}/libthunar*.so.*
	
%dir %{_libdir}/thunarx-*/
	
%{_libdir}/thunarx-*/thunar*.so
	
%dir %{_libdir}/Thunar/
	
%{_libdir}/Thunar/thunar-sendto-email
	
%dir %{_datadir}/Thunar/
	
%dir %{_datadir}/Thunar/sendto/
	
%{_datadir}/Thunar/sendto/*.desktop
	
%{_datadir}/polkit-1/actions/org.xfce.thunar.policy
	
%{_datadir}/applications/*.desktop
	
%{_datadir}/dbus-1/services/org.xfce.Thunar.FileManager1.service
	
%{_datadir}/dbus-1/services/org.xfce.FileManager.service
	
%{_datadir}/dbus-1/services/org.xfce.Thunar.service
	
%{_datadir}/icons/hicolor/*/*/*
	
%{_datadir}/xfce4/panel/plugins/thunar-tpa.desktop
	
%{_metainfodir}/org.xfce.thunar.appdata.xml
	
%{_libdir}/xfce4/panel/plugins/libthunar-tpa.so
	
%{_libdir}/girepository-1.0/*.0.typelib
	
%{_mandir}/man1/Thunar.1*
	
%dir %{_sysconfdir}/xdg/Thunar
	
%config(noreplace) %{_sysconfdir}/xdg/Thunar/uca.xml
	
%{_userunitdir}/thunar.service
	
 
	
%files devel
	
%doc examples
	
%{_includedir}/thunarx-*/
	
%{_libdir}/libthunar*.so
	
%{_libdir}/pkgconfig/thunarx-*.pc
	
%{_datadir}/gir-1.0/*.gir
	
 
	
%files docs
	
%dir %{_datadir}/gtk-doc/html/thunarx
	
%{_datadir}/gtk-doc/html/thunarx/*
	
 
	
%changelog
	
%autochangelog
