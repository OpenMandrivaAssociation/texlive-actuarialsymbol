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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/actuarialsymbol
%dir %{_datadir}/texmf-dist/source/latex/actuarialsymbol
%dir %{_datadir}/texmf-dist/tex/latex/actuarialsymbol
%doc %{_datadir}/texmf-dist/doc/latex/actuarialsymbol/README.md
%doc %{_datadir}/texmf-dist/doc/latex/actuarialsymbol/actuarialsymbol.pdf
%doc %{_datadir}/texmf-dist/doc/latex/actuarialsymbol/mosaic.jpg
%doc %{_datadir}/texmf-dist/source/latex/actuarialsymbol/actuarialsymbol.dtx
%{_datadir}/texmf-dist/tex/latex/actuarialsymbol/actuarialsymbol.sty
