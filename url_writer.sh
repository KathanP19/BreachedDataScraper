#!/bin/bash
echo "";
echo -e "[+] Before use, Copy/Paste Urls In File"
echo -ne "[+] Enter Url File Name: "
read url
wget -i $url
echo "";
echo "";
echo -e "[+] URLS have been written in file "
echo -ne "[+] Enter data search term to extract from downloaded files: "
read term
grep -e '$term' * > download_result
echo -e "[+] Data is extracted, see download_result file"
echo "";
