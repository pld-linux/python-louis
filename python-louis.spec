#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from liblouis.spec)

Summary:	Python 2 ctypes binding for liblouis
Summary(pl.UTF-8):	Wiązania Pythona 2 oparte na ctypes do biblioteki liblouis
Name:		python-louis
# keep 3.15.x for python2 support
Version:	3.15.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
#Source0Download: http://liblouis.org/downloads/
Source0:	https://github.com/liblouis/liblouis/releases/download/v%{version}/liblouis-%{version}.tar.gz
# Source0-md5:	ea605d9b55d5fc142a0678eb88bbf9d8
URL:		http://liblouis.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	liblouis >= 3.15.0
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 ctypes binding for liblouis.

%description -l pl.UTF-8
Wiązania Pythona 2 oparte na ctypes do biblioteki liblouis.

%package -n python3-%{module}
Summary:	Python 3 ctypes binding for liblouis
Summary(pl.UTF-8):	Wiązania Pythona 3 oparte na ctypes do biblioteki liblouis
Group:		Libraries/Python
Requires:	liblouis >= 3.15.0
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
Python 3 ctypes binding for liblouis.

%description -n python3-%{module} -l pl.UTF-8
Wiązania Pythona 3 oparte na ctypes do biblioteki liblouis.

%prep
%setup -q -n liblouis-%{version}

%{__sed} -e 's/###LIBLOUIS_SONAME###/liblouis.so.20/' python/louis/__init__.py.in >python/louis/__init__.py

%build
cd python

%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

cd python

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc python/README
%{py_sitescriptdir}/louis
%{py_sitescriptdir}/louis-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-louis
%defattr(644,root,root,755)
%doc python/README
%{py3_sitescriptdir}/louis
%{py3_sitescriptdir}/louis-%{version}-py*.egg-info
%endif
