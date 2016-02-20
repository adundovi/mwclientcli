# mwclientcli
Extensions over [mwclient](https://github.com/mwclient/mwclient) to view and edit MediaWiki instance from a command line interface (CLI). Tailored for private and small wikis, not Wikipedia.

## Install

At the moment only a development version is available:
```
$ pip install git+https://github.com/adundovi/mwclientcli.git
```

## Usage

To display a page from the wiki:
```
$ wiki show Main_Page
```

To edit pages with `$EDITOR` (e.g. vim):
```
$ wiki edit Main_Page
```

To rename/move a page:
```
$ wiki move Main_Page Old_main_page
```

(...)
