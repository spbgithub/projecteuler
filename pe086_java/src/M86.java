
public final class M86 {
	public static boolean isOk(long x, long sum_y_z) { 
		double d = Math.sqrt(x*x + sum_y_z*sum_y_z); 
		return d == (long) d; 
	}
	
	public static void main(String[] arg) { 
		long time = System.currentTimeMillis(); 
		long nSol = 0; long i; 
		for(i = 1; nSol <= 1000000; i++) { 
			for(int jk = 1; jk <= i+i; jk++) { 
				if(isOk(i,jk)) { 
					if(jk > i+1) nSol += (i+i+2-jk) / 2; 
				else nSol += jk / 2; } 
			} 
		} 
		System.out.println("Time:" + (System.currentTimeMillis() - time)); 
		System.out.println("M: " + (i+1) + " Number of solutions: " + nSol); 
	}
}
