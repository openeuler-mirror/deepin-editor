##%global debug_package   %{nil}
%define pkgrelease  3
%if 0%{?openeuler}
%define specrelease %{pkgrelease}
%else
## allow specrelease to have configurable %%{?dist} tag in other distribution
%define specrelease %{pkgrelease}%{?dist}
%endif

Name:           deepin-editor
Version:        5.9.7
Release:        %{specrelease}
Summary:        Simple editor for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-fix-broken-KF5-include-path.patch

BuildRequires: cmake3
BuildRequires: qt5-devel
BuildRequires: gcc-c++
BuildRequires: freeimage-devel
BuildRequires: dtkwidget-devel
BuildRequires: dtkcore-devel
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(polkit-qt5-1)
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(dframeworkdbus)
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-private-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-syntax-highlighting-devel
BuildRequires: gtest-devel
BuildRequires: gmock-devel



%description
%{summary}.

%prep
%setup -q
%patch0 -p1

# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
# cmake_minimum_required version is too high
sed -i "s|^cmake_minimum_required.*|cmake_minimum_required(VERSION 3.0)|" $(find . -name "CMakeLists.txt")
mkdir build && pushd build
%cmake -DCMAKE_BUILD_TYPE=Release -DAPP_VERSION=%{version} -DVERSION=%{version}  ../
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

# %check
# desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:

%files
%doc README.md
%license LICENSE
# %{_bindir}/dedit
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/deepin-manual/manual-assets/application/deepin-editor/editor/*

%changelog
* Wed Dec 21 2022 liweiganga <liweiganga@uniontech.com> - 5.9.7-3
- enable debuginfo for fix strip

* Wed Jul 27 2022 liweiganga <liweiganga@uniontech.com> - 5.9.7-2
- fix: broken KF5 include path

* Mon Jul 18 2022 konglidong <konglidong@uniontech.com> - 5.9.7-1
- update to 5.9.7

* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.6.28-1
- Update 5.6.28

* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.1-4
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-3
- Package init
