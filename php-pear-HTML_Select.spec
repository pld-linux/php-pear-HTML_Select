%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Select
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - small classes to handle common <select> lists
Summary(pl):	%{_pearname} - ma�e klasy do obs�ugi list <select>
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	0.1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides <select>lists for:
 - Country
 - UK counties
 - US States

%description -l pl
Dostarcza listy <select> do pyta� o:
 - kraj
 - kraje UK
 - stany US

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/I18N/%{_subclass}

install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/I18N/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/%{_subclass}/examples/*
%dir %{php_pear_dir}/I18N/%{_subclass}
%{php_pear_dir}/I18N/%{_subclass}/*.php
