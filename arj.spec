%define distfile ARJL_310

Summary: ARJ for Linux
Name: arj
Version: 3.10
Release: 0.1
Copyright: shareware
Vendor: ARJ Software Russia
ExclusiveOS: Linux
ExclusiveArch: i386
Group: Applications/Archiving
Source: ftp://ftp.black.ru/fileecho/AUTLCOMP/%{distfile}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This product is an implementation of ARJ v 2.7x for DOS on UNIX and
UNIX-like systems. It is assumed that the user is familiar with ARJ
operation on DOS before using this package.


%prep
%setup -T -c
chmod 755 ${RPM_SOURCE_DIR}/%{distfile}
${RPM_SOURCE_DIR}/%{distfile} << EOF
y
n

y
y
EOF

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mv bin/register bin/register-arj
install -m 644 bin/* ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(0644, root, root, 0755)
%doc doc/arj/*
%attr(0755, root, root) %{_bindir}/*
