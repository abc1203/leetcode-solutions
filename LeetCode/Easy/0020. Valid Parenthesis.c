bool isValid(char * s){
    char arr[10001]; int idx = 0;
    
    while(*s) {
        arr[idx] = *s;
        //printf("%s\n", arr);
        idx++;
        
        if(idx >= 2 && 
           ((arr[idx-2] == '(' && arr[idx-1] == ')') || 
            (arr[idx-2] == '[' && arr[idx-1] == ']') || 
            (arr[idx-2] == '{' && arr[idx-1] == '}'))) {
            arr[idx-2] = '\0'; arr[idx-1] = '\0'; 
            idx-=2;
        }
        s++;
    }
    
    //printf("%s\n", arr);
    if(arr[0] == '\0') {
        return true;
    } else {
        return false;
    }
    

}
