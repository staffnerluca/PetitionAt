package main

import (
	"time"
)

type Petition struct {
	Title        string    `json:"title"`
	Text         string    `json:"text"`
	StartingDate time.Time `json:"startingDate"`
	PolScore     int       `json:"polScore"`
	Attorney     string    `json:"attorney"`
	WebLink      string    `json:"webLink"`
}
