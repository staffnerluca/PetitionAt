package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

func OnGetPetition(w http.ResponseWriter, r *http.Request) {
	pet := Petition{
		Title:        "Title",
		Text:         "my Text",
		StartingDate: time.Now(),
		PolScore:     2,
		Attorney:     "Gustav",
		WebLink:      "myLink",
	}

	jData, err := json.Marshal(pet)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")

	_, err = w.Write(jData)
	if err != nil {
		fmt.Println(err)
		return
	}
}

func main() {
	fmt.Println("Server starting")

	http.HandleFunc("/GetPetition", OnGetPetition)
	err := http.ListenAndServe(":8081", nil)
	if err != nil {
		fmt.Println(err)
	}
}
