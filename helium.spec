%define app_name helium
%define version 0.6.7.1

%ifarch aarch64
%define release_arch arm64
%endif
%ifarch x86_64
%define release_arch x86_64
%endif

Name:           %{app_name}
Version:        %{version}
Release:        1%{?dist}
Summary:        Helium Browser
License:        GPL-3.0
URL:            https://github.com/imputnet/helium
Source0:        https://github.com/imputnet/helium-linux/releases/download/%{version}/%{app_name}-%{version}-%{release_arch}_linux.tar.xz
Source1:        helium-wrapper

%global debug_package %{nil}
%global __brp_check_rpaths %{nil}

%description
Helium is a lightweight, fast, and secure web browser based on Chromium.

%prep
%setup -q -n %{app_name}-%{version}-%{release_arch}_linux

%build
# No build needed

%install
mkdir -p %{buildroot}/opt/%{app_name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

cp -a * %{buildroot}/opt/%{app_name}/

# Install proper wrapper and link it to bindir
rm -f %{buildroot}/opt/%{app_name}/chrome-wrapper

install -m 755 %{SOURCE1} %{buildroot}/opt/%{app_name}/helium-wrapper
ln -sf /opt/%{app_name}/helium-wrapper %{buildroot}%{_bindir}/%{app_name}

# Install icon
install -m 644 product_logo_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{app_name}.png

# Install .desktop file
# Point exec to wrapper
sed -i 's|Exec=chromium|Exec=%{app_name}|g' %{buildroot}/opt/%{app_name}/%{app_name}.desktop
sed -i 's|Icon=.*|Icon=%{app_name}|g' %{buildroot}/opt/%{app_name}/%{app_name}.desktop

mv %{buildroot}/opt/%{app_name}/%{app_name}.desktop %{buildroot}%{_datadir}/applications/

%files
%defattr(-,root,root,-)
/opt/%{app_name}/
%{_bindir}/%{app_name}
%{_datadir}/applications/%{app_name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{app_name}.png

%post
# Refresh icon cache and update desktop database
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
# Refresh icon cache and update desktop database
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Tue Nov 25 2025 GitHub Action <action@github.com> - 0.6.7.1
- Auto-updated to version 0.6.7.1

* Tue Nov 25 2025 GitHub Action <action@github.com> - 0.6.7.1
- Auto-updated to version 0.6.7.1

* Tue Nov 25 2025 GitHub Action <action@github.com> - 0.6.7.1
- Auto-updated to version 0.6.7.1

* Tue Nov 25 2025 GitHub Action <action@github.com> - 0.6.7.1
- Auto-updated to version 0.6.7.1

* Tue Nov 26 2024 jhuang6451 <xplayerhtz123@gmail.com> - 0.6.7.1-2
- Replace wrapper script

* Tue Nov 26 2024 jhuang6451 <xplayerhtz123@gmail.com> - 0.6.7.1-1
- Initial RPM release based on version 0.6.7.1