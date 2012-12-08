%define version 3.6.0.2
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
Version:        %{version}
Release:        %{release}
Summary:        Fast and reliable FTP client
Group:          Networking/File transfer
License:        GPLv2+
URL:            http://filezilla-project.org/
Source0:        http://download.sourceforge.net/filezilla/FileZilla_%{tarballver}_src.tar.bz2
BuildRequires:  wxgtku2.8-devel >= 2.8.12
BuildRequires:  idn-devel
BuildRequires:  pkgconfig(gnutls)
BuildRequires:	dbus-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils xdg-utils
BuildRequires:  pkgconfig(sqlite3)
Requires:	xdg-utils

%description
FileZilla is a fast and reliable FTP client and server with lots 
of useful features and an intuitive interface

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/fzsftp
%{_bindir}/fzputtygen
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources
%{_datadir}/%{name}/docs/fzdefaults.xml.example
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{tarballver}

%build
%configure2_5x --disable-autoupdatecheck --with-tinyxml=builtin
%make LIBS="-lpthread"

%install
%makeinstall_std

desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--add-category='GTK' \
	--add-category='X-MandrivaLinux-CrossDesktop'\
	%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}
