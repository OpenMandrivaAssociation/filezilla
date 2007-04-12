Name:           filezilla
Version:        3.0.0
Release:        %mkrel 0.beta6.2
Summary:        FileZilla is a fast and reliable FTP client

Group:          Networking/File transfer
License:        GPL 
URL:            http://filezilla.sourceforge.net/
Source0:        FileZilla_3.0.0-beta6_src.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  libwxgtk2.8-devel
BuildRequires:  idn-devel
BuildRequires:  gnutls-devel

%description
FileZilla is a fast and reliable FTP client and server with lots 
of useful features and an intuitive interface

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/fzsftp
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources
%{_datadir}/%{name}/locales
%{_datadir}/applications/*-%{name}.desktop
%{_iconsdir}/filezilla.png

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version-beta6


%build
%configure 
%make 


%install
rm -rf %buildroot
make install DESTDIR=%buildroot

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Filezilla
Comment=FileZilla is a fast and reliable FTP client
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Internet-FileTransfer;Network;FileTransfer;
Encoding=UTF-8
EOF

%__mkdir -p %{buildroot}/%{_iconsdir}

ln -s %{buildroot}%{_datadir}/filezilla/resources/filezilla.png %{buildroot}/%{_iconsdir}/filezilla.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT


