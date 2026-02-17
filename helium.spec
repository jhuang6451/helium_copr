%define app_name helium
%define version 0.9.2.1

Name:           helium-browser
Version:        %{version}
Release:        1%{?dist}
Summary:        Helium Browser
License:        GPL-3.0
URL:            https://github.com/imputnet/helium
Source0:        https://github.com/imputnet/helium-linux/releases/download/%{version}/%{app_name}-%{version}-x86_64_linux.tar.xz
Source1:        https://github.com/imputnet/helium-linux/releases/download/%{version}/%{app_name}-%{version}-arm64_linux.tar.xz
Source2:        helium-wrapper

%global debug_package %{nil}
%global __brp_check_rpaths %{nil}

%description
Helium is a lightweight, fast, and secure web browser based on Chromium.

%prep
%ifarch x86_64
%setup -q -T -b 0 -n %{app_name}-%{version}-x86_64_linux
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{app_name}-%{version}-arm64_linux
%endif

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

install -m 755 %{SOURCE2} %{buildroot}/opt/%{app_name}/helium-wrapper
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
* Tue Feb 17 2026 GitHub Action <action@github.com> - 0.9.2.1
- Auto-updated to version 0.9.2.1

* Mon Feb 16 2026 GitHub Action <action@github.com> - 0.9.1.1
- Auto-updated to version 0.9.1.1

* Fri Feb 06 2026 GitHub Action <action@github.com> - 0.8.5.1
- Auto-updated to version 0.8.5.1

* Thu Jan 29 2026 GitHub Action <action@github.com> - 0.8.4.1
- Auto-updated to version 0.8.4.1

* Tue Jan 27 2026 GitHub Action <action@github.com> - 0.8.3.1
- Auto-updated to version 0.8.3.1

* Tue Jan 27 2026 GitHub Action <action@github.com> - null
- Auto-updated to version null

* Thu Jan 22 2026 GitHub Action <action@github.com> - 0.8.3.1
- Auto-updated to version 0.8.3.1

* Thu Jan 22 2026 GitHub Action <action@github.com> - 0.8.2.1
- Auto-updated to version 0.8.2.1

* Thu Jan 22 2026 GitHub Action <action@github.com> - null
- Auto-updated to version null

* Sun Jan 18 2026 GitHub Action <action@github.com> - 0.8.2.1
- Auto-updated to version 0.8.2.1

* Thu Jan 08 2026 GitHub Action <action@github.com> - 0.7.10.1
- Auto-updated to version 0.7.10.1

* Sat Jan 03 2026 GitHub Action <action@github.com> - 0.7.9.1
- Auto-updated to version 0.7.9.1

* Fri Jan 02 2026 GitHub Action <action@github.com> - 0.7.7.2
- Auto-updated to version 0.7.7.2

* Mon Dec 22 2025 GitHub Action <action@github.com> - 0.7.7.1
- Auto-updated to version 0.7.7.1

* Wed Dec 17 2025 GitHub Action <action@github.com> - 0.7.6.1
- Auto-updated to version 0.7.6.1

* Tue Dec 16 2025 GitHub Action <action@github.com> - 0.7.5.1
- Auto-updated to version 0.7.5.1

* Sat Dec 13 2025 GitHub Action <action@github.com> - 0.7.4.1
- Auto-updated to version 0.7.4.1

* Wed Dec 10 2025 GitHub Action <action@github.com> - 0.7.3.1
- Auto-updated to version 0.7.3.1

* Sun Dec 07 2025 GitHub Action <action@github.com> - 0.7.2.1
- Auto-updated to version 0.7.2.1

* Sat Dec 06 2025 GitHub Action <action@github.com> - 0.7.1.1
- Auto-updated to version 0.7.1.1

* Mon Dec 01 2025 GitHub Action <action@github.com> - 0.6.9.1
- Auto-updated to version 0.6.9.1

* Tue Nov 25 2025 GitHub Action <action@github.com> - 0.6.7.1
- Auto-updated to version 0.6.7.1

* Tue Nov 25 2025 jhuang6451 <xplayerhtz123@gmail.com> - 0.6.6.1-3
- Fix source files and architecture definitions

* Tue Nov 25 2025 jhuang6451 <xplayerhtz123@gmail.com> - 0.6.6.1-2
- Replace wrapper script

* Tue Nov 25 2025 jhuang6451 <xplayerhtz123@gmail.com> - 0.6.6.1-1
- Initial RPM release based on version 0.6.6.1