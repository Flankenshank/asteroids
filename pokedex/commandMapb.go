package main

import (
	"fmt"
)

func commandMapb(cfg *config) error {
	if cfg.Previous == nil {
	fmt.Println("you're on the first page")
	return nil
}
	resp, err := cfg.pokeapiClient.GetLocationAreas(cfg.Previous)
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

