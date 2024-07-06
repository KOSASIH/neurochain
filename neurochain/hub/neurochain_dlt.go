package main

import (
	"fmt"
	"github.com/hyperledger/fabric-sdk-go/pkg/core/config"
	"github.com/hyperledger/fabric-sdk-go/pkg/fabsdk"
)

func main() {
	sdk, err := fabsdk.New(config.FromFile("config.yaml"))
	if err != nil {
		fmt.Println(err)
		return
	}
	defer sdk.Close()

	channelClient, err := sdk.ChannelClient("neurochain_channel", fabsdk.WithUser("admin"))
	if err != nil {
		fmt.Println(err)
		return
	}

	_, err = channelClient.Query("neurochain_chaincode", "query", []string{"foo", "bar"})
	if err != nil {
		fmt.Println(err)
		return
	}
}
