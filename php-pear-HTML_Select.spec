%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Select
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - class for generating HTML form select elements
Summary(pl):	%{_pearname} - klasa do generowania elementów select formularzy HTML
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9c9b84cc3b1595f6000ef1845829dae8
Patch:		%{name}-case.patch
URL:		http://pear.php.net/package/HTML_Select/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_Common >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML_Select provides an OOP way of generating HTML form select
elements.

In PEAR status of this package is: %{_status}.

%description -l pl
HTML_Select dostarcza zorientowanej obiektowo metody tworzenia
elementów select formularzy HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
