Summary:	ARJ archiver for Linux
Summary(pl):	Archiwizator ARJ dla Linuksa
Name:		arj
Version:	3.10.21
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Archiving
Source0:	http://testcase.newmail.ru/files/%{name}-%{version}.tar.gz
# Source0-md5:	887d400ca6048516d4d447e1649af396
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip 1

%description
This product is an implementation of ARJ v 2.7x for DOS on UNIX and
UNIX-like systems. It is assumed that the user is familiar with ARJ
operation on DOS before using this package.

%description -l pl
Jest to implementacja programu ARJ v 2.7x dla DOS na platformê UNIX i
systemy uniksopodobne. Zak³ada siê, ¿e u¿ytkownik korzystaj±cy z tego
pakietu zna sposób funkcjonowania programu ARJ pod DOS-em.

%prep
%setup -q

%build
cd gnu
%{__autoconf}
install %{_datadir}/automake/config.* .

%configure
cd ..
%{__make} \
	CC="%{__cc}" \
	CFLAGS_DBG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

cd linux-gnu/en/rs
install \
	arj/arj \
	arjdisp/arjdisp \
	rearj/rearj \
	$RPM_BUILD_ROOT%{_bindir}
install register/arj-register $RPM_BUILD_ROOT%{_bindir}/arj-register

install arjcrypt/arjcrypt.so $RPM_BUILD_ROOT%{_libdir}

%{!?debug:strip -R .comment -R .note $RPM_BUILD_ROOT%{_bindir}/{arjdisp,rearj,arj-register}}
%{!?debug:strip --strip-unneeded -R .comment -R .note $RPM_BUILD_ROOT%{_libdir}/*.so}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/rev_hist.txt resource/en/arjl.txt resource/en/readme.txt resource/en/unix.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
