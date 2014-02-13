Summary:	Fast and reliable FTP client
Name:		filezilla
Version:	3.7.4
Release:	1
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://filezilla-project.org/
Source0:	http://download.sourceforge.net/filezilla/FileZilla_3.7.4_src.tar.bz2

BuildRequires:	desktop-file-utils
BuildRequires:	xdg-utils
BuildRequires:	wxgtku-devel >= 2.8.12
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(sqlite3)
Requires:	xdg-utils

%description
FileZilla is a fast and reliable FTP client and server with lots 
of useful features and an intuitive interface

%prep
%setup -q

%build
%configure2_5x \
	--disable-autoupdatecheck \
	--with-tinyxml=builtin
%make LIBS="-lpthread"

%install
%makeinstall_std

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
%{_datadir}/%{name}/docs/fzdefaults.xml.example
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man*/*



