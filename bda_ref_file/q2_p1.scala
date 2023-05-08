// Scala program add two numbers
// using currying Function
object Curry
{
    // Define currying function
    def add(x: Int, y: Int) = x + y;
    def multiply(x: Int,y: Int) = x * y
    
    def main(args: Array[String])
    {
    	
   	 val a = 5
    	 val b = 10
    	 val sum = add(a, b)
    	 val mul= multiply(a,b)
   
        println(s"The sum of $a and $b is: $sum")
    	println(s"The product of $a and $b is: $mul")
    }
}

