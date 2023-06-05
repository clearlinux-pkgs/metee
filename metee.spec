#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : metee
Version  : 3.2.3
Release  : 5
URL      : https://github.com/intel/metee/archive/3.2.3/metee-3.2.3.tar.gz
Source0  : https://github.com/intel/metee/archive/3.2.3/metee-3.2.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: metee-lib = %{version}-%{release}
Requires: metee-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Intel(R) ME TEE Library
Cross-platform access library for Intel(R) CSME HECI interface.

%package dev
Summary: dev components for the metee package.
Group: Development
Requires: metee-lib = %{version}-%{release}
Provides: metee-devel = %{version}-%{release}
Requires: metee = %{version}-%{release}

%description dev
dev components for the metee package.


%package doc
Summary: doc components for the metee package.
Group: Documentation

%description doc
doc components for the metee package.


%package lib
Summary: lib components for the metee package.
Group: Libraries
Requires: metee-license = %{version}-%{release}

%description lib
lib components for the metee package.


%package license
Summary: license components for the metee package.
Group: Default

%description license
license components for the metee package.


%prep
%setup -q -n metee-3.2.3
cd %{_builddir}/metee-3.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685986110
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685986110
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/metee
cp %{_builddir}/metee-%{version}/COPYING %{buildroot}/usr/share/package-licenses/metee/598f87f072f66e2269dd6919292b2934dbb20492 || :
cp %{_builddir}/metee-%{version}/src/linux/LICENSE.libmei %{buildroot}/usr/share/package-licenses/metee/c7267c875e2750d9cee1e9cc8c23055e1a992c93 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/metee.h
/usr/lib64/libmetee.so
/usr/share/man/man3/_TEEHANDLE.3
/usr/share/man/man3/metee.h.3
/usr/share/man/man3/teeDriverVersion_t.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/metee/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libmetee.so.3.2.3
/usr/lib64/libmetee.so.3.2.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/metee/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/metee/c7267c875e2750d9cee1e9cc8c23055e1a992c93
