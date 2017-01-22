# Gambit_task

TUF-2000M is an ultrasonic energy meter that has a Modbus interface described in docs/tuf-2000m.pdf.

As per my understanding from the problem description 

Input.text file contains the live text feed that shows the time of the reading followed by the first 100 register values.
Hello.py parses the text file, reads the register number and the corresponding values, and converts them into human readable format. 

In order to understand the human readable format, or into which data types the values need to be converted, I cross-checked the given examples with the manua provided ( docs/tuf-2000m.pdf ).

 From the manual (MODBUS register table), I understood that 
    -Long is a signed 4-byte integer
     Register 21-22, Negative energy accumulator is -56.

    -FLOAT/ REAL4 singular ieee-754 number
     Register 33-34, Temperature #1/inlet is 7.101173400878906.
    
    -INTEGER / high byte is step, low byte is signal quality. I am guessing  low byte is the last 4 bits of the input
     Register 92, Signal Quality is 38.
     
     Since the highest value in the live feed is 65535 which is less than 2 to the power 16, the values have to be 16 bit decimal format. I tried to reproduce the three example lines from the manual based on the docs as mentioned above. I began by writing three functions: for register 21-22, register 33-34, and register 92. This involved conversion of data to LONG, FLOAT, INTEGER respectivily.
     
     Where it involved more than one register, it involved conversion from current format to hexadecimal so that concanating the values is possible. After verifying the values with the function, I tried to incorporate the rest of the values to the same function depending on whether they need to be converted to INTEGER, FLOAT or LONG. 

My result:
(1, 2) -0.8598267436027527
(3, 4) -0.008671708405017853
(5, 6) -0.46402212977409363
(7, 8) 1343.789794921875
(9, 10) 0
(11, 12) 0.21618127822875977
(13, 14) 0
(17, 18) 57
(19, 20) 0.8638707995414734
(21, 22) -56
(23, 24) -0.885139524936676
(25, 26) 0
(29, 30) 90
(31, 32) 0.7490010857582092
(33, 34) 7.101173400878906
(35, 36) 4.701053619384766
(37, 38) 0.08159828186035156
(39, 40) 0.06944465637207031
(41, 42) -1.4928385019302368
(43, 44) 0.01631951332092285
(45, 46) 0.01631951332092285
(47, 48) 0.019097328186035156
(49, 50) 0
(51,) 0
(53, 55) 385947936
(56,) 0
(59,) 0
(60,) 255
(61,) 120
(62,) 0
(92,) 38
(93,) 3501
(94,) 3501
(96,) 1

 
