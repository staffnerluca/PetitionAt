package main

import (
	"time"
)

type User struct {
	Username   string    `json:"username"`
	Firstname  string    `json:"firstname"`
	Secondname string    `json:"secondname"`
	Mail       string    `json:"mail"`
	JoinedOn   time.Time `json:"joinedOn"`
	Password   string    `json:"password"`
}
