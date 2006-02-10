Summary: Library providing an API to use the Xen virtualization
Name: libvirt
Version: 0.0.4
Release: 1
License: LGPL
Group: Development/Libraries
Source: libvirt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://libvir.org/
BuildRequires: xen python python-devel
Requires: xen
Obsoletes: libvir
ExclusiveArch: i386 x86_64

%description
This C library provides an API to use the Xen virtualization framework,
and the virsh command line tool to control virtual domains.

%package devel
Summary: Libraries, includes, etc. to compile with the libvirt library
Group: Development/Libraries
Requires: libvirt = %{version}
Obsoletes: libvir-devel

%description devel
Includes and documentations for the C library providing an API to use
the Xen virtualization framework

%package python
Summary: Python bindings for the libvirt library
Group: Development/Libraries
Requires: libvirt = %{version}
Obsoletes: libvir-python
Requires: %{_libdir}/python%(echo `python -c "import sys; print sys.version[0:3]"`)

%description python
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the Xen virtualization framework.

%prep
%setup -q

%build
# 0.0.4 workaround timestamp in the future
find . -exec touch {} \;
%configure
make

%install
rm -fr %{buildroot}

%makeinstall
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.a

%clean
rm -fr %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README COPYING.LIB TODO
%{_bindir}/virsh
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root)

%{_libdir}/lib*.so
%{_includedir}/libvirt/*.h
%{_libdir}/pkgconfig/libvirt.pc

%doc docs/*.html docs/html docs/*.gif
%doc docs/libvirt-api.xml

%files python
%defattr(-, root, root)

%doc AUTHORS NEWS README COPYING.LIB
%{_libdir}/python*/site-packages/libvirt.py*
%{_libdir}/python*/site-packages/libvirtmod*
%doc python/TODO
%doc python/libvirtclass.txt

%changelog
* Fri Feb 10 2006 Daniel Veillard <veillard@redhat.com> 0.0.4-1
- fixes some problems in 0.0.3 due to the change of names

* Wed Feb  8 2006 Daniel Veillard <veillard@redhat.com> 0.0.3-1
- changed library name to libvirt from libvir, complete and test the python 
  bindings

* Sun Jan 29 2006 Daniel Veillard <veillard@redhat.com> 0.0.2-1
- upstream release of 0.0.2, use xend, save and restore added, python bindings
  fixed

* Wed Nov  2 2005 Daniel Veillard <veillard@redhat.com> 0.0.1-1
- created
