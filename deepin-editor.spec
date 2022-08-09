Name:           deepin-editor
Version:        5.6.28
Release:        2
Summary:        Simple editor for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-fix-broken-KF5-include-path.patch

BuildRequires: cmake3
BuildRequires: gcc-c++
BuildRequires: freeimage-devel
BuildRequires:  dtkcore-devel
BuildRequires:  dtkwidget-devel
BuildRequires: pkgconfig(dtkwm)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(polkit-qt5-1)
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-private-devel
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5SyntaxHighlighting)

%description
%{summary}.

%prep
%autosetup -p1

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
sed -i "s|^cmake_minimum_required.*|cmake_minimum_required(VERSION 3.0)|" $(find . -name "CMakeLists.txt")
%cmake . -DVERSION=%{version}
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/dedit
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Tue Aug 09 2022 liweiganga <liweiganga@uniontech.com> - 5.6.28-2
- fix: broken KF5 include path

* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.6.28-1
- Update 5.6.28

* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.1-4
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-3
- Package init

