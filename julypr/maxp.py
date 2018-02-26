last = arr[n-1];
for(int i=n-1;i>=0;i--){
       if(arr[i] > last) last = arr[i]; // else
       ans += last - arr[i];
      }
      ww.println(ans);
