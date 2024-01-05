int romanToInt(char *s){
    int n = 0;
    
    while(*s) {
        if(*s == 'I') {
            if(*(s+1) && *(s+1) == 'V') {
                n += 4;
                s+=2;
            } else if (*(s+1) && *(s+1) == 'X') {
                n += 9;
                s+=2;
            } else {
                n += 1;
                s++;
            }
        } else if(*s == 'X') {
            if(*(s+1) && *(s+1) == 'L') {
                n += 40;
                s+=2;
            } else if (*(s+1) && *(s+1) == 'C') {
                n += 90;
                s+=2;
            } else {
                n += 10;
                s++;
            }     
        } else if(*s == 'C') {
            if(*(s+1) && *(s+1) == 'D') {
                n += 400;
                s+=2;
            } else if(*(s+1) && *(s+1) == 'M') {
                n += 900;
                s+=2;
            } else {
                n += 100;
                s++;
            }
        } else if(*s == 'V') { 
            n += 5; s++; 
        } else if(*s == 'L') { 
            n += 50; s++; 
        } else if(*s == 'D') { 
            n += 500; s++; 
        } else if(*s == 'M') { 
            n += 1000; s++; 
        }
    }
    
  
    return n;
}
