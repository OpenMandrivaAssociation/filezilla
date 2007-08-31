%define betaver rc2

Name:           filezilla
Version:        3.0.0
Release:        %mkrel -c %{betaver} 3
Summary:        FileZilla is a fast and reliable FTP client

Group:          Networking/File transfer
License:        GPL 
URL:            http://filezilla.sourceforge.net/
Source0:        FileZilla_%{version}-%{betaver}_src.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  libwxgtk2.8-devel
BuildRequires:  idn-devel
BuildRequires:  gnutls-devel
BuildRequires:	ImageMagick

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
%setup -q -n %name-%version-%betaver


%build
%configure2_5x 
%make 


%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps

cp src/interface/resources/filezilla.png %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/filezilla.png
convert -resize 16x16 src/interface/resources/filezilla.png %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/filezilla.png
convert -resize 48x48 src/interface/resources/filezilla.png %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/filezilla.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
