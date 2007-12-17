%define version 0.06
%define release %mkrel 4
%define realname	Acme-JavaTrace
%define name 	perl-%{realname}

Summary:	Module for using Java-like stack traces
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Development/Perl
Source: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Acme/%{realname}-%{version}.tar.bz2
URL: 		http://search.cpan.org/dist/%{realname}
BuildRequires:	perl-devel
Requires: 	perl
BuildArch:	noarch
   
%description
<buzzword>This module tries to improves the Perl programmer experience
by porting the Java paradigm to print stack traces, which is more professional
than Perl's way.</buzzword>

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%{perl_vendorlib}
%{_mandir}/*/*
%doc Changes README INSTALL

%clean
rm -rf $RPM_BUILD_ROOT


