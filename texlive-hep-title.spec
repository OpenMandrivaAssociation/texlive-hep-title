%global tl_name hep-title
%global tl_revision 76220

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Extensions for the title page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hep-title
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-title.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-title.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-title.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The hep-title package extends the title macros of the standard classes
with macros for a preprint, affiliation, editors, and endorsers. The
package is loaded with \usepackage{hep-title}.

