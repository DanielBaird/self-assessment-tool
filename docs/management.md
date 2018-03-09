
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






