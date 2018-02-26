package may1d;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class May1d {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
			Reader.init(System.in);
			int n=Reader.nextInt();
			int k=Reader.nextInt();
			int p=Reader.nextInt();
			//int max=0;
			int[] arr=new int[n];
			
			for(int i=0;i<n;i++){
				arr[i]=Reader.nextInt();
			}
			String s=Reader.next();
			int j=0;
			while(j<p){
				if(s.charAt(j) == '!'){
					int as=arr[n-1];
					/*for(int k1=n-1; k1>=1;k1--){
						arr[k1]=arr[k1-1];
					}
					arr[0]=as;*/
					System.arraycopy(arr,0, arr,1,n-1);
					arr[0]=as;
				}
				else if(s.charAt(j) == '?'){
					int max_sum=0;
					if(n < k){
						for(int j2=0;j2<n;j2++){
							max_sum+=arr[j2];
						}
					}
					else{
					for(int i=0;i<k;i++)
						max_sum+=arr[i];
					int window_sum=max_sum;
					for(int i=k;i<n;i++){
						window_sum+=arr[i]-arr[i-k];
						if(window_sum > max_sum)
							max_sum=window_sum;
					}
					}
					System.out.println(max_sum);
					while(j+1<p && s.charAt(j+1)=='?'){
						System.out.println(max_sum);
						j++;
						//System.out.println("li");
					}
				}
				j++;
			}
	}
}
/** Class for buffered reading int and double values */
class Reader {
    static BufferedReader reader;
    static StringTokenizer tokenizer;

    /** call this method to initialize reader for InputStream */
    static void init(InputStream input) {
        reader = new BufferedReader(
                     new InputStreamReader(input) );
        tokenizer = new StringTokenizer("");
    }

    /** get next word */
    static String next() throws IOException {
        while ( ! tokenizer.hasMoreTokens() ) {
            //TODO add check for eof if necessary
            tokenizer = new StringTokenizer(
                   reader.readLine() );
        }
        return tokenizer.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt( next() );
    }
	
    static double nextDouble() throws IOException {
        return Double.parseDouble( next() );
    }
}