SAT5P Setup
===========


nectar Deployment
-----------------

### Server creation

Create instance `sat5p-server-1` from nectar official *NeCTAR CentOS 7 x86_64* image, create `sat5p-sites` volume, and attach volume to instance.

Configure access:

* provide SSH key to Nectar and attach to instance, or another user adds manually
* Nectar menu *Compute* > *Access & Security* > default *Manage Rules*
    * add Ingress rules for HTTP and HTTPS with open CIDR (`0.0.0.0/0`)
    * add an Ingress rule for SSH and the CIDR spec for your institution:
        * JCU: `137.219.0.0/16`
        * CQU: `??`

Connect via SSH as `ec2-user`, using something like this:

```
ssh ec2-user@203.101.226.29
```

Partition and format attached volume using `fdisk` and `mkfs.ext4`, add to `/etc/fstab` with something like:

```
/dev/vdb1	/mnt/sites	ext4	defaults,noatime	0	2 
```

#### Project init

Install git and use it to clone the project's repository:

```
sudo yum install -y git
cd ~
git clone https://github.com/DanielBaird/self-assessment-tool.git
```


#### Web serving

Install `nginx` and set it up to start automatically

```
yum install -y nginx
systemctl enable nginx
```

This config file will try to find a directory in `/mnt/sites/` for any subdomain, so to create a new subdomain, all that is required is to add a subdirectory into `sites`, and add the domain to your [Let's Encrypt](https://letsencrypt.org) / [certbot](https://certbot.eff.org) certificate.

Create directories for the sites we're serving, add default content, and give them to the `nginx` user.

TODO: remember to get a clean "default" set into the repo

```
cd /mnt/sites
mkdir jcu jcu-test cqu cqu-test federation federation-test usc usc-test csu csu-test
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/cqu/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/cqu-test/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/jcu/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/jcu-test/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/federation/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/federation-test/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/usc/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/usc-test/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/csu/
sudo cp -r ~/self-assessment-tool/clientside/* /mnt/sites/csu-test/
sudo chown --recursive nginx:nginx /mnt/sites
```

We also need a directory for `certbot` to drop its challenge files.

```
mkdir /usr/share/nginx/html/letsencrypt
mkdir /usr/share/nginx/html/letsencrypt/.well-known
mkdir /usr/share/nginx/html/letsencrypt/.well-known/acme-challenge
```

Copy the nginx configuration files into place, and run Nginx's config tester.  You will need to edit the `sat5psites.conf` file once you have generated your certificates.

```
cp /home/ec2-user/self-assessment-tool/serverside/nginx.conf /etc/nginx/
cp /home/ec2-user/self-assessment-tool/serverside/sat5psites.conf /etc/nginx/conf.d/
nginx -t
```


#### Certificates for `https`

Install `certbot` for Nginx, and run it to generate a certificate

```
yum install -y certbot-nginx
certbot certonly --webroot --webroot-path /usr/share/nginx/html/letsencrypt --domains sat5p.jcu.io,jcu.sat5p.jcu.io,jcu-test.sat5p.jcu.io,cqu.sat5p.jcu.io,cqu-test.sat5p.jcu.io,federation.sat5p.jcu.io,federation-test.sat5p.jcu.io,usc.sat5p.jcu.io,usc-test.sat5p.jcu.io,csu.sat5p.jcu.io,csu-test.sat5p.jcu.io
##
## enter your email for alerts, agree to Let's Encrypt conditions, etc
##
```

Now edit the `sat5psites.conf` file and un-comment the two lines that point to the certificates certbot just generated for you.

```
vi /etc/nginx/conf.d/sat5psites.conf
# ...un-comment the certificate lines...
```











