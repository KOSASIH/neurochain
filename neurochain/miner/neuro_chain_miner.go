package main

import (
	"fmt"
	"neuro_chain_hub/miner"
)

type NeuroChainMiner struct {
	miner *miner.Miner
}

func NewNeuroChainMiner(miner *miner.Miner) *NeuroChainMiner {
	return &NeuroChainMiner{miner: miner}
}

func (n *NeuroChainMiner) Mine(block *miner.Block) (*miner.MinedBlock, error) {
	// Perform advanced mining algorithm using Goroutine
	ch := make(chan *miner.MinedBlock)
	go func() {
		result, err := n.miner.Mine(block)
		ch <- result
		close(ch)
	}()

	return <-ch, nil
}

func main() {
	miner := miner.NewMiner()
	n := NewNeuroChainMiner(miner)

	block := miner.NewBlock()
	minedBlock, err := n.Mine(block)
	if err!= nil {
		fmt.Println(err)
		return
	}

	fmt.Println(minedBlock)
}
