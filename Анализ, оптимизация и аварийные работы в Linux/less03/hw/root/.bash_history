yum install mc -y
mcedit /etc/sysconfig/network-scripts/ifcfg-ens33
cd /etc/sysconfig/network-scripts/
touch ifcfg-ens34
ls
mcedit ifcfg-ens34
uuid ens34
uuidgen ens34
mcedit ifcfg-ens34
ifup ifcfg-ens34
ip a
ping 192.168.23.16
ping 192.168.23.17
yum install pcs fence-agents-all -y
firewall-cmd --permanent --add-service=high-availability
firewall-cmd --reload
id hacluster
echo centos | passwd --stdin hacluster
systemctl enable pcsd
systemctl status pcsd
systemctl start pcsd
systemctl status pcsd
sudo yum install httpd. -y
sudo yum install httpd -y
sudo systemctl enable httpd
sudo systemctl start httpd
sudo systemctl status httpd
ifup ens33
ip a
lsblk
reboot
ll
lsblk
reboot
