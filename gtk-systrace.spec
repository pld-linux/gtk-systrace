%define	_ver	2003-06-23
Summary:	GTK Systrace front end invoked by systrace
Name:		gtk-systrace
Version:	0.1
Release:	0.%(echo %{_ver} | tr - .).1
License:	GPL
Group:		X11/Applications
Source0:	http://www.citi.umich.edu/u/provos/systrace/%{name}-%{_ver}.tar.gz
# Source0-md5:	4073ae27ec31a6c66e16f134bdd37929
Patch0:		%{name}-build.patch
URL:		http://www.citi.umich.edu/u/provos/systrace/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
Requires:	systrace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK Systrace front end invoked by systrace.

%prep
%setup -q -n notification-%{version}
%patch0 -p1

%build
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s $RPM_BUILD_ROOT%{_bindir}/notification xsystrace

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/notification
