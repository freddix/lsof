Summary:	Lists files open by processes
Name:		lsof
Version:	4.87
Release:	2
License:	Free
Group:		Applications/System
Source0:	ftp://lsof.itap.purdue.edu/pub/tools/unix/lsof/%{name}_%{version}.tar.bz2
# Source0-md5:	80e2a76d0e05826db910ec88e631296c
URL:		http://people.freebsd.org/~abe/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lsof's name stands for LiSt Open Files, and it does just that. It
lists information about files that are open by the processes running
on a UNIX system.

%prep
%setup -q -c
cd %{name}_%{version}
tar xf %{name}_%{version}_src.tar

%build
cd %{name}_%{version}/%{name}_%{version}_src

export LSOF_CC="%{__cc}"
./Configure -n linux
%{__make} \
	DEBUG="%{rpmcppflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

cd %{name}_%{version}/%{name}_%{version}_src

install lsof $RPM_BUILD_ROOT%{_sbindir}
install lsof.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}_%{version}/{00*,README.*,RELEASE*} %{name}_%{version}/%{name}_%{version}_src/00*
%attr(755,root,root) %{_sbindir}/lsof
%{_mandir}/man8/*

