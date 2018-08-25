import * as blockstack from 'blockstack'

let options = {
   encrypt: true
 }

 blockstack.putFile("/privatekey.txt", "PrivateKey", options)
 .then(() => {

 })s