Name:		filezilla
Version:	3.5.3
Release:	1
Summary:	Fast and reliable FTP client
Group:		Networking/File transfer
License:	GPLv2+
#old url http://filezilla.sourceforge.net/
URL:		http://filezilla-project.org/
Source0:	http://download.sourceforge.net/filezilla/FileZilla_%{version}_src.tar.bz2
BuildRequires:	wxgtku2.8-devel >= 2.8.12
BuildRequires:	idn-devel
BuildRequires:	gnutls-devel
BuildRequires:	dbus-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	xdg-utils
BuildRequires:	sqlite3-devel

%description
FileZilla is a fast and reliable FTP client and server with lots 
of useful features and an intuitive interface

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-autoupdatecheck --with-tinyxml=builtin
%make

%install
%makeinstall_std

%__mkdir_p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
%__cp src/interface/resources/16x16/filezilla.png %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/filezilla.png
%__cp src/interface/resources/32x32/filezilla.png %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/filezilla.png
%__cp src/interface/resources/48x48/filezilla.png %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/filezilla.png

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
%{_iconsdir}/hicolor/*/apps/filezilla.png
%{_datadir}/applications/filezilla.desktop
%{_datadir}/pixmaps/filezilla.png
%{_mandir}/man*/*
