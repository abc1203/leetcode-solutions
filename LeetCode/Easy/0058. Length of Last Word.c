int lengthOfLastWord(char * s) {
    int prev = 0;
    int curr = 0;
    
    while(*s) {
        if(*s == ' ') {
            if(curr != 0) prev = curr;
            curr = 0;
        } else {
            curr++;
        }
        s++;        
    }
    
    printf("%d %d", prev, curr);
    if(curr != 0) return curr;
    return prev;
}
