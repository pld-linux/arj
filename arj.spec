Summary:	ARJ archiver for Linux
Summary(pl):	Archiwizator ARJ dla Linuksa
Name:		arj
Version:	3.10b
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://testcase.newmail.ru/files/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This product is an implementation of ARJ v 2.7x for DOS on UNIX and
UNIX-like systems. It is assumed that the user is familiar with ARJ
operation on DOS before using this package.

%description -l pl
Jest to implementacja programu ARJ v 2.7x dla DOS na platform� UNIX i
systemy uniksopodobne. Zak�ada si�, �e u�ytkownik korzystaj�cy z tego
pakietu zna spos�b funkcjonowania programu ARJ pod DOS-em.

%prep
%setup -q

%build
cd gnu
%{__autoconf}
%configure
cd ..
%{__make} -f makefile.gnu prepare
%{__make} -f makefile.gnu

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

cd linux-gnu/en/rs
install \
	arj/arj \
	arjdisp/arjdisp \
	rearj/rearj \
	$RPM_BUILD_ROOT%{_bindir}
install register/register $RPM_BUILD_ROOT%{_bindir}/register-arj

install arjcrypt/arjcrypt.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/rev_hist.txt resource/en/arjl.txt resource/en/readme.txt resource/en/unix.txt
%attr(0755, root, root) %{_bindir}/*
%{_libdir}/*
