# build segfaults
%define _disable_lto 1
%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1

Summary:	Fast and reliable FTP client
Name:		filezilla
Version:	3.67.1
Release:	1
Group:		Networking/File transfer
License:	GPLv2+
Url:		https://filezilla-project.org/
Source0:	https://download.filezilla-project.org/client/FileZilla_%{version}_src.tar.xz

BuildRequires:	which
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	xdg-utils
BuildRequires:	boost-regex-devel
BuildRequires:	wxgtk-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:  pkgconfig(nettle)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:  pugixml-devel
BuildRequires:	pkgconfig(libfilezilla)
Requires:	xdg-utils

%description
FileZilla is a fast and reliable FTP client and server with lots 
of useful features and an intuitive interface

%prep
%setup -q

%build
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
%{_libdir}/libfzclient-private-%{version}.so
%{_libdir}/libfzclient-private.so
%{_libdir}/libfzclient-commonui-private-%{version}.so
%{_libdir}/libfzclient-commonui-private.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources
%dir %{_datadir}/%{name}/docs
%{_datadir}/%{name}/docs/fzdefaults.xml.example
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man*/*
