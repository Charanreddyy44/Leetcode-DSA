class Solution {
    public boolean validDigit(int n, int x) {
        
        String str= String.valueOf(n);
        String s=""+x;

        if(str.startsWith(s)){
            return false;
        }

        if(str.contains(s)){
            return true;
        }

        return false;
    }
}