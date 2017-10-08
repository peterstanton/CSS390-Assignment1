echo -e "Total Tracks: $(find . -type f | grep ogg | wc -l) \n"


echo -e "Total Artists: $(find . -type f | grep ogg | cut -f3 -d '/' | sort -u | wc -l) \n"


echo -e "Multi-Genre Artist: \n $(find . -type f | grep ogg | cut -f2,3 -d '/' | sort -u | cut -f2 -d '/' | sort | uniq -d) \n"


echo -e "Multi-Disk Albums: \n $(find . -type f | grep ogg | cut -f4,5,6 -d '/' | grep [dD]isk\s*[1-9]/ | cut -f1 -d '/' | sort -u) \n"
