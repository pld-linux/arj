Summary:	ARJ archiver for Linux
Summary(pl.UTF-8):	Archiwizator ARJ dla Linuksa
Name:		arj
Version:	3.10.22
Release:	7
Epoch:		1
License:	GPL
Group:		Applications/Archiving
Source0:	https://arj.sourceforge.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	f263bf3cf6d42a8b7e85b4fb514336d3
URL:		https://arj.sourceforge.net/
Patch0:		strnlen.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-format-security.patch
Patch3:		no-strip.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# main executable cannot be stripped (doesn't work then)
%define		no_install_post_strip 1
%define		specflags	-fno-unit-at-a-time

%description
This product is an implementation of ARJ v 2.7x for DOS on UNIX and
UNIX-like systems. It is assumed that the user is familiar with ARJ
operation on DOS before using this package.

%description -l pl.UTF-8
Jest to implementacja programu ARJ v 2.7x dla DOS na platformę UNIX i
systemy uniksopodobne. Zakłada się, że użytkownik korzystający z tego
pakietu zna sposób funkcjonowania programu ARJ pod DOS-em.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
cd gnu
%{__autoconf}
install /usr/share/automake/config.* .

export CFLAGS="%{rpmcflags} -D_GNU_SOURCE"
%configure
cd ..
%{__make} -j1 \
	CC="%{__cc}"

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
