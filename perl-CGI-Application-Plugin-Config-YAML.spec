%define module   CGI-Application-Plugin-Config-YAML
%define version    0.01
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    add Config::YAML support to CGI::Application
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/CGI/%{module}-%{version}.tar.gz
BuildRequires: perl(Config::YAML)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This plug-in add Config::YAML support to CGI::Application. The usage of this
plug-in is almost the same as CGI::Application::Plugin::Config::Simple. This
plug-in can be easily used instead of CGI::Application::Plugin::Config::Simple.
This plug-in refers to CGI::Application::Plugin::Config::Simple.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


