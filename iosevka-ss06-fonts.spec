%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss06
Version:        4.0.1
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
* Sat Dec 05 10:18:42 EST 2020 Peter Wu - v4.0.1
- Release v4.0.1
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0
