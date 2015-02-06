%define upstream_name    CGI-Application-Plugin-Config-YAML
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Add Config::YAML support to CGI::Application
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Config::YAML)
BuildRequires:	perl(CGI::Application)
BuildArch:	noarch

%description
This plug-in add Config::YAML support to CGI::Application. The usage of this
plug-in is almost the same as CGI::Application::Plugin::Config::Simple. This
plug-in can be easily used instead of CGI::Application::Plugin::Config::Simple.
This plug-in refers to CGI::Application::Plugin::Config::Simple.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.10.0-2mdv2011.0
+ Revision: 653390
- rebuild for updated spec-helper

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 405773
- rebuild using %%perl_convert_version

* Fri Oct 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdv2009.1
+ Revision: 291380
- import perl-CGI-Application-Plugin-Config-YAML


* Thu Oct 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdv2009.1
- initial mdv release, generated with cpan2dist

