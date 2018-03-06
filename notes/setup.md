
nectar Deployment
=================

Initial setup
-------------

Create instance `sat5p-server-1` from nectar official *NeCTAR CentOS 7 x86_64* image, create `sat5p-sites` volume, and attach volume to instance.

Configure access:

* provide SSH key to Nectar and attach to instance, or another user adds manually
* Nectar menu *Compute* > *Access & Security* > default *Manage Rules*
** add Ingress rules for HTTP and HTTPS with open CIDR (`0.0.0.0/0`)
** add an Ingress rule for SSH and the CIDR spec for your institution:
*** JCU: `137.219.0.0/16`
*** CQU: `??`

Connect via SSH as ec2-user, using something like:

```
ssh ec2-user@203.101.226.29
```

Partition and format attached volume using `fdisk` and `mkfs.ext4`, add to `/etc/fstab` with something like:

```
/dev/vdb1	/mnt/sites	ext4	defaults,noatime	0	2 
```

### Project init

Install git and use it to clone the project's repository:

```
sudo yum install -y git
cd ~
git clone https://github.com/DanielBaird/self-assessment-tool.git
```


### Web serving

Install `nginx` and set it up to start automatically

```
yum install -y nginx
systemctl enable nginx
```

Copy the `sat5psites.conf` configuration file into `nginx`'s `/etc/nginx/conf.d/` dir, and run Nginx's config tester:

TODO update path to get config from git repo

```
cp /where/ever/sat5psites.conf /etc/nginx/conf.d/
nginx -t
```

This config file will try to find a directory in `/mnt/sites/` for any subdomain, so to create a new subdomain, all that is required is to add a subdirectory into `sites`, and add the domain to your [Let's Encrypt](https://letsencrypt.org) / [certbot](https://certbot.eff.org) certificate.

Create directories for the sites we're serving, add default content, and give them to the `nginx` user.

TODO: remember to get a clean "default" set into the repo, and delete `now.json`

```
cd /mnt/sites
mkdir jcu jcu-test cqu cqu-test
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/cqu/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/cqu-test/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/jcu/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/jcu-test/
sudo chown --recursive nginx:nginx /mnt/sites
```


### Certificates for `https`

TODO: finish this

Install `certbot` for Nginx, and run it to generate a certificate

```
yum install -y certbot-nginx
systemctl enable nginx
```

Run `certbot` to get certificates for your sites.
```
certbot --nginx --domains jcu.sat5p.jcu.io,jcu-test.sat5p.jcu.io,cqu.sat5p.jcu.io,cqu-test.sat5p.jcu.io
##
## enter your email for alerts, agree to Let's Encrypt conditions, etc
##
```


Tools setup
-----------

The `sat5p` tools can convert an Excel spreadsheet into a conversation data file, and also into a flow graph that is good for checking through the conversation without tediously clicking all the possible paths in the web chat.

If you've been following this install guide from the top, you already have the source of the tools in a git repository; however, I recommend installing the "published" version of the tools to minimise messing around with Python.

Make sure you have a recent version of `pip`, a Python package installer. If you want to use `sat5p` tools on Windows, it's worth getting through this, as the tools you're installing will 🤞 work properly at your command line without you having to type full paths, even if your Python installation doesn't work that way.

First, check if you already have `pip`:

```
pip --version
```

If you get "command not found", here's how to install it:

```
## on CentOS and RedHat with EPEL repository:
sudo yum install -y python-pip
sudo pip install --upgrade pip

## on Ubuntu, Debian etc:
sudo apt-get install python-pip
sudo pip install --upgrade pip

## on Windows, good luck:
start https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows
```

Once you have `pip`, you can install the tools:

```
sudo pip install sat5ptools
```

This installs four command line tools, summarised below.  Running `<command> --help` will produce detailed instructions on options for each command.

| tool           | purpose |
|----------------|---------|
| `sat5pconfig`  | Generates a config file with default settings, which you can edit and use to alter the bahaviour of the other tools |
| `excel2qns`    | Reads conversation questions from an Excel workbook and generates the JSON file required to deliver that conversation via the web interface |
| `excel2graph`  | Reads conversation questions from an Excel workbook and generates the DOT file required to create a graph of that conversion, and optionally runs GraphViz to produce a graphic of the graph |
| `excel2all`    | Combines the behaviour of `excel2qns` and `excel2all`, and therefore is probably the command you'll use most of the time. |

Also install [GraphViz](https://www.graphviz.org/) so you can get pretty graphs as PNGs or PDFs or whatever:

```
sudo yum install -y graphviz
```










