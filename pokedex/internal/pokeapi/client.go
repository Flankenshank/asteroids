package pokeapi

import (
	"net/http"
	"github.com/Flankenshank/pokedexcli/internal/pokecache"
	"time"
)

type Client struct {
	httpClient		http.Client
	cache	pokecache.Cache
}

func NewClient (timeout time.Duration, cacheInterval time.Duration) Client {
	return Client{
		httpClient: http.Client{Timeout: timeout},
		cache: pokecache.NewCache(cacheInterval),
	}
}