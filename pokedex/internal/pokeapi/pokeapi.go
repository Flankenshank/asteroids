package pokeapi

import (
	"encoding/json"
	"io"
)

const (
	baseURL = "https://pokeapi.co/api/v2"
)

func (c *Client) GetLocationAreas(url *string) (LocationAreasResponse, error) {
	fullURL := baseURL + "/location-area"
	if url != nil {
		fullURL = *url
	}

	var body []byte
	
	if val, ok := c.cache.Get(fullURL); ok {
		// Cache hit - use cached data
		body = val
	} else {
		// Cache miss - fetch from API
		resp, err := c.httpClient.Get(fullURL)
		if err != nil {
			return LocationAreasResponse{}, err
		}
		defer resp.Body.Close()
		
		body, err = io.ReadAll(resp.Body)
		if err != nil {
			return LocationAreasResponse{}, err
		}
		
		c.cache.Add(fullURL, body)
	}
	
	var locationResp LocationAreasResponse
	err := json.Unmarshal(body, &locationResp)
	if err != nil {
		return LocationAreasResponse{}, err
	}
	
	return locationResp, nil
}