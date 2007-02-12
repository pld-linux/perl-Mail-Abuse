#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Abuse
Summary:	Mail::Abuse - Helps parse and respond to miscellaneous abuse complaints
Summary(pl.UTF-8):   Mail::Abuse - pomoc przy analizie i odpowiedzi na różne skargi o nadużyciach
Name:		perl-Mail-Abuse
Version:	1.021
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	93fb9d6625a06f02b318e32911bc1d0e
URL:		http://search.cpan.org/dist/Mail-Abuse/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Date-Manip
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl(IO::File)
BuildRequires:	perl-IO-Zlib
BuildRequires:	perl(MIME::Entity)
BuildRequires:	perl(MIME::Parser)
BuildRequires:	perl-MIME-tools
BuildRequires:	perl(Mail::Mailer)
BuildRequires:	perl-MailTools
BuildRequires:	perl(Net::POP3) >= 2.23
BuildRequires:	perl-NetAddr-IP >= 3
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-Storable
BuildRequires:	perl(Test::More)
BuildRequires:	perl-Tie-NetAddr-IP >= 1.51
BuildRequires:	perl-TimeDate
BuildRequires:	perl-WWW-Google-Groups
BuildRequires:	perl-WWW-Mechanize
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module and the accompaining software can be used to automatically
parse and respond to various formats of abuse complaints. This
software is geared towards abuse desk administrators who need
sophisticated tools to deal with the complains.

%description -l pl.UTF-8
Ten moduł i towarzyszące oprogramowanie może być używane do
automatycznej analizy i odpowiadania na różne formaty skarg o
nadużyciach. To oprogramowanie jest ukierunkowane na administratorów
obsługujących zgłoszenia o nadużyciach, potrzebujących wyszukanych
narzędzi do obsługi skarg.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLSCRIPT=%{_bindir} \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/Abuse
%{_mandir}/man?/*
