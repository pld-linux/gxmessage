Summary:	Display a message using GTK+2 (like xmessage)
Summary(pl):	Program wyświetlający komunikat używając GTK+2 (podobny do xmessage)
Name:		gxmessage
Version:	2.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://homepages.ihug.co.nz/~trmusson/stuff/%{name}-%{version}.tar.gz
# Source0-md5:	3151d6a49a67c863e0dddb9058b7624f
URL:		http://homepages.ihug.co.nz/~trmusson/programs.html#gxmessage
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gxmessage is a GTK+2 based clone of xmessage. I is used to display a
message box with a text specified on the command line, a file or via a
pipe.

%description -l pl
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/gxmessage.1.*
%{_pixmapsdir}/*.png
%{_examplesdir}/%{name}-%{version}
