# spacewalk-demo

Demo for workshop about Spacewalk

1. Create organization

http://demo.spacewalk.cloud/???

2. Register system

    # wget http://demo.spacewalk.cloud/pub/RHN-ORG-TRUSTED-SSL-CERT -O /usr/share/rhn/cert-demo.spacewalk.cloud
    # rhnreg_ks --serverUrl=https://demo.spacewalk.cloud/XMLRPC --sslCACert=/usr/share/rhn/cert-demo.spacewalk.cloud --username USERNAME --password PASSWORD
RHEL/CentOS

3. Client tools

 - Enable Spacewalk Client repository for your client
    - # rhn-channel --add -c spacewalk27-client-fedora26-x86_64
    - Systems > Software > Software Channels > Change Subscriptions

4. Configuration management

    # yum install rhncfg-management rhncfg-client rhncfg-actions

5. Kickstarts

6. Channels

7. ?
