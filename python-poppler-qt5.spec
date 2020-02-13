%define _disable_ld_no_undefined 1
Name:		python-poppler-qt5
Version:	0.75.0
Release:	1
Summary:	Python bindings for the Poppler PDF rendering library
Group:		Office
License:	LGPLv2+
URL:		https://github.com/wbsoft/python-poppler-qt5
Source0:	https://github.com/wbsoft/python-poppler-qt5/releases/python-poppler-qt5-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-qt5-devel
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(poppler-qt5) >= 0.12.0
BuildRequires:	python-sip >= 4.9.1
BuildRequires:	python-distribute

%description
Python bindings for the Poppler PDF rendering library. It is needed to run
programs written in Python and using Poppler set.


%prep
%setup -q
%autopatch -p1

%install
export PATH=%_libdir/qt5/bin:$PATH
export CFLAGS='-std=c++11'
python setup.py install --single-version-externally-managed --root=%{buildroot} build_ext -lQt5Core,Qt5Gui

%files
%doc ChangeLog LICENSE TODO README.rst
%{python_sitearch}/popplerqt5.*.so
%{python_sitearch}/python_poppler*
