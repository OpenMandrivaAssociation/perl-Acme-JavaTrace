%define upstream_name	Acme-JavaTrace
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Module for using Java-like stack traces
License: 	GPL
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Acme/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
   
%description
<buzzword>This module tries to improves the Perl programmer experience
by porting the Java paradigm to print stack traces, which is more professional
than Perl's way.</buzzword>

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README INSTALL
%{perl_vendorlib}
%{_mandir}/*/*
