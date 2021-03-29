package database;
public class Hasher {
  private static boolean hash(String paramString) {
    int i = 7;
    int j = 593779930;
    for (byte b = 0; b < paramString.length(); b++)
      i = i * 31 + paramString.charAt(b); 
    return (i == j);
  }
  
  public static void main(String[] paramArrayOfString) {
    if (paramArrayOfString.length != 1) {
      System.out.println("Usage: java Hasher <password>");
      System.exit(1);
    } 
    if (hash(paramArrayOfString[0])) {
      System.out.println("Correct");
    } else {
      System.out.println("Incorrect");
    } 
  }
}