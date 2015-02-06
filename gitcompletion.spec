Summary: Bash completion for git and porcelains
Name: gitcompletion
Version: 0
Release: 0.20060726.4
Source0: %{name}.tar.bz2
Patch0: gitcompletion-path.patch
License: GPL
Group: Development/Other
Url: http://www.hawaga.org.uk/ben/tech/gitcompletion/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: bash-completion
Requires: git-core
BuildArch: noarch

%description
Bash completion for git and porcelains (stgit, cogito
and gitk).


%prep
%setup -q -n %{name}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}

cp all-compl $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/%{name}
cp cg-compl  git-compl  git-compl-lib  gitk-compl  stg-compl $RPM_BUILD_ROOT/%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%{_datadir}/%{name}
%doc README


