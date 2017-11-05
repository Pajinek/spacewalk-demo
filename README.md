# spacewalk-demo

Demo for workshop about Spacewalk

1. Create organization

Go to following site and crate new account:

http://www.spacewalk.cloud/


2. Register system

Create client system by docker

```
   # docker run -it spacewalk/demo-client
   # yum install -y http://demo.spacewalk.cloud/pub/rhn-org-trusted-ssl-cert-1.0-3.noarch.rpm
   # rhnreg_ks --serverUrl=https://demo.spacewalk.cloud/XMLRPC --username USERNAME --password PASSWORD
```

or you can use own system for it.

```
    # yum install -y http://demo.spacewalk.cloud/pub/rhn-org-trusted-ssl-cert-1.0-3.noarch.rpm
    # rhnreg_ks --serverUrl=https://demo.spacewalk.cloud/XMLRPC --username USERNAME --password PASSWORD
    # wget http://yum.spacewalkproject.org/RPM-GPG-KEY-spacewalk-2015
    # rpm --import RPM-GPG-KEY-spacewalk-2015
    # wget https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7
    # rpm --import RPM-GPG-KEY-EPEL-7

```


3. Client tools

 - Enable Spacewalk Client repository for your client
    - `# rhn-channel --add -c spacewalk27-client-fedora26-x86_64`
    - Systems > Software > Software Channels > Change Subscriptions

 - Upgrade
    - `# yum upgrade -y`


4. Configuration management

```
    # yum install rhncfg-management rhncfg-client rhncfg-actions
    # rhncfg-manager create-channel configchannel
    # wget https://github.com/Pajinek/spacewalk-demo/raw/master/bashrc
    # rhncfg-manager add -c configchannel -d /root/.bashrc bashrc
```
    - Systems > Configuration > Manage Configuration Channels > Subscribe to Channels > Continue
    - Systems > Configuration > Deploy Files > Deploy


5. Kickstarts


6. Channels

 * You may need to install some packages

```
    # yum install rpm-build wget unzip python-setuptools rhnpush
```

 * Create your channel on Spacewalk

    - Channels > Manage Software Channels > Create Channel
    - `# spacecmd -- softwarechannel_create -n NAME -l LABEL -p fedora26-x86_64 -a x86_64 -c sha1`
    - `# spacecmd -- softwarechannel_create -n NAME -l LABEL -p centos7-x86_64 -a x86_64 -c sha1`
    - API http://demo.spacewalk.cloud/pub/create-channel.py

 * Enable created channel for the client

 * Dowload source files

```
    # wget http://demo.spacewalk.cloud/pub/packages.zip
```

 * Build rpm

```
    # python setup.py bdist --format=rpm
```

 * Push created rpm into Spacewalk channel

```
    # rhnpush -c LABEL --nosig --server demo.spacewalk.cloud dist/spacewalk-demo-0.1-1.noarch.rpm
```

 * Install rpm on you client

```
    # yum install spacewalk-demo
    # sw-demo.py
```

7. ?
