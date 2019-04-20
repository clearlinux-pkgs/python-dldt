#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-dldt
Version  : 2018.r5
Release  : 19
URL      : https://github.com/opencv/dldt/archive/2018_R5.tar.gz
Source0  : https://github.com/opencv/dldt/archive/2018_R5.tar.gz
Summary  : @PACKAGE_DESCRIPTION@
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: python-dldt-license = %{version}-%{release}
Requires: python-dldt-python = %{version}-%{release}
Requires: python-dldt-python3 = %{version}-%{release}
Requires: mxnet
Requires: networkx
Requires: numpy
Requires: onnx
Requires: opencv-python
Requires: protobuf
Requires: tensorflow
BuildRequires : Cython
BuildRequires : ade-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : dldt-dev
BuildRequires : googletest
BuildRequires : googletest-dev
BuildRequires : mkl-dnn-dev
BuildRequires : openblas
BuildRequires : opencv
BuildRequires : opencv-dev
BuildRequires : opencv-python
BuildRequires : pugixml-dev
BuildRequires : python-dev
BuildRequires : python3-dev
Patch1: 0001-Build-fixes.patch
Patch2: 0002-Add-fopenmp.patch
Patch3: 0003-Don-t-look-for-ade-in-a-subdir.patch
Patch4: 0004-Fix-Python-setup.py.patch

%description
# Validation Application
Inference Engine Validation Application is a tool that allows to infer deep learning models with
standard inputs and outputs configuration and to collect simple
validation metrics for topologies. It supports **top-1** and **top-5** metric for Classification networks and
11-points **mAP** metric for Object Detection networks.

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
%setup -q -n dldt-2018_R5
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
## build_prepend content
pushd inference-engine
mkdir -p clr-build
pushd clr-build
cmake -G 'Unix Makefiles' -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DLIB_SUFFIX=64 -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib .. -DENABLE_CLDNN=0 -DENABLE_INTEL_OMP=0 -DENABLE_OPENCV=0 -DENABLE_CLDNN_BUILD=1 -DENABLE_SAMPLES_CORE=1 -DENABLE_PYTHON=1 -DINSTALL_GMOCK=0 -DINSTALL_GTEST=0 -DBUILD_GMOCK=1 -DBUILD_GTEST=0 -DENABLE_GNA=0 -DCMAKE_CYTHON_EXECUTABLE=cython -DCMAKE_PYTHON_VERSION=3
pushd ie_bridges/python
make -j10
popd
cmake -G 'Unix Makefiles' -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DLIB_SUFFIX=64 -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib .. -DENABLE_CLDNN=0 -DENABLE_INTEL_OMP=0 -DENABLE_OPENCV=0 -DENABLE_CLDNN_BUILD=1 -DENABLE_SAMPLES_CORE=1 -DENABLE_PYTHON=1 -DINSTALL_GMOCK=0 -DINSTALL_GTEST=0 -DBUILD_GMOCK=1 -DBUILD_GTEST=0 -DENABLE_GNA=0 -DCMAKE_CYTHON_EXECUTABLE=cython -DCMAKE_PYTHON_VERSION=2 -DPYTHON_LIBRARY=/usr/lib64/libpython2.7.so -DPYTHON_EXECUTABLE=/usr/bin/python2 -DPYTHON_INCLUDE_DIR=/usr/include/python2.7
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
export SOURCE_DATE_EPOCH=1554348846
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export MAKEFLAGS=%{?_smp_mflags}
pushd inference-engine/ie_bridges/python
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-dldt
cp LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/LICENSE
cp inference-engine/samples/thirdparty/gflags/COPYING.txt %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_samples_thirdparty_gflags_COPYING.txt
cp inference-engine/tests/libs/gtest/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googlemock_LICENSE
cp inference-engine/tests/libs/gtest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googlemock_scripts_generator_LICENSE
cp inference-engine/tests/libs/gtest/googletest/LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googletest_LICENSE
cp inference-engine/thirdparty/clDNN/common/googletest-fused/License.txt %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_clDNN_common_googletest-fused_License.txt
cp inference-engine/thirdparty/clDNN/common/khronos_ocl_clhpp/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_clDNN_common_khronos_ocl_clhpp_LICENSE.txt
cp inference-engine/thirdparty/mkl-dnn/LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_mkl-dnn_LICENSE
cp inference-engine/thirdparty/mkl-dnn/src/cpu/xbyak/COPYRIGHT %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_mkl-dnn_src_cpu_xbyak_COPYRIGHT
cp inference-engine/thirdparty/mkl-dnn/tests/gtests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/python-dldt/inference-engine_thirdparty_mkl-dnn_tests_gtests_gtest_LICENSE
pushd inference-engine/ie_bridges/python
python3 -tt setup.py build  install --root=%{buildroot}
popd
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
install -m 0755 -D inference-engine/bin/intel64/RelWithDebInfo/lib/python_api/python3.7/openvino/inference_engine/ie_api.so %{buildroot}/usr/lib/python3.7/site-packages/openvino/inference_engine/ie_api.so
install -m 0755 -D inference-engine/bin/intel64/RelWithDebInfo/lib/python_api/python3.7/openvino/inference_engine/dnn_builder/dnn_builder.so %{buildroot}/usr/lib/python3.7/site-packages/openvino/inference_engine/dnn_builder/dnn_builder.so
install -m 0755 -D inference-engine/bin/intel64/RelWithDebInfo/lib/python_api/python2.7/openvino/inference_engine/ie_api.so %{buildroot}/usr/lib/python2.7/site-packages/openvino/inference_engine/ie_api.so
install -m 0755 -D inference-engine/bin/intel64/RelWithDebInfo/lib/python_api/python2.7/openvino/inference_engine/dnn_builder/dnn_builder.so %{buildroot}/usr/lib/python2.7/site-packages/openvino/inference_engine/dnn_builder/dnn_builder.so
rm -rf %{buildroot}/usr/lib/python2*/*
## install_append end

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-dldt/LICENSE
/usr/share/package-licenses/python-dldt/inference-engine_samples_thirdparty_gflags_COPYING.txt
/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googlemock_LICENSE
/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googlemock_scripts_generator_LICENSE
/usr/share/package-licenses/python-dldt/inference-engine_tests_libs_gtest_googletest_LICENSE
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
