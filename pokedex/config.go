package main

import (
    "github.com/Flankenshank/pokedexcli/internal/pokeapi"
)

type config struct {
    pokeapiClient pokeapi.Client
    Next     *string
    Previous *string
}