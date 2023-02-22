***
### Learn about hashes by trying it yourself
***

#### Fast

djb2 hash is non-cryptographic. If you need to scale to handle a large number of items, djb2 hash will have less resource usage than a cryptographic hash. Daniel J Bernstein is DJB and someone you may enjoy reading up about on Wikipedia. No doubt he has a facscinating controversies section. A truly brilliant mathemetician.

#### Cryptographic

md5 and sha-N hashes are frequently used to help classify malware or avoid storing readable passwords in a user database. There are security vulnerabilities to many of the older implementations of cryptographic hashes so be sure to read up on best practice if you intend to use hashes for something other than comparison of bulk email campaigns. 

#### Take my advice with a grain of salt

Salted hashes are really great especially if no one forgets what the salt parameter was. Good security is hard.