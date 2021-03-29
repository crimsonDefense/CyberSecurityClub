

public class Hasher {

  public static void main(String[] paramArrayOfString) {

    int ans = 593779930;
    int A, B, C, D, E, F, G, H, I, J, K, L, M;

    int[] caps = {97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118,
    119, 120, 121, 122, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 83, 75, 89, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76,
    77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 90};

    for(int a = 0; a < caps.length; a++){
    	A = (7 * 31) + caps[a];
    	for(int b = 0; b < caps.length; b++){
    		B = (A * 31) + caps[b];
    		for(int c = 0; c < caps.length; c++){
    			C = (B * 31) + caps[c];
          for(int d = 0; d < caps.length; d++){
            D = (C * 31) + caps[d];
            for(int e = 0; e < caps.length; e++){
              E = (D * 31) + caps[e];
              for(int f = 0; f < caps.length; f++){
                F = (E * 31) + caps[f];
                for(int g = 0; g < caps.length; g++){
                  G = (F * 31) + caps[g];
                  if(G > 593779000 && G < 593779999){
                      System.out.println(G);
                  }
                  if(G == ans) {
                    System.out.println("Cracked");
                    System.out.println(caps[a] + " " + caps[b] + " " + caps[c] + " " + caps[d] + " " + caps[e] + " " + caps[f] + " " + caps[g]);
                    return;
                  }
                }
              }
            }
          }
        }
      }
    }

    System.out.println("Wrong");
  }
}
