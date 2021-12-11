%define srcname webencodings
%global desc This is a Python implementation of the WHATWG Encoding standard.

%bcond_with doc
%bcond_with check

Name: python3-%{srcname}
Version: 0.5.1
Release: 1
BuildArch: noarch
License: BSD
Summary: Character encoding for the web
URL: https://github.com/gsnedders/python-%{srcname}
Source0: %{name}-%{version}.tar.bz2
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if %{with check}
BuildRequires: python3-pytest
%endif
%if %{with doc}
BuildRequires: python3-sphinx
%endif

%description
%{desc}


%if %{with doc}
%package doc
Summary: Documentation for python-webencodings


%description doc
Documentation for python-webencodings.
%endif


%prep
%autosetup -n %{name}-%{version}/upstream


%build
%py3_build

%if %{with doc}
PYTHONPATH=. sphinx-build-3 docs docs/_build

# Remove unneeded build artifacts.
rm -rf docs/_build/.buildinfo
rm -rf docs/_build/.doctrees
%endif


%install
%py3_install


%check
%if %{with check}
py.test-3
%endif

%if %{with doc}
%files doc
%license LICENSE
%doc docs/_build
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info
