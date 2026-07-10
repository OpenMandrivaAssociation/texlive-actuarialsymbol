%global tl_name actuarialsymbol
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Actuarial symbols of life contingencies and financial mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/actuarialsymbol
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialsymbol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialsymbol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialsymbol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands to compose actuarial symbols of life
contingencies and financial mathematics characterized by subscripts and
superscripts on both sides of a principal symbol. The package also
features commands to easily and consistently position precedence numbers
above or below statuses in symbols for multiple lives contracts. Since
the actuarial notation can get quite involved, the package defines a
number of shortcut macros to ease entry of the most common elements.
Appendix A of the package documentation lists the commands to typeset a
large selection of symbols of life contingencies. This package requires
actuarialangle.

