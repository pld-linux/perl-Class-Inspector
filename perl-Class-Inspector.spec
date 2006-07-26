#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Inspector
Summary:	Class::Inspector - provides information about classes
Summary(pl):	Class::Inspector - dostarczenie informacji o klasach
Name:		perl-Class-Inspector
Version:	1.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	46eeeeb5a5df0da03f4e53229f7ed360
URL:		http://search.cpan.org/dist/Class-Inspector/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(Test::More)
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

%description -l pl
Class::Inspector umo¿liwia pobieranie informacji o za³adowanych
klasach. Wiêkszo¶æ z tych informacji mo¿na znale¼æ na inne sposoby,
ale nie zawsze s± one przyjazne i zwykle wymagaj± dosyæ du¿ej
znajomo¶ci perlowej magii lub dziwnego i niezwykle wygl±daj±cego kodu.
Class::Inspector próbuje dostarczyæ ³atwiejszy, bardziej przyjazny
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
%{perl_vendorlib}/Class/*.pm
%{_mandir}/man3/*
