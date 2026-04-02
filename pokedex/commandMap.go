package main

import (
	"fmt"
)

func commandMap(cfg *config) error {
	resp, err := cfg.pokeapiClient.GetLocationAreas(cfg.Next)
	if err != nil {
		return err
	}

	for _, location := range resp.Results {
		fmt.Println(location.Name)
	}

cfg.Next = resp.Next
cfg.Previous = resp.Previous

	return nil
}

