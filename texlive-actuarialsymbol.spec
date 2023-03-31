Name:		texlive-actuarialsymbol
Version:	54080
Release:	2
Summary:	Actuarial symbols of life contingencies and financial mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/actuarialsymbol
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialsymbol.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialsymbol.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialsymbol.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands to compose actuarial symbols of
life contingencies and financial mathematics characterized by
subscripts and superscripts on both sides of a principal
symbol. The package also features commands to easily and
consistently position precedence numbers above or below
statuses in symbols for multiple lives contracts. Since the
actuarial notation can get quite involved, the package defines
a number of shortcut macros to ease entry of the most common
elements. Appendix A of the package documentation lists the
commands to typeset a large selection of symbols of life
contingencies. This package requires actuarialangle.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/actuarialsymbol
%{_texmfdistdir}/tex/latex/actuarialsymbol
%doc %{_texmfdistdir}/doc/latex/actuarialsymbol

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
