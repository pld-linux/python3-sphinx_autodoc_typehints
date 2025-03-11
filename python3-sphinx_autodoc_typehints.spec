#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Type hints (PEP 484) support for the Sphinx autodoc extension
Summary(pl.UTF-8):	Obsługa podpowiedzi o typach (PEP 484) do rozszerzenia Sphinksa autodoc
Name:		python3-sphinx_autodoc_typehints
# 1.19.3+ uses hatchling instead of setuptools
# 1.19.2 requires Sphinx>=5.1.1
Version:	1.19.1
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx_autodoc_typehints/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_autodoc_typehints/sphinx_autodoc_typehints-%{version}.tar.gz
# Source0-md5:	410e410577be2a41bab152c1b0709ff2
URL:		https://pypi.org/project/sphinx_autodoc_typehints/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:50
BuildRequires:	python3-setuptools_scm >= 6
%if %{with tests}
BuildRequires:	python3-Sphinx >= 4.5
BuildRequires:	python3-nptyping >= 2.1.2
BuildRequires:	python3-pytest >= 7.1
BuildRequires:	python3-sphobjinv >= 2
BuildRequires:	python3-typing_extensions >= 4.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension allows you to use Python 3 annotations for documenting
acceptable argument types and return value types of functions.

%description -l pl.UTF-8
To rozszerzenie pozwala na używanie adnotacji Pythona 3 do
dokumentacji akceptowalnych typów argumentów i wartości zwracanych
przez funkcje.

%prep
%setup -q -n sphinx_autodoc_typehints-%{version}

%build
%py3_build

%if %{with tests}
# test_format_annotation fails on some NDArray types
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests -k 'not test_format_annotation' \
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/sphinx_autodoc_typehints
%{py3_sitescriptdir}/sphinx_autodoc_typehints-%{version}-py*.egg-info
