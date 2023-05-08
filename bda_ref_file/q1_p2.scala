// Create an array of integers
val arr = Array(1, 2, 3, 4, 5)

// Define a parameterized function to print the sum of the first n elements of the array
def printArraySum(n: Int): Unit = {
  val sum = arr.take(n).sum
  println(s"The sum of the first $n elements of the array is $sum")
}

// Call the function with parameter n = 3
printArraySum(3)

