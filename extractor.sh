#!/bin/bash
echo "";
echo -ne "[+] Enter Search Term to Extract from all files: "
read term
grep -e "$term" * > download_results
echo -e "[+] Data extracted and saved in download_results"
echo "";
