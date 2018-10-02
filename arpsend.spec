Summary:	arpsend - tool for network diagnostics and testing
Summary(pl.UTF-8):	arpsend - narzędzie do diagnostyki testowania sieci
Name:		arpsend
Version:	1.2.3
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://www.net.princeton.edu/software/arpsend/%{name}-%{version}.tar.gz
# Source0-md5:	283cfa7452e2c93fb5dc5311d22c1d6e
URL:		http://www.net.princeton.edu/software/arpsend/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnet-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arpsend sends an Ethernet frame containing an IP ARP request or reply
packet containing fields you specify. This is a diagnostic tool
intended for use by network administrators.

%description -l pl.UTF-8
arpsend wysyła ramkę ethernetową zawierającą żądanie lub odpowiedź ARP
z określonymi polami. Jest to narzędzie diagnostyczne przeznaczone dla
administratorów sieci.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/arpsend.8*
