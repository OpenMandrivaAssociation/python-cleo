Summary:	Create beautiful and testable command-line interfaces for Python
Name:		python-cleo
Version:	2.0.1
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/cleo/
Source0:	https://files.pythonhosted.org/packages/source/c/cleo/cleo-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildArch:	noarch

%description
Cleo allows you to create beautiful and testable command-line interfaces.

%files
%doc README.md
%{py_sitedir}/cleo
%{py_sitedir}/cleo-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n cleo-%{version}

%build
%py_build

%install
%py_install

