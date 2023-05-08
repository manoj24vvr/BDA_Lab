object NestedFunctionExample {
  def main(args: Array[String]): Unit = {
    println(factorial(5))
  }

  def factorial(n: Int): Int = {
    def loop(acc: Int, x: Int): Int = {
      if (x == 0) acc
      else loop(acc * x, x - 1)
    }

    loop(1, n)
  }
}


