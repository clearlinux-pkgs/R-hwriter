#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-hwriter
Version  : 1.3.2
Release  : 15
URL      : https://cran.r-project.org/src/contrib/hwriter_1.3.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/hwriter_1.3.2.tar.gz
Summary  : HTML Writer - Outputs R objects in HTML format
Group    : Development/Tools
License  : LGPL-2.1
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
HTML format

%prep
%setup -q -c -n hwriter

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571845160

%install
export SOURCE_DATE_EPOCH=1571845160
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hwriter
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hwriter
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hwriter
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc hwriter || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/hwriter/DESCRIPTION
/usr/lib64/R/library/hwriter/INDEX
/usr/lib64/R/library/hwriter/Meta/Rd.rds
/usr/lib64/R/library/hwriter/Meta/features.rds
/usr/lib64/R/library/hwriter/Meta/hsearch.rds
/usr/lib64/R/library/hwriter/Meta/links.rds
/usr/lib64/R/library/hwriter/Meta/nsInfo.rds
/usr/lib64/R/library/hwriter/Meta/package.rds
/usr/lib64/R/library/hwriter/Meta/vignette.rds
/usr/lib64/R/library/hwriter/NAMESPACE
/usr/lib64/R/library/hwriter/R/hwriter
/usr/lib64/R/library/hwriter/R/hwriter.rdb
/usr/lib64/R/library/hwriter/R/hwriter.rdx
/usr/lib64/R/library/hwriter/doc/hwriter.R
/usr/lib64/R/library/hwriter/doc/hwriter.Rnw
/usr/lib64/R/library/hwriter/doc/hwriter.pdf
/usr/lib64/R/library/hwriter/doc/index.html
/usr/lib64/R/library/hwriter/help/AnIndex
/usr/lib64/R/library/hwriter/help/aliases.rds
/usr/lib64/R/library/hwriter/help/hwriter.rdb
/usr/lib64/R/library/hwriter/help/hwriter.rdx
/usr/lib64/R/library/hwriter/help/paths.rds
/usr/lib64/R/library/hwriter/html/00Index.html
/usr/lib64/R/library/hwriter/html/R.css
/usr/lib64/R/library/hwriter/images/hwriter.css
/usr/lib64/R/library/hwriter/images/iris1.jpg
/usr/lib64/R/library/hwriter/images/iris2.jpg
/usr/lib64/R/library/hwriter/images/iris3.jpg
/usr/lib64/R/library/hwriter/images/motif.png
/usr/lib64/R/library/hwriter/scripts/build.sh
