Name:		texlive-hep-title
Version:	64907
Release:	2
Summary:	Extensions for the title page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hep-title
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-title.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-title.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-title.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hep-title package extends the title macros of the standard
classes with macros for a preprint, affiliation, editors, and
endorsers. The package is loaded with \usepackage{hep-title}.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hep-title
%{_texmfdistdir}/tex/latex/hep-title
%doc %{_texmfdistdir}/doc/latex/hep-title

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
