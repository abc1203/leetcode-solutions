int strStr(char * haystack, char * needle){
    int idx = 0;
    if(strlen(needle) > strlen(haystack)) return -1;
    
    while(*(haystack + strlen(needle) - 1)) {
        char str[10000];
        strncpy(str, haystack, strlen(needle));
        str[strlen(needle)] = '\0';
        
        if(!strcmp(str, needle)) return idx;
            
        haystack++; idx++;
    }
    return -1;
}
