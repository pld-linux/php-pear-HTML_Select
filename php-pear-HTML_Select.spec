%define		status		stable
%define		pearname	HTML_Select
Summary:	%{pearname} - class for generating HTML form select elements
Summary(pl.UTF-8):	%{pearname} - klasa do generowania elementów select formularzy HTML
Name:		php-pear-%{pearname}
Version:	1.3.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	5643561c512416b41dbf1e68acb0cae4
Patch0:		%{name}-case.patch
URL:		http://pear.php.net/package/HTML_Select/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-HTML_Common >= 1.1
Requires:	php-pear-PEAR-core >= 1:1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML_Select provides an OOP way of generating HTML form select
elements.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
HTML_Select dostarcza zorientowanej obiektowo metody tworzenia
elementów select formularzy HTML.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup
%patch0 -p1

mv .%{php_pear_dir}/data/HTML_Select/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/*.php
