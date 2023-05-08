// Create an array of integers
val arr = Array(1, 2, 3, 4, 5)

// Define a non-parameterized function to print the sum of the array
def printArraySum(): Unit = {
  val sum = arr.sum
  println(s"The sum of the array is $sum")
}

// Call the function
printArraySum()
