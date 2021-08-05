# Lab 18 - Cryptography

*Author*: Kassie Bradshaw

## Overview

Today we'll be tackling a cryptographic classic - the Caesar Cipher.

Your job will be to devise a method to encrypt to encrypt a message that can then be decrypted when supplied with the corresponding key.

But don't stop there! You'll also need to devise a way to decipher the encrypted message event when you do NOT have the key!

## Feature Tasks & Requirements

* [ ] Create an `encrypt` function that takes in a plain text phrase and a numeric shift.
  * The phrase will then be `shifted` that many letters
    * E.g. `encrypt('abc',1)` would return 'bcd'
    * E.g. `encrypt('abc',10)` would return 'klm'
  * Shifts that exceed 26 should wrap around
    * E.g. `encrypt('abc',27)` should return 'bcd'
  * Shifts that push a letter out of range should wrap around
    * E.g. `encrypt('zzz',1)` should return 'aaa'

* [ ] Create a `decrypt` function that takes in encrypted text and a numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
* [ ] Create a `crack` function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key
* [ ] Devise a method for the computer to determine if code was broken with minimal human guidance

## Implementation Notes

* In order to accomplish a certain task, you'll need access to a `corpus` of English words.
  * A search on something like "python list of English worlds
