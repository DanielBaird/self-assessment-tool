
System Management
=================

Update a conversation
---------------------

When you receive an updated conversation spreadsheet:

1. make the next steps easier by renaming / save-as-ing the sheet to a short name with no spaces, e.g. `jcu-questions.xlsx` 

2. `scp` the file to the sat5p server, into the default user's `incoming` directory:

```
scp sat5p-comingsoon-1.xlsx ec2-user@203.101.226.29:incoming/ 
```

3. `ssh` into the server

```
ssh ec2-user@203.101.226.29
```

4. change into your `incoming` directory and check that your spreadsheet is there

```
cd ~/incoming
ls *.xlsx
```

5. run `excel2all` (from the `sat5ptools` package, check the [setup guide](setup.html) for installation instructions) to create the conversation data file and graph.  Specify the correct target institution's site directory for output; you will generally want to send incoming updates into the `-test` dir.

The default `ec2-user` user doesn't have permission to write to `/mnt/sites`, so use `sudo` to write there, and then reset ownership of `sites` contents back to `nginx`.

```
sudo excel2all ~/incoming/jcu-questions.xslx --make --makeformat pdf /mnt/sites/jcu-test/conversation
sudo chown --recursive nginx:nginx /mnt/sites
```

6. Confirm that the site you've just updated is working: jcu-test.sat5p.jcu.io


Update header, footer, or icons
-------------------------------

Each site is constructed from a set of files in its `/mnt/sites/` directory.

| filename               | purpose     |
|------------------------|-------------|
| `index.html`           | The core functionality of the Self Assessment Tool |
| `header.html`          | A header, loaded and added to the top of the page by `index.html` (unless disabled by adding `?noheader` to the URL). The institution may supply alternative header content. |
| `footer.html`          | A footer, loaded and added to the bottom of the page by `index.html` (unless disabled by adding the slightly incorrectly named `?noheader` option to the URL). The institution may supply alternative header content. |
| `conversation.json`    | The data file containing the conversation. |
| `conversation.dot`     | A graph specification describing the conversational flow. |
| `conversation.dot.pdf` | A PDF of the conversational graph, rendered as a PDF. |
| `logo.png`             | The institution's logo, included in the default `header.html`. |
| `uni.png`              | The avatar used for the institution during the conversation. |
| `user.png`             | The avatar used for the user during the conversation. |


`iframe` friendly mode
----------------------

The 'normal' display for the conversational interface uses a maximum width, and includes headers and footers as described in the preceding section.  This ensures a reasonable presentation in stand-alone mode, where the user visits the subdomain directly.

There is an alternative display mode that removes the header and footer and doesn't enforce a minimum width; this is for display in an iframe or other wrapping arrangement.  To show the conversation in `iframe` friendly mode, add `?noheader` to the url:

```
https://cqu.sat5p.jcu.io/?noheader
```


Tools - setup
-------------

The `sat5p` tools can convert an Excel spreadsheet into a conversation data file, and also into a flow graph that is good for checking through the conversation without tediously clicking all the possible paths in the web chat.

If you're setting up a server via this guide, you already have the source of the tools in a git repository; however, I recommend installing the "published" version of the tools to minimise messing around with Python.

Make sure you have a recent version of `pip`, a Python package installer. If you want to use `sat5p` tools on Windows, it's worth getting through this, as the tools you're installing will 🤞 work properly at your command line without you having to type full paths, even if your Python installation doesn't work that way.

First, check if you already have `pip`:

```
pip --version
```

If you get "command not found", here's how to install it:

##### on CentOS and RedHat with EPEL repository:

```
sudo yum install -y python-pip
sudo pip install --upgrade pip
```

##### on Ubuntu, Debian etc:

```
sudo apt-get install python-pip
sudo pip install --upgrade pip
```

##### on Windows... good luck:

```
start https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows
```

Once you have `pip`, you can install the tools:

```
sudo pip install sat5ptools
```

### GraphViz

[GraphViz](https://www.graphviz.org/) is optional, but recommended.  If it is available, sat5ptools can use it to make useful flow-charts as PNGs or PDFs (or any other format GraphViz supports):

```
sudo yum install -y graphviz
```

The conversation flowcharts are usually very narrow and long, so it's worth experimenting with which format is most useful for scrolling through -- some people report that Adobe Acrobat can't always show a long conversation.


Tools - using
-------------

There are four command line tools, summarised below.  Running `<command> --help` will produce detailed instructions on options for each command.

| tool           | purpose |
|----------------|---------|
| `sat5pconfig`  | Generates a config file with default settings, which you can edit and use to alter the bahaviour of the other tools                       |
| `excel2qns`    | Reads conversation questions from an Excel workbook and generates the JSON file required to deliver that conversation via the web interface |
| `excel2graph`  | Reads conversation questions from an Excel workbook and generates a DOT describing a graph of that conversion, and optionally runs GraphViz to produce an actual graph |
| `excel2all`    | Combines the behaviour of `excel2qns` and `excel2all`, and therefore is probably the command you'll use most of the time.               |






