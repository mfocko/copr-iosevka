%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss09
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

# Iosevka SS09 — Monospace, Source Code Pro Style
%package -n iosevka-ss09-fonts
Summary:        Monospace, Source Code Pro Style
%description -n iosevka-ss09-fonts
Iosevka Monospace, Source Code Pro Style

%package -n iosevka-term-ss09-fonts
Summary:        Monospace, Source Code Pro Style
%description -n iosevka-term-ss09-fonts
Iosevka Monospace, Source Code Pro Style

%package -n iosevka-fixed-ss09-fonts
Summary:        Monospace, Source Code Pro Style
%description -n iosevka-fixed-ss09-fonts
Iosevka Monospace, Source Code Pro Style

%build
npm install

npm run build -- ttf::iosevka-ss09
npm run build -- ttf::iosevka-term-ss09
npm run build -- ttf::iosevka-fixed-ss09

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss09/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss09-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss09/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss09-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss09/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss09-fonts

# Iosevka SS09 — Monospace, Source Code Pro Style
%files -n iosevka-ss09-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss09-fonts/*

%files -n iosevka-term-ss09-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss09-fonts/*

%files -n iosevka-fixed-ss09-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss09-fonts/*

%changelog
* Sat Dec 05 10:18:42 EST 2020 Peter Wu - v4.0.1
- Release v4.0.1
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0