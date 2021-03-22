%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss06
Version:        5.0.9
Release:        1%{?dist}
Summary:        Slender typeface for code, from code.

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  clang
BuildRequires:  npm
BuildRequires:  ttfautohint

%description
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.

%prep
%autosetup -n %{source_name}-%{version}

# Iosevka SS06 — Monospace, Liberation Mono Style
%package -n iosevka-ss06-fonts
Summary:        Monospace, Liberation Mono Style
%description -n iosevka-ss06-fonts
Iosevka Monospace, Liberation Mono Style

%package -n iosevka-term-ss06-fonts
Summary:        Monospace, Liberation Mono Style
%description -n iosevka-term-ss06-fonts
Iosevka Monospace, Liberation Mono Style

%package -n iosevka-fixed-ss06-fonts
Summary:        Monospace, Liberation Mono Style
%description -n iosevka-fixed-ss06-fonts
Iosevka Monospace, Liberation Mono Style

%build
npm install

npm run build -- ttf::iosevka-ss06
npm run build -- ttf::iosevka-term-ss06
npm run build -- ttf::iosevka-fixed-ss06

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss06/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss06-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss06/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss06-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss06/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss06-fonts

# Iosevka SS06 — Monospace, Liberation Mono Style
%files -n iosevka-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss06-fonts/*

%files -n iosevka-term-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss06-fonts/*

%files -n iosevka-fixed-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss06-fonts/*

%changelog
* Mon Mar 22 09:33:49 EDT 2021 Peter Wu - v5.0.9
- Release v5.0.9
* Sun Mar 14 20:17:31 EDT 2021 Peter Wu - v5.0.8
- Release v5.0.8
* Sat Mar 13 18:47:27 EST 2021 Peter Wu - v5.0.6
- Release v5.0.6
* Sat Mar 06 09:55:14 EST 2021 Peter Wu - v5.0.5
- Release v5.0.5
* Sat Feb 27 15:47:08 EST 2021 Peter Wu - v5.0.4
- Release v5.0.4
* Sat Feb 20 16:29:32 EST 2021 Peter Wu - v5.0.3
- Release v5.0.3
* Wed Feb 17 09:20:02 EST 2021 Peter Wu - v5.0.2
- Release v5.0.2
* Sun Feb 14 11:13:38 EST 2021 Peter Wu - v5.0.1
- Release v5.0.1
* Sat Feb 13 09:54:24 EST 2021 Peter Wu - v5.0.0
- Release v5.0.0
* Sat Jan 16 09:19:10 EST 2021 Peter Wu - v4.5.0
- Release v4.5.0
* Sat Jan 09 09:14:30 EST 2021 Peter Wu - v4.4.0
- Release v4.4.0
* Sat Jan 02 13:23:06 EST 2021 Peter Wu - v4.3.0
- Release v4.3.0
* Sat Dec 26 09:19:12 EST 2020 Peter Wu - v4.2.0
- Release v4.2.0
* Sat Dec 19 18:01:02 EST 2020 Peter Wu - v4.1.1
- Release v4.1.1
* Sat Dec 19 09:06:44 EST 2020 Peter Wu - v4.1.0
- Release v4.1.0
* Sat Dec 12 09:28:44 EST 2020 Peter Wu - v4.0.3
- Release v4.0.3
* Sun Dec 06 10:38:56 EST 2020 Peter Wu - v4.0.2
- Release v4.0.2
* Sat Dec 05 10:18:42 EST 2020 Peter Wu - v4.0.1
- Release v4.0.1
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0
