#!/bin/bash
echo "";
echo -e "[+] Before use, Copy/Paste Urls In File"
echo -ne "[+] Enter Url File Name: "
read url
wget -i $url
echo "";
echo "";
echo -e "[+] URLS have been written in file "
echo "";
