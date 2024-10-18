package main

import "fmt"

func x() error {
	return fmt.Errorf("hlloi")
}

func main() {
	fmt.Println("Hello")
	c := x()
	fmt.Println(c)
}
