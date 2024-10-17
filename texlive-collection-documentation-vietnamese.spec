# revision 13822
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-vietnamese
Epoch:		1
Version:	20120224
Release:	11
Summary:	Vietnamese documentation
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-vietnamese.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-amsldoc-vn
Requires:	texlive-lshort-vietnamese
Requires:	texlive-ntheorem-vn
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-vietnamese package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780278
- Update to latest release.
- Import texlive-collection-documentation-vietnamese
- Import texlive-collection-documentation-vietnamese

