class Solution {
    public int minimumChairs(String s) {
        int chairs=0;
        int count=0;
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(ch=='E'){
                count++;
                if(count>chairs){
                    chairs++;
                }
            }
            else{
                count--;
            }
        }
        return chairs;
        
    }
}