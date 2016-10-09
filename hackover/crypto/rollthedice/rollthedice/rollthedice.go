package main

import (
	"bufio"
	"crypto/aes"
	"crypto/rand"
	"encoding/base64"
	"encoding/binary"
	"errors"
	"fmt"
	"io"
	"log"
	mrand "math/rand"
	"net"
	"strings"
)

const FLAG = "hackover16{REMOVED}"

func main() {
	l, err := net.Listen("tcp", "0.0.0.0:1415")
	if err != nil {
		log.Fatal(err)
	}
	defer l.Close()
	for {
		conn, err := l.Accept()
		if err != nil {
			log.Fatal(err)
		}
		go handleConnection(conn)
	}
}

func rollDice() int {
	// Momma told me to use cryptographic randomness instead ...
	roll := mrand.Intn(6) + 1
	return roll
}

func encryptDiceRoll(roll int) ([]byte, []byte) {
	key := make([]byte, 16)
	if _, err := io.ReadFull(rand.Reader, key); err != nil {
		log.Fatal(err)
	}
	block, err := aes.NewCipher(key)
	if err != nil {
		log.Fatal(err)
	}
	rollEncoded := make([]byte, aes.BlockSize)
	if _, err := io.ReadFull(rand.Reader, rollEncoded); err != nil {
		log.Fatal(err)
	}
	binary.BigEndian.PutUint16(rollEncoded, uint16(roll))
	block.Encrypt(rollEncoded, rollEncoded)
	return key, rollEncoded
}

func decryptDiceRoll(key []byte, diceRollEnc []byte) (int, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return -1, errors.New("Invalid key size")
	}
	if len(diceRollEnc) != aes.BlockSize {
		return -1, errors.New("Invalid block size")
	}
	block.Decrypt(diceRollEnc, diceRollEnc)
	return int(binary.BigEndian.Uint16(diceRollEnc)), nil
}

func handleConnection(conn net.Conn) {
	defer func() {
		log.Println(conn.RemoteAddr(), "disconnected")
		conn.Close()
	}()
	log.Println(conn.RemoteAddr(), "connected")

	fmt.Fprintln(conn, "Welcome to rollthedice!")
	fmt.Fprintln(conn, "We use a cool cryptographic scheme to do fair dice rolls.")
	fmt.Fprintln(conn, "You can easily proof that I don't cheat on you.")
	fmt.Fprintln(conn, "And I can easily proof that you don't cheat on me.\n")
	fmt.Fprintln(conn, "Rules are simple:\nRoll the opposite side of my dice roll and you win a round.")
	fmt.Fprintln(conn, "Win 32 consecutive rounds and I will give you a flag.\n")

	r := bufio.NewReader(conn)
	for i := 0; i < 32; i++ {
		myDiceRoll := rollDice()
		myKey, myDiceRollEnc := encryptDiceRoll(myDiceRoll)
		fmt.Fprintf(conn, "My dice roll: %s\n", base64.StdEncoding.EncodeToString(myDiceRollEnc))
		fmt.Fprintf(conn, "Your dice roll: ")
		yourDiceRollStr, err := r.ReadString('\n')
		if err != nil {
			return
		}
		yourDiceRollStr = strings.TrimSpace(yourDiceRollStr)
		fmt.Fprintf(conn, "My key: %s\n", base64.StdEncoding.EncodeToString(myKey))
		fmt.Fprintf(conn, "Your key: ")
		yourKeyStr, err := r.ReadString('\n')
		if err != nil {
			return
		}
		yourKeyStr = strings.TrimSpace(yourKeyStr)
		yourKey, err := base64.StdEncoding.DecodeString(yourKeyStr)
		if err != nil {
			fmt.Fprintln(conn, "Invalid key.")
			return
		}
		yourDiceRollEnc, err := base64.StdEncoding.DecodeString(yourDiceRollStr)
		if err != nil {
			fmt.Fprintln(conn, "Invalid dice roll.")
			return
		}
		yourDiceRoll, err := decryptDiceRoll(yourKey, yourDiceRollEnc)
		if err != nil {
			fmt.Fprintln(conn, err)
			return
		}

		if yourDiceRoll < 1 || yourDiceRoll > 6 {
			fmt.Fprintln(conn, "Don't cheat on me ...")
			return
		}

		if myDiceRoll+yourDiceRoll != 7 {
			fmt.Fprintf(conn, "%d is not on the opposite side of %d. You lose.\n", yourDiceRoll, myDiceRoll)
			return
		}
	}
	fmt.Fprintf(conn, "You win! How was that possible? However, here is your flag: %s\n", FLAG)
}
