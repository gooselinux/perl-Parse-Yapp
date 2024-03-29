Name:           perl-Parse-Yapp
Version:        1.05
Release:        41%{?dist}
Summary:        Perl extension for generating and using LALR parsers

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Parse-Yapp/
Source0:        http://www.cpan.org/authors/id/F/FD/FDESAR/Parse-Yapp-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Parse::Yapp (Yet Another Perl Parser compiler) is a collection of
modules that let you generate and use yacc like thread safe
(reentrant) parsers with perl object oriented interface.  The script
yapp is a front-end to the Parse::Yapp module and let you easily
create a Perl OO parser from an input grammar file.


%prep
%setup -q -n Parse-Yapp-%{version} 
chmod 644 README lib/Parse/{*.pm,Yapp/*.pm}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{_bindir}/yapp
%{perl_vendorlib}/Parse/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.05-41
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.05-38
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.05-37
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.05-36.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Tue Aug 29 2006 Patrice Dumas <dumas@centre-cired.fr> - 1.05-36
- rebuild for FC6

* Fri Feb 17 2006 Patrice Dumas <dumas@centre-cired.fr> - 1.05-35
- rebuild for fc5

* Wed Nov 16 2005 Warren Togami <wtogami@redhat.com> - 1.05-34
- import into Extras

* Wed Apr 20 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-33
- #155467
- Bring up to date with current Fedora.Extras perl spec template.

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 1.05-32
- rebuild

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 27 2003 Chip Turner <cturner@redhat.com>
- version bump and rebuild

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Tue Jun  4 2002 Chip Turner <cturner@redhat.com>
- properly claim directories owned by package so they are removed when package is removed

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 7 2001 root <root@redhat.com>
- Spec file was autogenerated. 
