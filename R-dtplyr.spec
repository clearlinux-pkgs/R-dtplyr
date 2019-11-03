#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dtplyr
Version  : 0.0.3
Release  : 7
URL      : https://cran.r-project.org/src/contrib/dtplyr_0.0.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dtplyr_0.0.3.tar.gz
Summary  : Data Table Back-End for 'dplyr'
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-data.table
Requires: R-dplyr
Requires: R-lazyeval
Requires: R-rlang
BuildRequires : R-data.table
BuildRequires : R-dplyr
BuildRequires : R-lazyeval
BuildRequires : R-rlang
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
# dtplyr
[![Travis-CI Build Status](https://travis-ci.org/hadley/dtplyr.svg?branch=master)](https://travis-ci.org/hadley/dtplyr)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/dtplyr)](https://cran.r-project.org/package=dtplyr)
[![Coverage Status](https://img.shields.io/codecov/c/github/hadley/dtplyr/master.svg)](https://codecov.io/github/hadley/dtplyr?branch=master)

%prep
%setup -q -c -n dtplyr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571821003

%install
export SOURCE_DATE_EPOCH=1571821003
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dtplyr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dtplyr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dtplyr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dtplyr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dtplyr/DESCRIPTION
/usr/lib64/R/library/dtplyr/INDEX
/usr/lib64/R/library/dtplyr/Meta/Rd.rds
/usr/lib64/R/library/dtplyr/Meta/features.rds
/usr/lib64/R/library/dtplyr/Meta/hsearch.rds
/usr/lib64/R/library/dtplyr/Meta/links.rds
/usr/lib64/R/library/dtplyr/Meta/nsInfo.rds
/usr/lib64/R/library/dtplyr/Meta/package.rds
/usr/lib64/R/library/dtplyr/NAMESPACE
/usr/lib64/R/library/dtplyr/NEWS.md
/usr/lib64/R/library/dtplyr/R/dtplyr
/usr/lib64/R/library/dtplyr/R/dtplyr.rdb
/usr/lib64/R/library/dtplyr/R/dtplyr.rdx
/usr/lib64/R/library/dtplyr/help/AnIndex
/usr/lib64/R/library/dtplyr/help/aliases.rds
/usr/lib64/R/library/dtplyr/help/dtplyr.rdb
/usr/lib64/R/library/dtplyr/help/dtplyr.rdx
/usr/lib64/R/library/dtplyr/help/paths.rds
/usr/lib64/R/library/dtplyr/html/00Index.html
/usr/lib64/R/library/dtplyr/html/R.css
/usr/lib64/R/library/dtplyr/tests/testthat.R
/usr/lib64/R/library/dtplyr/tests/testthat/helper-data.R
/usr/lib64/R/library/dtplyr/tests/testthat/helpers-library.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-arrange.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-distinct.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-do.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-filter.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-group-by.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-joins.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-mutate.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-pronouns.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-sample.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-select.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-slice.R
