%define prerel rc1

Name:           filezilla
Version:        3.0.2
Release:        %mkrel -c %prerel 1
Summary:        FileZilla is a fast and reliable FTP client

Group:          Networking/File transfer
License:        GPLv2 
URL:            http://filezilla.sourceforge.net/
Source0:        http://nchc.dl.sourceforge.net/sourceforge/%{name}/FileZilla_%{version}-%{prerel}_src.tar.bz2
Patch1:		FileZilla_3.0.0-rc3-fix-desktopfile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  wxGTK2.8-devel
BuildRequires:  idn-devel
BuildRequires:  gnutls-devel
BuildRequires:	ImageMagick
BuildRequires:	desktop-file-utils

%description
FileZilla is a fast and reliable FTP client and server with lots 
of useful features and an intuitive interface

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/fzsftp
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources
%{_datadir}/%{name}/docs/fzdefaults.xml.example
%{_iconsdir}/hicolor/*/apps/filezilla.png
%{_datadir}/applications/filezilla.desktop
%{_datadir}/pixmaps/filezilla.png

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version-%{prerel}
%patch1 -p0

%build
%configure2_5x 
%make 


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
	%buildroot%_datadir/applications/*.desktop

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
