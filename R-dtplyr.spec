#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-dtplyr
Version  : 1.3.1
Release  : 41
URL      : https://cran.r-project.org/src/contrib/dtplyr_1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dtplyr_1.3.1.tar.gz
Summary  : Data Table Back-End for 'dplyr'
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-data.table
Requires: R-dplyr
Requires: R-glue
Requires: R-lifecycle
Requires: R-rlang
Requires: R-tibble
Requires: R-tidyselect
Requires: R-vctrs
BuildRequires : R-cli
BuildRequires : R-data.table
BuildRequires : R-dplyr
BuildRequires : R-glue
BuildRequires : R-lifecycle
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : R-tidyselect
BuildRequires : R-vctrs
BuildRequires : buildreq-R

%description
'dtplyr' is to allow you to write 'dplyr' code that is automatically
    translated to the equivalent, but usually much faster, data.table
    code.

%prep
%setup -q -n dtplyr
cd %{_builddir}/dtplyr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679503787

%install
export SOURCE_DATE_EPOCH=1679503787
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dtplyr/DESCRIPTION
/usr/lib64/R/library/dtplyr/INDEX
/usr/lib64/R/library/dtplyr/LICENSE
/usr/lib64/R/library/dtplyr/Meta/Rd.rds
/usr/lib64/R/library/dtplyr/Meta/features.rds
/usr/lib64/R/library/dtplyr/Meta/hsearch.rds
/usr/lib64/R/library/dtplyr/Meta/links.rds
/usr/lib64/R/library/dtplyr/Meta/nsInfo.rds
/usr/lib64/R/library/dtplyr/Meta/package.rds
/usr/lib64/R/library/dtplyr/Meta/vignette.rds
/usr/lib64/R/library/dtplyr/NAMESPACE
/usr/lib64/R/library/dtplyr/NEWS.md
/usr/lib64/R/library/dtplyr/R/dtplyr
/usr/lib64/R/library/dtplyr/R/dtplyr.rdb
/usr/lib64/R/library/dtplyr/R/dtplyr.rdx
/usr/lib64/R/library/dtplyr/doc/index.html
/usr/lib64/R/library/dtplyr/doc/translation.R
/usr/lib64/R/library/dtplyr/doc/translation.Rmd
/usr/lib64/R/library/dtplyr/doc/translation.html
/usr/lib64/R/library/dtplyr/help/AnIndex
/usr/lib64/R/library/dtplyr/help/aliases.rds
/usr/lib64/R/library/dtplyr/help/dtplyr.rdb
/usr/lib64/R/library/dtplyr/help/dtplyr.rdx
/usr/lib64/R/library/dtplyr/help/figures/logo.png
/usr/lib64/R/library/dtplyr/help/paths.rds
/usr/lib64/R/library/dtplyr/html/00Index.html
/usr/lib64/R/library/dtplyr/html/R.css
/usr/lib64/R/library/dtplyr/tests/testthat.R
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/count.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-call-pivot_longer.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-call-pivot_wider.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-call.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-colorder-relocate.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-colorder.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-group.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-join.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-mutate.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-subset-filter.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-subset-select.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-subset-separate.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-subset-slice.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step-subset-summarise.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/step.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/tidyeval-across.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/tidyeval.md
/usr/lib64/R/library/dtplyr/tests/testthat/_snaps/unite.md
/usr/lib64/R/library/dtplyr/tests/testthat/helpers-library.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-complete.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-count.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-fill.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-replace_na.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-call-pivot_longer.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-call-pivot_wider.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-call.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-colorder-relocate.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-colorder.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-first.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-group.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-join.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-modify.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-mutate.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-nest.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-set.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-subset-arrange.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-subset-do.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-subset-expand.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-subset-filter.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-subset-select.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-subset-separate.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-subset-slice.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-subset-summarise.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-subset-transmute.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step-subset.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-step.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-tidyeval-across.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-tidyeval.R
/usr/lib64/R/library/dtplyr/tests/testthat/test-unite.R
