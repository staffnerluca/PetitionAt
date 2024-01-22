package main

import (
	"time"
)

type petition struct {
	title        string
	text         string
	startingDate time.Time
	polScore     int
	attorney     string
	webLink      string
}
