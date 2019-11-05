# Huffman Coding  
  
### Part 1  
Here, a huffman code, "huffCode.txt", is created based on character frequency in fileOne, then fileTwo is encoded and decoded using the respective functions.  
  
### Part 2  
Here, three huffman codes are created based on three different canonical collections of .txt files. Each is then used to encode the 5 files in "data". Below is a comparison of the file sizes after each encoding.
  

| **"data" .txt file** | Original size | CC1 Encoded* | CC2 Encoded* | CC3 Encoded*|
|:---:|:---|:---|:---|:---|
|`EarthASCII.txt` | 438.3 kB  | 1075 kB | 300 kB  | 250 kB  |
|`MysteryASCII.txt` | 444.6 kB  | 1175 kB | 312 kB  | 262.5 kB  |
|`MythsASCII.txt` | 740.7 kB  | 2100 kB | 650 kB  | 450 kB  |
|`SimakASCII.txt` | 310.1 kB  | 812.5 kB | 212.5 kB  | 175 kB  |
|`WodehouseASCII.txt` | 403.3 kB  | 1050 kB | 275 kB  | 225 kB  |  
  
(* = since string '0's and '1's were used to simulate bits, a byte = bit conversion was applied for the size of encoded files.)  
  
The 1st CC is the worst (and actually increases program size) since the character frequency was based upon a list of lowercase words lacking any punctuation. This differs drastically from the collection of .txt files in "data" being encoded.  
  
Both the 2nd & 3rd improve the file sizes similarly because of similar file structure between the canonical collections & "data". CC3 out performs CC2 because of the length of files, a larger 'sample space' leads directly to more accurate character frequencies.
