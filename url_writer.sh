#!/bin/bash
echo -e "[+] Copy and Paste Url In List"
echo -ne "[+] Provide List Name: "
read url
wget -i $url
echo "";
echo "";
echo "";
echo -e "[+] URLS have been written from file: $url "
echo "";
echo "";
