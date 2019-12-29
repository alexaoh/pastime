package main

import  "fmt"  
import "time"

import "github.com/tj/go-spin"

func main(){  
    s := spin.New()
    s.Set(spin.Default);

    for i := 0; i < 30; i++ {
        fmt.Printf("\r  \033[36mcomputing\033[m %s ", s.Next())
        time.Sleep(100 * time.Millisecond)
    }

}
