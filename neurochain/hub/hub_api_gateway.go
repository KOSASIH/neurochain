package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/api/v1/neurochain", neuroChainHandler)
	http.ListenAndServe(":8080", nil)
}

func neuroChainHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Welcome to NeuroChain Hub API!")
}
