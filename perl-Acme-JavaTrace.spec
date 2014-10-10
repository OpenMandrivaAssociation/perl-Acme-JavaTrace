%define upstream_name	Acme-JavaTrace
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Module for using Java-like stack traces
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Acme/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch
   
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
%makeinstall_std

%files
%doc Changes README INSTALL
%{perl_vendorlib}/*/*.pm
%{_mandir}/*/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 653287
- do not include arch dir

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1
+ Revision: 638891
- update to new version 0.08

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 406832
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.07-3mdv2009.0
+ Revision: 255256
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2008.1
+ Revision: 152821
- update to new version 0.07

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-4mdv2008.0
+ Revision: 85917
- rebuild


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 21:50:38 (53688)
- test in %%check, rebuild

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 21:49:34 (53687)
Import perl-Acme-JavaTrace

* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.06-2mdk
- Fix BuildRequires Using perl Policies
	- Source URL
- use mkrel

* Thu Aug 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- New release 0.06

* Wed May 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.04-1mdk
- 0.04

* Sun Mar 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.03-1mdk
- 0.03

* Tue Dec 14 2004 Olivier Thauvin <nanardon@mandrake.org> 0.02-2mdk
- Fix URL

* Tue Dec 14 2004 Olivier Thauvin <nanardon@mandrake.org> 0.02-1mdk
- 0.02
- For my queen :)

* Tue Jun 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.01-1mdk
- First mdk release to make Mandrakelinux professional

