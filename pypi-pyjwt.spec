#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyjwt
Version  : 2.4.0
Release  : 66
URL      : https://files.pythonhosted.org/packages/d8/6b/6287745054dbcccf75903630346be77d4715c594402cec7c2518032416c2/PyJWT-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d8/6b/6287745054dbcccf75903630346be77d4715c594402cec7c2518032416c2/PyJWT-2.4.0.tar.gz
Summary  : JSON Web Token implementation in Python
Group    : Development/Tools
License  : MIT
Requires: pypi-pyjwt-python = %{version}-%{release}
Requires: pypi-pyjwt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-py
BuildRequires : pypi-pytest
BuildRequires : pypi-pytest_runner
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
=====

%package python
Summary: python components for the pypi-pyjwt package.
Group: Default
Requires: pypi-pyjwt-python3 = %{version}-%{release}

%description python
python components for the pypi-pyjwt package.


%package python3
Summary: python3 components for the pypi-pyjwt package.
Group: Default
Requires: python3-core
Provides: pypi(pyjwt)

%description python3
python3 components for the pypi-pyjwt package.


%prep
%setup -q -n PyJWT-2.4.0
cd %{_builddir}/PyJWT-2.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652399459
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
