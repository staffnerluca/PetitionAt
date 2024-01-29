package main

import (
	"time"
)

type Petition struct {
	Id           uint      `gorm:"primary_key`
	Title        string    `json:"title"`
	Text         string    `json:"text"`
	StartingDate time.Time `json:"startingDate"`
	PolScore     int       `json:"polScore"`
	Attorney     string    `json:"attorney"`
	WebLink      string    `json:"webLink"`
}
