%global xfceversion 4.17

Name:           xfce4-dev-tools
Version:        4.17.0
Release:        1%{?dist}
Summary:        Xfce developer tools

License:        GPLv2+
URL:            http://xfce.org/~benny/projects/xfce4-dev-tools/
#VCS git:git://git.xfce.org/xfce/xfce4-dev-tools
Source0:        https://archive.xfce.org/src/xfce/xfce4-dev-tools/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  glib2-devel

%description
This package contains common tools required by Xfce developers and people
that want to build Xfce from SVN.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install


%files
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS
%{_bindir}/xfce-build
%{_bindir}/xfce-do-release
%{_bindir}/xfce-get-release-notes
%{_bindir}/xfce-get-translations
%{_bindir}/xfce-update-news
%{_bindir}/xdt-autogen
%{_bindir}/xdt-csource
%{_datadir}/aclocal/*
%{_mandir}/man1/xdt-csource.1.gz

%changelog
* Tue Mar 8 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 4.17.0-1
* Update to 4.17.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.16.0-1
- Update to 4.16.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.14.0-1
- Update to 4.14.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.0-1
- Update to 4.13.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Kevin Fenzi <kevin@scrye.com> 4.12.0-1
- Update to 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-4
- Require missing dependencies (#964474)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-1
- Update to 4.10.0 final
- Add VCS key

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.2-1
- Update to 4.9.2 (Xfce 4.10pre2)

* Sun Apr 01 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.1-1
- Update to 4.9.1
- Packge is no longer noarch.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.0-1
- Update to 4.8.0 final. 

* Sun Jan 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.4-1
- Update to 4.7.4

* Sun Oct 31 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3

* Mon Sep 21 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.2-1
- Update to 4.7.2

* Sun Sep 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.1-1
- Update to 4.7.1

* Wed Aug 19 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.0-1
- Update to 4.7.0

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.0-1
- Update to 4.6.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.99.1-1
- Update to 4.5.99.1

* Tue Jan 13 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.93-1
- Update to 4.5.93

* Sun Dec 28 2008 Kevin Fenzi <kevin@tummy.com> - 4.5.92-1
- Update to 4.5.92

* Mon Sep 08 2008 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.0.1-1
- Update to 4.4.0.1

* Tue Aug 12 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 4.4.0-2
- Fix license tag.

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0.

* Sat Nov 11 2006 Christoph Wickert <cwickert@fedoraproject.org> - 4.3.99.2-1
- Update to 4.3.99.2.

* Tue Oct 03 2006 Christoph Wickert <cwickert@fedoraproject.org> - 4.3.99.1-3
- Require gettext-devel.
- Install m4 macros also to /usr/share/aclocal.

* Tue Oct 03 2006 Christoph Wickert <cwickert@fedoraproject.org> - 4.3.99.1-2
- Some more requires: glib2-devel, make and gtk-doc.
- Own %%{_datadir}/xfce4

* Sat Sep 23 2006 Christoph Wickert <cwickert@fedoraproject.org> - 4.3.99.1-1
- Initial Fedora Extras release.
