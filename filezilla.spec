# build segfaults
%define _disable_lto 1
%define _disable_rebuild_configure 1

Summary:	Fast and reliable FTP client
Name:		filezilla
Version:	3.43.0
Release:	1
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://filezilla-project.org/
Source0:	http://download.filezilla-project.org/FileZilla_%{version}_src.tar.bz2

BuildRequires:	desktop-file-utils
BuildRequires:	xdg-utils
BuildRequires:	wxgtku3.0-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:  pugixml-devel > 1.5
BuildRequires:	pkgconfig(libfilezilla)
Requires:	xdg-utils

%description
FileZilla is a fast and reliable FTP client and server with lots 
of useful features and an intuitive interface

%prep
%setup -q

%build
%ifarch %ix86
export CC=gcc
export CXX=g++
%endif

%configure \
	--disable-autoupdatecheck \
	--with-tinyxml=builtin
%make LIBS="-lpthread"

%install
%make_install

desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--add-category='GTK' \
	--add-category='X-MandrivaLinux-CrossDesktop'\
	%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/fzsftp
%{_bindir}/fzputtygen
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources
%dir %{_datadir}/%{name}/docs
%{_datadir}/%{name}/docs/fzdefaults.xml.example
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man*/*
