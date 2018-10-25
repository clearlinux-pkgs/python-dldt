#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-dldt
Version  : 2018.r3
Release  : 1
URL      : https://github.com/opencv/dldt/archive/2018_R3.tar.gz
Source0  : https://github.com/opencv/dldt/archive/2018_R3.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 MIT
Requires: python-dldt-license = %{version}-%{release}
Requires: python-dldt-python = %{version}-%{release}
Requires: python-dldt-python3 = %{version}-%{release}
Requires: networkx
Requires: numpy
Requires: onnx
Requires: opencv-python
Requires: protobuf
Requires: tensorflow
BuildRequires : Cython
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : dldt-data
BuildRequires : dldt-dev
BuildRequires : googletest
BuildRequires : googletest-dev
BuildRequires : mkl-dnn-dev
BuildRequires : openblas
BuildRequires : opencv
BuildRequires : opencv-dev
BuildRequires : opencv-python
BuildRequires : pugixml-dev
Patch1: 0001-Build-fixes.patch

%description
The Google Mock class generator is an application that is part of cppclean.
visit http://code.google.com/p/cppclean/

%package license
Summary: license components for the python-dldt package.
Group: Default

%description license
license components for the python-dldt package.


%package python
Summary: python components for the python-dldt package.
Group: Default
Requires: python-dldt-python3 = %{version}-%{release}

%description python
python components for the python-dldt package.


%package python3
Summary: python3 components for the python-dldt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-dldt package.


%prep
%setup -q -n dldt-2018_R3
%patch1 -p1

%build
## build_prepend content
pushd inference-engine
mkdir -p clr-build
pushd clr-build
cmake -G 'Unix Makefiles' -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DLIB_SUFFIX=64 -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib .. -DENABLE_CLDNN=0 -DENABLE_INTEL_OMP=0 -DENABLE_OPENCV=0 -DENABLE_CLDNN_BUILD=1 -DENABLE_SAMPLES_CORE=1 -DENABLE_PYTHON_BINDINGS=1 -DINSTALL_GMOCK=0 -DINSTALL_GTEST=0 -DBUILD_GMOCK=1 -DBUILD_GTEST=0
pushd ie_bridges/python
make -j10
popd
popd
popd
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540470604
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
pushd inference-engine/clr-build/ie_bridges/python
python3 setup.py build

popd
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-dldt
cp LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/LICENSE
cp inference-engine/samples/thirdparty/gflags/COPYING.txt %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_samples_thirdparty_gflags_COPYING.txt
cp inference-engine/tests/libs/gtest/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googlemock_LICENSE
cp inference-engine/tests/libs/gtest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googlemock_scripts_generator_LICENSE
cp inference-engine/tests/libs/gtest/googletest/LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googletest_LICENSE
cp inference-engine/thirdparty/clDNN/common/boost/1.64.0/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_clDNN_common_boost_1.64.0_LICENSE_1_0.txt
cp inference-engine/thirdparty/clDNN/common/googletest-fused/License.txt %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_clDNN_common_googletest-fused_License.txt
cp inference-engine/thirdparty/clDNN/common/khronos_ocl_clhpp/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_clDNN_common_khronos_ocl_clhpp_LICENSE.txt
cp inference-engine/thirdparty/mkl-dnn/LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_mkl-dnn_LICENSE
cp inference-engine/thirdparty/mkl-dnn/src/cpu/xbyak/COPYRIGHT %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_mkl-dnn_src_cpu_xbyak_COPYRIGHT
cp inference-engine/thirdparty/mkl-dnn/tests/gtests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_mkl-dnn_tests_gtests_gtest_LICENSE
pushd inference-engine/clr-build/ie_bridges/python
python3 -tt setup.py build  install --root=%{buildroot}
popd
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-dldt/LICENSE
/usr/share/package-licenses/python-dldt/inference-engine_samples_thirdparty_gflags_COPYING.txt
/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googlemock_LICENSE
/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googlemock_scripts_generator_LICENSE
/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googletest_LICENSE
/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_clDNN_common_boost_1.64.0_LICENSE_1_0.txt
/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_clDNN_common_googletest-fused_License.txt
/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_clDNN_common_khronos_ocl_clhpp_LICENSE.txt
/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_mkl-dnn_LICENSE
/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_mkl-dnn_src_cpu_xbyak_COPYRIGHT
/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_mkl-dnn_tests_gtests_gtest_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*