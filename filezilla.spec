%define version 3.2.0
%define betaver 0
%define rel 1
%if %betaver
%define release %mkrel -c %betaver %rel
%define tarballver %version-%betaver
%else
%define release %mkrel %rel
%define tarballver %version
%endif

Name:           filezilla
Version:        %version
Release:        %release
Summary:        Fast and reliable FTP client
Group:          Networking/File transfer
License:        GPLv2+ 
URL:            http://filezilla.sourceforge.net/
Source0:        http://nchc.dl.sourceforge.net/sourceforge/%{name}/FileZilla_%{tarballver}_src.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
%if %mdkversion > 200800
BuildRequires:  wxgtku2.8-devel >= 2.8.9
%else
BuildRequires:  wxgtku-devel >= 2.8.9
%endif
BuildRequires:  idn-devel
BuildRequires:  gnutls-devel
BuildRequires:	dbus-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils

%description
FileZilla is a fast and reliable FTP client and server with lots 
of useful features and an intuitive interface

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/fzsftp
%{_bindir}/fzputtygen
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources
%{_datadir}/%{name}/docs/fzdefaults.xml.example
%{_iconsdir}/hicolor/*/apps/filezilla.png
%{_datadir}/applications/filezilla.desktop
%{_datadir}/pixmaps/filezilla.png
%{_mandir}/man*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%tarballver

%build
%configure2_5x --disable-autoupdatecheck
%make -j1

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
cp src/interface/resources/16x16/filezilla.png %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/filezilla.png
cp src/interface/resources/32x32/filezilla.png %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/filezilla.png
cp src/interface/resources/48x48/filezilla.png %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/filezilla.png

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--add-category='GTK' \
	--add-category='X-MandrivaLinux-CrossDesktop'\
	%buildroot%_datadir/applications/*.desktop

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
