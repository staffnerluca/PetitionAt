package main

import (
	"log"

	_ "github.com/lib/pq"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var db *gorm.DB

func connectToDB() *gorm.DB {
	if db != nil {
		return db
	}
	var con = "postgres://postgres:secret@localhost:5432/petitionAT?sslmode=disable"
	db, err := gorm.Open(postgres.Open(con), &gorm.Config{})
	if err != nil {
		log.Fatal(err)
	}
	return db
}

func createPetitionTable() {

}

func createUserTable() {}

func GetPetition() {}

func GetUser() {}
