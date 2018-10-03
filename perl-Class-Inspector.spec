#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Inspector
Summary:	Class::Inspector - provides information about classes
Summary(pl.UTF-8):	Class::Inspector - dostarczenie informacji o klasach
Name:		perl-Class-Inspector
Version:	1.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	db471d6ecf47fa054726553319b7c34f
URL:		http://metacpan.org/release/Class-Inspector
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl-Test-Simple >= 0.94
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Inspector allows you to get information about a loaded class.
Most or all of this information can be found in other ways, but they
aren't always very friendly, and usually involve a relatively high
level of Perl wizardry, or strange and unusual looking code.
Class::Inspector attempts to provide an easier, more friendly
interface to this information.

%description -l pl.UTF-8
Class::Inspector umożliwia pobieranie informacji o załadowanych
klasach. Większość z tych informacji można znaleźć na inne sposoby,
ale nie zawsze są one przyjazne i zwykle wymagają dosyć dużej
znajomości perlowej magii lub dziwnego i niezwykle wyglądającego kodu.
Class::Inspector próbuje dostarczyć łatwiejszy, bardziej przyjazny
interfejs do tych informacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
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
%doc Changes README
%{perl_vendorlib}/Class/Inspector.pm
%{perl_vendorlib}/Class/Inspector/Functions.pm
%{_mandir}/man3/Class::Inspector*.3pm*
