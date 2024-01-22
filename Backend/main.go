package main

import (
	"fmt"
	"net/http"
	"time"
)

type petition struct {
	title        string
	text         string
	startingDate time.Time
}

func OnIndex(w http.ResponseWriter, r *http.Request) {

}

func main() {
	fmt.Println("Server starting")

	http.HandleFunc("/", OnIndex)
}
