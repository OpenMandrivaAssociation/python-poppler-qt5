%define _disable_ld_no_undefined 1
Name:		python-poppler-qt5
Version:	21.1.0
Release:	1
Summary:	Python bindings for the Poppler PDF rendering library
Group:		Office
License:	LGPLv2+
URL:		https://github.com/frescobaldi/python-poppler-qt5
Source0:	https://github.com/frescobaldi/python-poppler-qt5/archive/refs/tags/v21.1.0.tar.gz
Patch0:		https://github.com/frescobaldi/python-poppler-qt5/pull/45.patch
BuildRequires:	python-devel
BuildRequires:	python-qt5-devel
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(poppler-qt5) >= 0.12.0
BuildRequires:	python-distribute
BuildRequires:	python-sip

%description
Python bindings for the Poppler PDF rendering library. It is needed to run
programs written in Python and using Poppler set.

%package devel
Summary:	Development files for %{name}
Group:		Development/Python
Requires:	%{name} = %{EVRD}

%description devel
Development files for %{name}

%prep
%autosetup -p1
sip-build \
	--no-make

%build
%make_build -C build

%install
%make_install -C build INSTALL_ROOT=%{buildroot}

%files
%doc ChangeLog LICENSE TODO README.rst
%{python_sitearch}/popplerqt5.*.so
%{python_sitearch}/python_poppler*

%files devel
%{python_sitearch}/PyQt5/bindings/popplerqt5
