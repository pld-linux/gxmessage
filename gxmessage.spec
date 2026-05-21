Summary:	Display a message using GTK+2 (like xmessage)
Summary(pl.UTF-8):	Program wyświetlający komunikat używając GTK+2 (podobny do xmessage)
Name:		gxmessage
Version:	2.20.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://trmusson.dreamhosters.com/stuff/%{name}-%{version}.tar.gz
# Source0-md5:	dbef00c5e9dd1fb3463b08044be7ae8e
URL:		https://trmusson.dreamhosters.com/programs.html#gxmessage
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	texinfo
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gxmessage is a GTK+2 based clone of xmessage. It is used to display a
message box with a text specified on the command line, a file or via a
pipe.

%description -l pl.UTF-8
gxmessage jest klonem xmessage korzystającym z GTK+2. Można go
wykorzystać do wyświetlania okienek z tekstem podanym z linii poleceń,
pliku lub potoku.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
%update_icon_cache hicolor

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/gxmessage.1*
%{_infodir}/gxmessage.info*
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_examplesdir}/%{name}-%{version}
