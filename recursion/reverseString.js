var reverseString = function(s) {
    const N = s.length;
    
    for(let i = 0; i < N / 2; i++) {
        const j = N - 1 - i;
        [s[i], s[j]] = [s[j], s[i]];
    }
};

var reverseString2 = function(s) {
    start = 0 ;
    end = s.length-1;
    return helper(s,start,end);
};

function helper(s,start,end){
    if (start<end){
        temp = s[start];
        s[start] = s[end];
        s[end] = temp;
        return helper(s,start+1,end-1);
    } else{
        return s;
    }
};