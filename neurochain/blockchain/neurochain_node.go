package main

import (
	"fmt"
	"github.com/KOSASIH/neurochain/neurochain/blockchain"
)

func main() {
	node := blockchain.NewNode("localhost:8080")
	node.Start()
	fmt.Println("NeuroChain node started")
}
