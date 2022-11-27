Summary: arttime brings curated text-art to otherwise artless terminal emulators of starving developers and other users
Name: arttime
Version: %{version}
Release: %{releasenum}%{?dist}
License: CFLA v1.0 ("Collective Friendliness License Addendum" version 1.0)
Group: System Environment/Shells
URL: https://github.com/poetaman/arttime
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: zsh

%description
Beauty of text-art meets functionality of a feature-rich clock / timer / pattern-based time manager. In addition to its functional/productivity features, arttime brings curated text-art to otherwise artless terminal emulators of starving developers and other users who can use terminal. It is a cross-platform application with native notifications/sounds that runs well on macOS, Linux, and BSD Unixes.

%prep
%autosetup

%build
# nothing to do here

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
 
%{__install} -d %{buildroot}%{_bindir}
%{__install} -c -m 755 bin/%{name} %{buildroot}%{_bindir}/%{name}
%{__install} -c -m 755 bin/artprint %{buildroot}%{_bindir}/artprint

%{__install} -d %{buildroot}%{_datadir}/%{name}/textart
%{__install} -c -m 644 share/%{name}/textart/* %{buildroot}%{_datadir}/%{name}/textart/

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE_CODE LICENSE_ADDENDUM_CFLA LICENSE_ART
%{_bindir}/%{name}
%{_bindir}/artprint
%{_datadir}/%{name}/textart
# %attr(0644,root,root) %{_datadir}/%{name}/textart/*

%changelog
* Sun Nov 27 2022 Jaron Rubenstein <jaronrubenstein+arttime@gmail.com>
- Version bump to arttime v1.9.2

* Fri Oct 07 2022 Jaron Rubenstein <jaronrubenstein+arttime@gmail.com>
- Initial version of package for arttime v1.9.1
