%define distfile ARJL_310
Summary:	ARJ archiver for Linux
Summary(pl):	Archiwizator ARJ dla Linuksa
Name:		arj
Version:	3.10
Release:	1
License:	Shareware, distributable
Vendor:		ARJ Software Russia
Group:		Applications/Archiving
# The original URL is outdated:	ftp://ftp.black.ru/fileecho/AUTLCOMP/%{distfile}
Source0:	%distfile
ExclusiveOS:	Linux
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define no_install_post_strip 1

%description
This product is an implementation of ARJ v 2.7x for DOS on UNIX and
UNIX-like systems. It is assumed that the user is familiar with ARJ
operation on DOS before using this package.

%description -l pl
Jest to implementacja programu ARJ v 2.7x dla DOS na platformê UNIX i
systemy uniksopodobne. Zak³ada siê, ¿e u¿ytkownik korzystaj±cy z tego
pakietu zna sposób funkcjonowania programu ARJ pod DOS-em.

%prep
%setup -q -T -c
install %{SOURCE0} .
chmod 755 %{distfile}
./%{distfile} << EOF
y
n

y
y
EOF
bin/arj | head -4 > doc/arj/LICENSE

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

mv -f bin/register bin/register-arj
install bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/arj/*
%attr(0755, root, root) %{_bindir}/*
