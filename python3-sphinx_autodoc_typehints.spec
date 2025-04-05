#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Type hints (PEP 484) support for the Sphinx autodoc extension
Summary(pl.UTF-8):	Obsługa podpowiedzi o typach (PEP 484) do rozszerzenia Sphinksa autodoc
Name:		python3-sphinx_autodoc_typehints
Version:	3.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx_autodoc_typehints/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_autodoc_typehints/sphinx_autodoc_typehints-%{version}.tar.gz
# Source0-md5:	f6fcbf2df25198d6d0597a15550a9768
URL:		https://pypi.org/project/sphinx_autodoc_typehints/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-hatchling
BuildRequires:	python3-hatch-vcs >= 0.4
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
%py3_build_pyproject

%if %{with tests}
# test_format_annotation fails on some NDArray types
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests -k 'not test_format_annotation' \
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/sphinx_autodoc_typehints
%{py3_sitescriptdir}/sphinx_autodoc_typehints-%{version}.dist-info
